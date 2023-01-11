from .db_session import get_engine_from_yaml, get_session
from sqlalchemy import Column, Integer, String, Float, Boolean, UniqueConstraint, Identity
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

ENGINE = get_engine_from_yaml()
BASE = declarative_base()


class Pack(BASE):
    __tablename__ = 'Package'

    id = Column(Integer, Identity(start=1, cycle=True),
                nullable=False, unique=True)
    uuid_id = Column(UUID(as_uuid=True), primary_key=True,
                     default=uuid.uuid4, nullable=False, unique=True)
    name = Column(String)
    description = Column(String)
    download_link = Column(String)
    like_count = Column(Integer)
    download_count = Column(Integer)
    package_size = Column(Float)


class User(BASE):
    __tablename__ = 'User'

    id = Column(Integer, Identity(start=1, cycle=True),
                nullable=False, unique=True)

    uuid_id = Column(UUID(as_uuid=True), primary_key=True,
                     default=uuid.uuid4, nullable=False, unique=True)
    username = Column(String, nullable=False)
    hashedpassword = Column(String)
    disabled = Column(Boolean, nullable=False, default=False)


def db_init():

    BASE.metadata.create_all(ENGINE)

    print('probably the db is done')


def session_init():
    engine = get_engine_from_yaml()
    session = get_session(engine)
    print('probably the session is done')
    return session
