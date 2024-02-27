from typing import Optional
from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services import user

app = APIRouter()


@app.post("/message")
async def new_message():
    try:
        # check db for user existing with the phone number (From)
        phone = "+1234567890"
        user_response = await user.get_user_service(phone)
        if user_response["data"] == None:
            await user.create_user_service({"name": "Sample Name", "phone": phone})
        # give the data for LLM analysis:
        # if type image => image-to-text then text-analyze
        # if type text => text-analyze
        return {"success": True, "message": "Message Recieved"}
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
