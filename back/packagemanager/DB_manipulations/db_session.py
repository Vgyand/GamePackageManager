from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from packagemanager.etc.readyaml import read_config_yaml


def get_engine(user, passwd, db):
    """
    Connects to database
    """
    url = f'postgresql://{user}:{passwd}@db/{db}'
    pass
    if not database_exists(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine


def get_engine_from_yaml():
    """
    Calls 2 previous functions to return connected engine
    """
    parsed_yaml = read_config_yaml()

    return get_engine(parsed_yaml['pg_user'],
                      parsed_yaml['db_passwd'],
                      parsed_yaml['pg_name'],)


def get_session(engine):
    '''
    Makes session
    '''
    session = sessionmaker(bind=engine)()
    return session
