import sqlalchemy

from core.security import crypt_password
from db import User
from models.Users import (
    UserIn,
    user,
)
from repositories.base import BaseRepository
from settings import logger


class UserRepository(BaseRepository):
    """
        Репозиторий Юзера
    """

    async def get_all(self, limit: int = 10, skip: int = 0) -> list[user]:
        """
            Возвращяет список всех юзеров
        :param limit: int (Лимитировать длину списка)
        :param skip: int (Сколько юзеров пропустить)
        :return: list (список юзеров)
        """
        logger.info(f"Запрос на выборку списка юзеров лимит: {limit}, skip: {skip}")
        query = sqlalchemy.select(User).limit(limit).offset(skip)
        return await self.session.execute(query)

    async def get_by_id(self, id: int) -> user | None:
        """
            Берет из базы юзера по id и возвращяет
        :param id: int
        :return: user
        """
        logger.info(f"Запрос выдать юзера по id: {id}")
        query = sqlalchemy.select(User).where(User.id == id)
        user_db = await self.session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            logger.warning("Неуспешно, Юзер не найден")
            return None
        return user.parse_obj(instance)

    async def create(self, user_in: UserIn) -> user | None:
        """
            Создает изера с пайдантик модели
        :param user_in: UserIn (пайдантик модель юзера)
        :return: user
        """
        logger.info("Запрос на создания юзера")
        if user_in is None:
            logger.warning("Неуспешно, нечего создавать")
            return None
        new_user = user(
            username=user_in.username,
            email=user_in.email,
            is_superuser=user_in.is_superuser,
            is_stuf=user_in.is_stuf,
            password=crypt_password(UserIn.password),
        )
        values = {**new_user.dict()}
        values.pop("id", None)
        query = sqlalchemy.insert(User).values(values)
        new_user.id = self.session.execute(query)
        return new_user

    async def get_by_email(self, email: str) -> user | None:
        """
            Берет из базы юзера по email и возвращяет
        :param email: str
        :return: user
        """
        logger.info(f"Запрос на выдачу юзера по email: {email}")
        query = sqlalchemy.select(User).where(email == email)
        user_db = await self.session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            logger.warning("Неуспешно, юзер не найден")
            return None
        return user.parse_obj(instance)

    async def update(self, id: int, user_in: UserIn) -> user | None:
        """
            Обновляет юзера
        :param id: id юзера
        :param user_in: UserIn (пайдантик модель Юзера)
        :return: user
        """
        logger.info(f"Запрос на обновление юзера id: {id}")
        if user_in is None:
            return None
        new_user = user(
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
        self.session.execute(query)
        return new_user
