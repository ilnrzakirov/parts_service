from aioredis import Redis
from decouple import config
from loguru import logger
from sqlalchemy.engine import URL

from db.engine import (
    asinc_engine,
    get_session_maker,
)

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

async_engine = asinc_engine(postgres_url)
session_maker = get_session_maker(async_engine)  # noqa f841

redis = Redis()

logger = logger.add("log.log", format="{time}, {level}, {message}", level="INFO", encoding="UTF-8")
