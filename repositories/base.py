from sqlalchemy.orm import sessionmaker


class BaseRepository:
    def __init__(self, session_maker: sessionmaker):
        self.session = session_maker()
