from prisma import Prisma
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class NewScores(BaseModel):
    extroversion: float
    agreeableness: float
    conscientiousness: float
    neuroticism: float
    openness: float
    userPhone: str


async def get_score_by_phone(phone: str, latest: bool):
    db = Prisma()
    await db.connect()
    result = await db.score.find_many(where={"userPhone": phone})
    await db.disconnect()
    if latest:
        return {"success": True, "data": result[-1]}
    return {"success": True, "data": result}


async def add_new_score(scores: NewScores):
    db = Prisma()
    await db.connect()
    result = await db.score.create(
        {
            "extroversion": scores["extroversion"],
            "agreeableness": scores["agreeableness"],
            "conscientiousness": scores["conscientiousness"],
            "neuroticism": scores["neuroticism"],
            "openness": scores["openness"],
            "user": {"connect": {"phone": scores["userPhone"]}},
        }
    )
    await db.disconnect()
    return {"success": True, "data": result}
