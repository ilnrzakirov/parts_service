import uvicorn
from fastapi import FastAPI
from loguru import logger

from settings import (
    UVICORN_HOST,
    UVICORN_PORT,
    async_engine,
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.on_event("startup")
async def startup():
    logger.info("Сервис зпущен")


@app.on_event("shutdown")
async def shutdown():
    logger.info("Сервис остановлен")
    await async_engine.dispose()


if __name__ == "__main__":
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=True)
