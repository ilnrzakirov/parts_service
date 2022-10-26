from sqlalchemy.orm import sessionmaker

from settings import session_maker


class BaseRepository:
    def __init__(self, session_maker: sessionmaker = session_maker):
        self.session = session_maker()
