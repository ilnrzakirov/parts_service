from fastapi import APIRouter
from loguru import logger

from models.Users import UserIn
from repositories.users import UserRepository

user_router = APIRouter()


@user_router.post("/create/")
async def create_user(user_in: UserIn):
    """
        Эндпоинт для создания юзера
    :param user_in: Pydantic модель
    :return: msg со статусом
    """
    user = UserRepository()
    try:
        user_in.is_valid()
        await user.create(user_in)
        return {"msg": "Ok"}
    except ValueError:
        logger.warning("Не верно ввден пароль")
        return {"msg": "Не совпадают пароли"}
    except Exception as error:
        logger.warning(error)
        return {"msg": "Юзер уже существует"}


@user_router.post("/update/")
async def update_user(user_in: UserIn):
    """
        Эндпоинт для обновления юзера
    :param user_in: Pydsntic user in
    :return: msg json
    """
    user = UserRepository()
    try:
        instance = await user.get_by_email(user_in.email)
        await user.update(instance.id, user_in)
        return {"msg": "Ok"}
    except Exception as error:
        logger.warning(error)
        return {"msg": error}
