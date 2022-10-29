import uvicorn
from fastapi import FastAPI
from loguru import logger

from repositories.users import UserRepository
from settings import (
    UVICORN_HOST,
    UVICORN_PORT,
    async_engine,
)

app = FastAPI()


@app.get("/")
async def root():
    user = UserRepository()
    res = await user.get_by_id(1)
    print(res)
    return {"message": "Hello"}


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
