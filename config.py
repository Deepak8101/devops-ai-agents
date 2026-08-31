from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "gemini-3.5-flash-lite"
