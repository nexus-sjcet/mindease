from typing import Optional
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = APIRouter()


class NewMessage(BaseModel):
    Body: Optional[str] = None
    MediaUrl0: Optional[str] = None
    ProfileName: str
    From: str


@app.post("/message")
async def new_message(data: NewMessage):
    try:
        # check db for user existing with the phone number (From)
        # if not exist create new user
        # give the data for LLM analysis:
        # if type image => image-to-text then text-analyze
        # if type text => text-analyze
        print(data)
        return {"success": True, "message": "Message Recieved"}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
