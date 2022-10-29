import sqlalchemy

from db import User
from models.Users import (
    UserIn,
    user,
)
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    """
        Репозиторий Юзера
    """

    async def get_all(self, limit: int = 10, skip: int = 0) -> list[user]:
        query = sqlalchemy.select(User).limit(limit).offset(skip)
        return await self.session.execute(query)

    async def get_by_id(self, id: int) -> user | None:
        query = sqlalchemy.select(User).where(User.id == id)
        user_db = await self.session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            return None
        return user.parse_obj(instance)

    async def create(self, user_in: UserIn) -> user:
        pass

    async def get_by_email(self, email: str) -> user | None:
        query = sqlalchemy.select(User).where(email == email)
        user_db = await self.session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            return None
        return user.parse_obj(instance)

    async def update(self, user_in: UserIn) -> user:
        pass
