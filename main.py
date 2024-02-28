import os
from fastapi import FastAPI
from routes import chat, score
from models import text_to_text
import whatsapp

app = FastAPI()
app.include_router(chat.app, prefix="/api/chat", tags=["chat"])
app.include_router(score.app, prefix="/api/score", tags=["score"])

