from passlib.hash import bcrypt
from sqlalchemy import (
    VARCHAR,
    Column,
    Integer,
)
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class User(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(VARCHAR(255), nullable=False)
    password = Column(VARCHAR(500), nullable=False)
    email = Column(VARCHAR(300), nullable=False)

    def __init__(self, username, password, email):
        self.username = username
        self.password = bcrypt.encrypt(password)
        self.email = email

    def password_is_valid(self, password):
        return bcrypt.verify(password, self.password)