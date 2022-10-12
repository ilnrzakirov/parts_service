from decouple import config
from sqlalchemy.engine import URL

UVICORN_PORT = int(config("UVICORN_PORT"))
UVICORN_HOST = config("UVICORN_HOST")

DB_USER = config("DB_USER")
DB_PASS = config("DB_PASS")
DB_PORT = int(config("DB_PORT"))
DB_NAME = config("DB_NAME")
DB_HOST = config("DB_HOST")

postgres_url = URL.create(
    "postgresql+asyncpg",
    username=DB_USER,
    password=DB_PASS,
    port=DB_PORT,
    database=DB_NAME,
    host=DB_HOST,
)
