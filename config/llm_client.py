import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm_client = OpenAI(
    base_url=os.getenv("QWEN_BASE_URL"),
    api_key=os.getenv("QWEN_API_KEY")
)