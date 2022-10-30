from pydantic import BaseModel


class company(BaseModel):
    id: int
    name: str
