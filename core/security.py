from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def crypt_password(password: str) -> str:
    return context.hash(password)


def verify_password(password: str, hash: str) -> bool:
    return context.verify(secret=password, hash=hash)
