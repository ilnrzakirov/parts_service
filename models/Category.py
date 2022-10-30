from pydantic import BaseModel


class CategoryPydantic(BaseModel):

    id: int
    name: str
