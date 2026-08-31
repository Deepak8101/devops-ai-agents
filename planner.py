from ai_client import ask_ai


def choose_command(user_question):

    prompt = f"""
You are a Senior Linux Administrator.

The user asked:

{user_question}

Choose the SINGLE best Linux command to answer the question.

Rules:
- Return ONLY the command.
- No explanation.
- No markdown.

Examples:

Question:
What is my hostname?

Command:
hostname

Question:
How much memory is available?

Command:
free -m

Question:
How much disk space is available?

Command:
df -h
"""

    command = ask_ai(prompt)

    return command.strip()
