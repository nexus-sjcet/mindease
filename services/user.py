from prisma import Prisma
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class NewUser(BaseModel):
    name: str
    phone: str


async def get_user_by_phone(phone: str = None):
    db = Prisma()
    await db.connect()
    result = await db.user.find_unique(where={"phone": phone})
    await db.disconnect()
    return {"success": True, "data": result}


async def create_user(data: NewUser):
    db = Prisma()
    await db.connect()
    result = await db.user.create(data=data)
    await db.disconnect()
    data = {"success": True, "data": result, "message": "New Chat Created"}
    return data
