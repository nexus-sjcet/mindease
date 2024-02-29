import os
from typing import Optional
from fastapi import APIRouter, Form, Request, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services import user, whatsapp, supastore, graph, score
from actions import ocean, message

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
            body = llava(mediaUrl)
        else:
            body = req.get("Body")
        phone = req.get("From").split(":")[1]
        name = req.get("ProfileName")

        # check db for user existing with the phone number (From)
        user_response = await user.get_user_by_phone(phone)
        if user_response["data"] == None:
            await user.create_user({"name": name, "phone": phone})

        if body == "/stats":
            res = await score.get_score_by_phone(phone, True)
            filename = graph.generate_graph(
                res["data"].extroversion,
                res["data"].agreeableness,
                res["data"].conscientiousness,
                res["data"].neuroticism,
                res["data"].openness,
            )
            image_url = supastore.upload(filename)
            # os.remove(f"/images/{filename}.png")
            return Response(
                content=str(
                    whatsapp.generateImageResponse(
                        "Have a look at your stats", image_url
                    )
                ),
                media_type="application/xml",
            )
        # give the data for LLM analysis:
        ocean_scores = ocean.generate_ocean_score(body)
        if (
            "scores" in ocean_scores.keys()
            and [
                "extroversion",
                "agreeableness",
                "conscientiousness",
                "neuroticism",
                "openness",
            ]
            in ocean_scores["scores"].keys()
        ):
            res = await score.add_new_score(
                {**ocean_scores["scores"], "userPhone": phone}
            )
        # if type image => image-to-text then text-analyze
        # if type text => text-analyze
        response = message.generate_message(body)

        return Response(
            content=str(whatsapp.generateResponse(response)),
            media_type="application/xml",
        )
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
