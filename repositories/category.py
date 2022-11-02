import sqlalchemy
from loguru import logger

from db.models import Category
from models.Category import CategoryPydantic
from repositories.base import BaseRepository


class CategoryRepository(BaseRepository):

    async def get_all(self) -> list[CategoryPydantic]:
        logger.info("Запрос на выборку списка категорий")
        query = sqlalchemy.select(Category)
        cat_list = await self.session.execute(query)
        result = []
        for category in cat_list:
            result.append(CategoryPydantic.parse_obj(category[0]))
        return result

    async def get_by_name(self, name: str) -> CategoryPydantic | None:
        logger.info("Запрос на выдачу категории по имени")
        query = sqlalchemy.select(Category).where(Category.name == name)
        category_db = self.session.execute(query)
        instance = category_db.scalars().first()
        if instance is None:
            logger.warning("Неуспешно, Категория не найдена")
            return None
        return CategoryPydantic.parse_obj(instance)

    async def create(self, category_in: CategoryPydantic) -> CategoryPydantic | None:
        logger.info("Запрос на создание категории")
        if category_in is None:
            logger.warning("Неуспешно, нечего создавать")
            return None
        values = {**category_in.dict()}
        values.pop("id", None)
        query = sqlalchemy.insert(Category).values(values)
        category_in.id = await self.session.execute(query)
        return category_in
