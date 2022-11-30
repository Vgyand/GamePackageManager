from .db_session import get_engine_from_yaml, get_session
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

ENGINE = get_engine_from_yaml()
BASE = declarative_base()


class Pack(BASE):
    __tablename__ = 'Package'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    download_link = Column(String)
    like_count = Column(Integer)
    download_count = Column(Integer)


def db_init():

    BASE.metadata.create_all(ENGINE)

    print('probably the db is done')


def session_init():
    engine = get_engine_from_yaml()
    session = get_session(engine)
    print('probably the session is done')
    return session
