from typing import Optional
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services import user
import whatsapp

app = APIRouter()


@app.post("/message")
async def new_message(request: Request):
    try:
        req = await request.form()

        numMedia = req.get("NumMedia")
        mediaUrl = ""
        body = ""
        if int(numMedia) > 0:
            mediaUrl = req.get("MediaUrl0")
        else:
            body = ""
        phone = req.get("From").split(":")[1]
        name = req.get("ProfileName")

        # check db for user existing with the phone number (From)
        user_response = await user.get_user_by_phone(phone)
        if user_response["data"] == None:
            await user.create_user({"name": name, "phone": phone})

        # give the data for LLM analysis:
        # if type image => image-to-text then text-analyze
        # if type text => text-analyze

        return Response(
            content=str(whatsapp.generateResponse("This is a response")),
            media_type="application/xml",
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
