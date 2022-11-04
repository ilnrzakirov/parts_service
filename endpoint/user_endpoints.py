from fastapi import APIRouter

from models.Users import UserIn
from repositories.users import UserRepository

user_router = APIRouter()


@user_router.post("/create/")
async def create_user(user_in: UserIn):
    user = UserRepository()
    try:
        await user.create(user_in)
        return {"msg": "Ok"}
    except Exception as error:
        return {"msg": "Юзер уже существует"}
