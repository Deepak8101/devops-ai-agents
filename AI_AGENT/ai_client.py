import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def ask_ai(contents, tools=None):
    config = types.GenerateContentConfig(
        tools=tools
    )

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=contents,
        config=config
    )

    return response
