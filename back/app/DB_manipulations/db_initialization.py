from .db import Pack
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime
# from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


def insert_to_db(session, pack_name, pack_description, pack_dl_url):
    '''
    Inserting package into DB
    '''
    print('we got here1')
    Pack_to_insert = Pack(
        name=pack_name, description=pack_description, download_link=pack_dl_url, like_count=0, download_count=0)
    print('we got here2')
    session.add(Pack_to_insert)
    session.commit()


def select_from_db(session, **kwargs):
    '''
    Selecting packages from DB depending on the requirements
    kwargs can be: package_name, like_count, download_count, page_number
    '''
    if len(kwargs) == 0:
        Packages = session.query(Pack)
        packages_to_return = {}

        for pack in Packages:
            packages_to_return[str(pack.id)] = {
                'name': str(pack.name),
                'description': str(pack.description),
                'download_link': str(pack.download_link),
                'like_count': str(pack.like_count),
                'download_count': str(pack.download_count), }
        return packages_to_return

    return {'Message': 'DB is empty'}


def delete_from_db(session, pack_name):
    '''
    Deleting packages into DB
    '''
    pass


def adjust_package_in_db(session, pack_name, new_like, new_download):
    '''
    Changes the information of specified package in DB
    Like updating the like count or download count
    Depending on the recived values
    '''
    pass
