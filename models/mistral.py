from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]


def text_to_text(message):

    client = OpenAI(
        api_key=TOGETHER_API_KEY,
        base_url="https://api.together.xyz",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are an AI assistant",
            },
            {
                "role": "user",
                "content": message,
            },
        ],
        model="mistralai/Mistral-7B-Instruct-v0.1",
        max_tokens=1024,
    )
    return chat_completion.choices[0].message.content
