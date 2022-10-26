from pydantic import (
    BaseModel,
    EmailStr,
    constr,
    validator,
)


class User(BaseModel):
    id: int | None
    username: str
    password: str
    email: EmailStr
    is_superuser: bool = False
    is_stuf: bool = False


class UserIn(BaseModel):
    username: str
    password: constr(min_length=8)
    password2: str
    email: EmailStr
    is_superuser: bool = False
    is_stuf: bool = False

    @validator("password2")
    def is_valid(cls, v, values, **kwargs):
        if "password" in values and v != values["password"]:
            raise ValueError("Не верно введен пароль")
        return v
