import os
from fastapi import FastAPI
from routes import chat
from models import text_to_text
import whatsapp

app = FastAPI()
app.include_router(chat.app, prefix="/api/chat", tags=["chat"])

