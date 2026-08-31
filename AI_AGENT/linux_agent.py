from google.genai import types

from ai_client import ask_ai
from tool_registry import TOOLS, TOOL_DEFINITIONS


def run_agent(user_question: str):

    # --------------------------------
    # 1. First LLM call
    # --------------------------------

    response = ask_ai(
        user_question,
        tools=TOOL_DEFINITIONS
    )

    print("FUNCTION CALLS:")
    print(response.function_calls)

    # --------------------------------
    # 2. Check if LLM requested a tool
    # --------------------------------

    if response.function_calls:

        function_call = response.function_calls[0]

        print("\nFUNCTION CALL OBJECT:")
        print(function_call)

        tool_name = function_call.name
        tool_args = function_call.args

        print("\nTOOL NAME:")
        print(tool_name)

        print("\nTOOL ARGUMENTS:")
        print(tool_args)

        # --------------------------------
        # 3. Look up actual Python function
        # --------------------------------

        tool = TOOLS[tool_name]

        print("\nTOOL OBJECT:")
        print(tool)

        # --------------------------------
        # 4. Execute tool
        # --------------------------------

        tool_result = tool(**tool_args)

        print("\nTOOL RESULT:")
        print(tool_result)

        # --------------------------------
        # 5. Build user's original message
        # --------------------------------

        user_content = types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text=user_question
                )
            ]
        )

        # --------------------------------
        # 6. Get the model's original
        #    function-call message
        # --------------------------------

        function_call_content = response.candidates[0].content

        # --------------------------------
        # 7. Build function response
        # --------------------------------

        function_response_part = types.Part.from_function_response(
            name=tool_name,
            response={
                "result": tool_result
            }
        )


        # --------------------------------
        # 8. Second LLM call
        # --------------------------------

        final_response = ask_ai(
            [
                user_content,
                function_call_content,
                function_response_part
            ],
            tools=TOOL_DEFINITIONS
        )

        print("\nFINAL RESPONSE:")
        print(final_response.text)

        return final_response.text

    # --------------------------------
    # 9. No tool was required
    # --------------------------------

    return response.text
