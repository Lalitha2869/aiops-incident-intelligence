from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
# print("API KEY FOUND:", os.getenv("OPENAI_API_KEY"))

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_llm():
    return client