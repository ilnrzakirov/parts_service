import sqlalchemy

from db import User
from models.Users import (
    UserIn,
    user,
)
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 10, skip: int = 0) -> list[user]:
        query = sqlalchemy.select(User).limit(limit).offset(skip)
        return await self.session.execute(query)

    async def get_by_id(self, id: int) -> user:
        pass

    async def create(self, user: UserIn) -> user:
        pass

    async def get_by_email(self, email: str) -> user:
        pass

    async def update(self, user: UserIn) -> user:
        pass
