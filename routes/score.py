from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = APIRouter()


@app.get("/")
async def get_score(phone: str = None):
    try:
        # return await get_score_service(id)
        print(id)
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"success": False, "message": "Something Went Wrong!"},
        )
