from .db_session import get_session, get_engine_from_yaml
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


engine = get_engine_from_yaml()
session = get_session(engine)

base = declarative_base()

base.metadata.create_all(engine)


class Pack(base):
    __tablename__ = 'Package'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    download_link = Column(String)
    like_count = Column(Integer)
    download_count = Column(Integer)


def insert_to_db(pack_name, pack_description, pack_dl_url):
    '''
    Inserting package into DB
    '''
    Pack_to_insert = Pack(
        name=pack_name, description=pack_description, download_link=pack_dl_url)
    session.add(Pack_to_insert)
    session.commit()


def select_from_db(**kwargs):
    '''
    Selecting packages from DB depending on the requirements
    kwargs can be: package_name, like_count, download_count, page_number
    '''
    if len(kwargs) == 0:
        Packages = session.query(Pack)
        packages_to_return = {}

        for pack in Packages:
            packages_to_return[str(pack.id)] = [
                {'name': str(pack.name)},
                {'description': str(pack.description)},
                {'download_link': str(pack.download_link)},
                {'like_count': str(pack.like_count)},
                {'download_count': str(pack.download_count)}, ]
        return packages_to_return
    return {'Message': 'DB is empty'}


def delete_from_db(pack_name):
    '''
    Deleting packages into DB
    '''
    pass


def adjust_package_in_db(pack_name, new_like, new_download):
    '''
    Changes the information of specified package in DB
    Like updating the like count or download count
    Depending on the recived values
    '''
    pass
