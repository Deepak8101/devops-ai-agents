from google import genai

from config import API_KEY
from config import MODEL


client = genai.Client(
    api_key=API_KEY
)


def ask_ai(prompt):

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )

    return response.text
