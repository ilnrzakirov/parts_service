from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    async def get_all(self, limit: int = 10, skip: int = 0):
        pass

    async def get_by_id(self, id: int):
        pass

    async def create(self):
        pass

    async def get_by_email(self, email: str):
        pass

    async def update(self):
        pass
