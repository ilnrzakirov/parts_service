from fastapi import APIRouter
from loguru import logger
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
        logger.warning(error)
        return {"msg": "Юзер уже существует"}


@user_router.post("/update/")
async def update_user(user_in: UserIn):
    user = UserRepository()
    try:
        instance = await user.get_by_email(user_in.email)
        await user.update(instance.id, user_in)
        return {"msg": "Ok"}
    except Exception as error:
        logger.warning(error)
        return {"msg": error}
