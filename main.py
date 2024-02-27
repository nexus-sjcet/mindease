from models import text_to_text
import os
from dotenv import load_dotenv
import whatsapp

load_dotenv()
TOGETHER_API_KEY = os.environ["TOGETHER_API_KEY"]

if __name__ == "__main__":
    text_data = text_to_text.text_to_text(
        "Tell me about San Francisco", TOGETHER_API_KEY
    )
    print(text_data)
    whatsapp.sendMessage(text_data, "+918921964884")
