from .db_session import get_engine_from_yaml

from sqlalchemy.ext.declarative import declarative_base


def db_init():
    engine = get_engine_from_yaml()
    base = declarative_base()
    base.metadata.create_all(engine)
    print('probably it is done')
