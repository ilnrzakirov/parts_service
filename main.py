import uvicorn
from fastapi import FastAPI

from settings import UVICORN_PORT, UVICORN_HOST

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=UVICORN_PORT, host=UVICORN_HOST, reload=True)