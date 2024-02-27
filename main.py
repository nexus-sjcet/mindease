import os
from fastapi import FastAPI
from routes import chat
from models import text_to_text
import whatsapp

app = FastAPI()
app.include_router(chat.app, prefix="/api/chat", tags=["chat"])

if __name__ == "__main__":
    text_data = text_to_text.text_to_text("Tell me about San Francisco")
    print(text_data)
    whatsapp.sendMessage(text_data, "+918921964884")
