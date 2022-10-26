from pydantic import (
    BaseModel,
    EmailStr,
    validator,
)


class User(BaseModel):
    id: int | None
    username: str
    password: str
    email: EmailStr
    is_superuser: bool
    is_stuf: bool


class UserIn(BaseModel):
    username: str
    password: str
    password2: str
    email: EmailStr

    @validator("password2")
    def is_valid(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Не верно введен пароль")
        return v
