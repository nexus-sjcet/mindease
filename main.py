import os
from fastapi import FastAPI
from routes import chat, score
from models import text_to_text
import whatsapp
import graph

app = FastAPI()
app.include_router(chat.app, prefix="/api/chat", tags=["chat"])
app.include_router(score.app, prefix="/api/score", tags=["score"])


graph.generate_graph(3,5,2,0.4,4)
