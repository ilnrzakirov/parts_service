from pydantic import BaseModel


class CompanyPydantic(BaseModel):
    """
        Пайдантик модель компаний
    """
    id: int
    name: str
