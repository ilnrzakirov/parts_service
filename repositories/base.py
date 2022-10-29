from sqlalchemy.orm import sessionmaker

from settings import session_maker


class BaseRepository:
    """
        Репозиторий для обращения к БД
    """
    def __init__(self, session: sessionmaker = session_maker):
        self.session = session()
