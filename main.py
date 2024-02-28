import os
from fastapi import FastAPI
from routes import score, whatsapp

app = FastAPI()
app.include_router(whatsapp.app, prefix="/api/whatsapp", tags=["whatsapp"])
app.include_router(score.app, prefix="/api/score", tags=["score"])
