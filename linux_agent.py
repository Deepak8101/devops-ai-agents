from linux_tools import collect_system_info
from prompt_builder import build_prompt
from ai_client import ask_ai


def analyze_linux():

    system_info = collect_system_info()

    prompt = build_prompt(system_info)

    answer = ask_ai(prompt)

    return answer
