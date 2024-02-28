from prisma import Prisma
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class NewUser(BaseModel):
    name: str
    phone: str


class UpdateUser(BaseModel):
    prompt: str = None
    response: str = None
    summary: str = None


async def get_user_by_phone(phone: str):
    db = Prisma()
    await db.connect()
    result = await db.user.find_unique(where={"phone": phone})
    await db.disconnect()
    return {"success": True, "data": result}


async def update_user(phone: str, update_data: UpdateUser):
    db = Prisma()
    await db.connect()
    result = await db.user.update(where={"phone": phone}, data=update_data)
    await db.disconnect()
    return {"success": True, "data": result}


async def create_user(data: NewUser):
    db = Prisma()
    await db.connect()
    result = await db.user.create(data=data)
    await db.disconnect()
    data = {"success": True, "data": result, "message": "New Chat Created"}
    return data
