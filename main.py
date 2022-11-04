import uvicorn
from fastapi import FastAPI
from loguru import logger

from endpoint.user_endpoints import user_router
from settings import (
    UVICORN_HOST,
    UVICORN_PORT,
    async_engine,
)

app = FastAPI()


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

app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=True)
