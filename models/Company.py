from pydantic import BaseModel


class CompanyPydantic(BaseModel):
    id: int
    name: str
