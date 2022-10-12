run:
	uvicorn main:app --reload

makemigrations:
	alembic revision --m="$(NAME)" --autogenerate

migrate:
	alembic upgrade head