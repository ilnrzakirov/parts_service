from decouple import config

UVICORN_PORT = int(config("UVICORN_PORT"))
UVICORN_HOST = config("UVICORN_HOST")

