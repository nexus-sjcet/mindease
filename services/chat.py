from prisma import Prisma
from fastapi.responses import JSONResponse


def get_user(phone: str = None):
    db = Prisma()
    await db.connect()
    result = await db.chat.find_unique(where={"phone": phone})
    await db.disconnect()
    return {"success": True, "data": result}


async def create_user():
    db = Prisma()
    await db.connect()
    result = await db.chat.create(data={})
    await db.disconnect()
    data = {"success": True, "data": result, "message": "New Chat Created"}
    return data
