from pydantic import BaseModel

from models.Category import CategoryPydantic
from models.Company import CompanyPydantic


class ProductPydantic(BaseModel):

    id: int
    category: CategoryPydantic
    balance: int
    company: CompanyPydantic
    name: str
    price: int
