import uvicorn
from fastapi import FastAPI

from settings import (
    UVICORN_HOST,
    UVICORN_PORT,
    logger,
)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


@app.on_event("startup")
async def startup():
    logger.info("Сервис зпущен")


if __name__ == "__main__":
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=True)
