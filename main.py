import uvicorn
from loguru import logger
from starlette.requests import Request

from models.Users import UserIn
from repositories.users import UserRepository
from fastapi.encoders import jsonable_encoder
from settings import (
    UVICORN_HOST,
    UVICORN_PORT,
    async_engine, app,
)


@app.get("/create/{name}")
async def root(name: str, request: Request):
    user = UserRepository()
    new = UserIn(
        username=f"{name}",
        password="123456789",
        password2="123456789",
        email="1234@123.com",
        is_superuser=True,
        is_stuf=True
    )
    # res = await user.create(new)
    res = await user.get_by_id(15)
    # new_user = jsonable_encoder(res)
    # print(new_user)
    return {"message": "Hello", "instance": res}


@app.on_event("startup")
async def startup():
    """
        Корутина запускается при пуске сервиса
    """
    logger.info("Сервис зпущен")


@app.on_event("shutdown")
async def shutdown():
    """
        Корутина запускается при остановке сервиса
    """
    logger.info("Сервис остановлен")
    await async_engine.dispose()


if __name__ == "__main__":
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=True)
