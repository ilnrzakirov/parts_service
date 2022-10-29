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

    async def create(self, user_in: UserIn) -> user | None:
        if user_in is None:
            return None
        new_user = user(
            username=user_in.username,
            email=user_in.email,
            is_superuser=user_in.is_superuser,
            is_stuf=user_in.is_stuf,
            password=UserIn.password,
        )
        values = {**new_user.dict()}
        values.pop("id", None)
        query = sqlalchemy.insert(User).values(values)
        new_user.id = self.session.execute(query)
        return new_user

    async def get_by_email(self, email: str) -> user | None:
        query = sqlalchemy.select(User).where(email == email)
        user_db = await self.session.execute(query)
        instance = user_db.scalars().first()
        if instance is None:
            return None
        return user.parse_obj(instance)

    async def update(self, user_in: UserIn) -> user:
        pass
