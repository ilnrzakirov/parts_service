from pydantic import BaseModel


class CategoryPydantic(BaseModel):
    """
        Пайдантик модель категорий
    """

    id: int
    name: str
