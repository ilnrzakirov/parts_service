from pydantic import BaseModel


class CompanyPydantic(BaseModel):
    """
        Падантик модель компаний
    """
    id: int
    name: str
