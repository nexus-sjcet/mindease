from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from services import score

app = APIRouter()


class NewScores(BaseModel):
    extroversion: float
    agreeableness: float
    conscientiousness: float
    neuroticism: float
    openness: float
    userPhone: str


@app.get("/")
async def get_score(phone: str):
    try:
        return await score.get_score_by_phone(phone, False)
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )


@app.get("/latest")
async def get_score(phone: str):
    try:
        return await score.get_score_by_phone(phone, True)
    except Exception as e:
        print(e)
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )


@app.post("/")
async def create_score(scores: NewScores):
    try:
        return await score.add_new_score(scores)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
