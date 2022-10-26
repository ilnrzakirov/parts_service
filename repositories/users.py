from models.Users import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 10, skip: int = 0) -> list[User]:
        pass

    async def get_by_id(self, id: int) -> User:
        pass

    async def create(self) -> User:
        pass

    async def get_by_email(self, email: str) -> User:
        pass

    async def update(self) -> User:
        pass
