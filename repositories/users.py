import sqlalchemy
from loguru import logger

from core.security import crypt_password
from db import User
from models.Users import (
    UserIn,
    UserPydantic,
)
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    """
        Репозиторий Юзера
    """

    async def get_all(self, limit: int = 10, skip: int = 0) -> list[UserPydantic]:
        """
            Возвращяет список всех юзеров
        :param limit: int (Лимитировать длину списка)
        :param skip: int (Сколько юзеров пропустить)
        :return: list (список юзеров)
        """
        session = self.session()
        logger.info(f"Запрос на выборку списка юзеров лимит: {limit}, skip: {skip}")
        query = sqlalchemy.select(User).limit(limit).offset(skip)
        result = await session.execute(query)
        result_list = []
        for item in result:
            result_list.append(UserPydantic.parse_obj(item[0].__dict__))
        return result_list

    async def get_by_id(self, id: int) -> UserPydantic | None:
        """
            Берет из базы юзера по id и возвращяет
        :param id: int
        :return: user
        """
        session = self.session()
        logger.info(f"Запрос выдать юзера по id: {id}")
        query = sqlalchemy.select(User).where(User.id == id)
        user_db = await session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            logger.warning("Неуспешно, Юзер не найден")
            return None
        return UserPydantic.parse_obj(instance.__dict__)

    async def create(self, user_in: UserIn) -> UserPydantic | None:
        """
            Создает изера с пайдантик модели
        :param user_in: UserIn (пайдантик модель юзера)
        :return: user
        """
        session = self.session()
        logger.info("Запрос на создания юзера")
        if user_in is None:
            logger.warning("Неуспешно, нечего создавать")
            return None
        new_user = UserPydantic(
            username=user_in.username,
            email=user_in.email,
            is_superuser=user_in.is_superuser,
            is_stuf=user_in.is_stuf,
            password=crypt_password(user_in.password),
        )
        values = {**new_user.dict()}
        values.pop("id", None)
        query = sqlalchemy.insert(User).values(values)
        new_user.id = await session.execute(query)
        await session.commit()
        return new_user

    async def get_by_email(self, email: str) -> UserPydantic | None:
        """
            Берет из базы юзера по email и возвращяет
        :param email: str
        :return: user
        """
        session = self.session()
        logger.info(f"Запрос на выдачу юзера по email: {email}")
        query = sqlalchemy.select(User).where(User.email == email)
        user_db = await session.execute(query)
        instance = user_db.scalars().first()
        print(instance)
        if instance is None:
            logger.warning("Неуспешно, юзер не найден")
            return None
        return UserPydantic.parse_obj(instance.__dict__)

    async def update(self, id: int, user_in: UserIn) -> UserPydantic | None:
        """
            Обновляет юзера
        :param id: id юзера
        :param user_in: UserIn (пайдантик модель Юзера)
        :return: user
        """
        session = self.session()
        logger.info(f"Запрос на обновление юзера по id: {id}")
        if user_in is None:
            return None
        new_user = UserPydantic(
            id=id,
            username=user_in.username,
            email=user_in.email,
            is_superuser=user_in.is_superuser,
            is_stuf=user_in.is_stuf,
            password=crypt_password(UserIn.password),
        )
        values = {**new_user.dict()}
        values.pop("id", None)
        query = sqlalchemy.update(User).where(User.id == id).values(values)
        session.execute(query)
        return new_user
