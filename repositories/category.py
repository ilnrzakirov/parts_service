import sqlalchemy
from loguru import logger

from db.models import Category
from repositories.base import BaseRepository


class CategoryRepository(BaseRepository):

    async def get_all(self) -> list[Category]:
        logger.info("Запрос на выборку списка категорий")
        query = sqlalchemy.select(Category)
        return await self.session.execute(query)
