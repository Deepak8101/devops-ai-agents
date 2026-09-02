
from google.genai import types

from ai_client import ask_ai
from tool_registry import TOOLS, TOOL_DEFINITIONS


def run_agent(user_question: str):

    # Conversation history that will be passed back to the LLM
    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=user_question
                )
            ]
        )
    ]

    while True:

        # Ask the LLM what to do next
        response = ask_ai(
            messages,
            tools=TOOL_DEFINITIONS
        )

        print("\nFUNCTION CALLS:")
        print(response.function_calls)

        # ---------------------------------------------------------
        # No tool call = LLM has enough information to answer
        # ---------------------------------------------------------
        if not response.function_calls:
            print("\nFINAL RESPONSE:")
            print(response.text)

            return response.text

        # ---------------------------------------------------------
        # Preserve the model's response containing function calls
        # ---------------------------------------------------------
        model_content = response.candidates[0].content

        messages.append(model_content)

        # ---------------------------------------------------------
        # Execute every tool requested by the LLM
        # ---------------------------------------------------------
        for function_call in response.function_calls:

            print("\nFUNCTION CALL OBJECT:")
            print(function_call)

            tool_name = function_call.name
            tool_args = function_call.args

            print("\nTOOL NAME:")
            print(tool_name)

            print("\nTOOL ARGUMENTS:")
            print(tool_args)

            # Find the actual Python function
            tool = TOOLS[tool_name]

            print("\nTOOL OBJECT:")
            print(tool)

            # Execute the function with the arguments
            tool_result = tool(**tool_args)

            print("\nTOOL RESULT:")
            print(tool_result)

            # Build the response that goes back to the LLM
            function_response_part = types.Part.from_function_response(
                name=tool_name,
                response={
                    "result": tool_result
                }
            )

            messages.append(function_response_part)
