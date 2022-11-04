from fastapi import APIRouter

from models.Users import UserIn

user_router = APIRouter()


@user_router.post("/create/")
async def create_user(user_in: UserIn):
    print(user_in)
