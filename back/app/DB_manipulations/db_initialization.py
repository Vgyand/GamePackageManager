from .db import Pack
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime
# from sqlalchemy.orm import relationship


def insert_to_db(session, pack_name, pack_description, pack_dl_url):
    '''
    Inserting package into DB
    '''
    Pack_to_insert = Pack(
        name=pack_name, description=pack_description,
        download_link=pack_dl_url, like_count=0, download_count=0)
    session.add(Pack_to_insert)
    session.commit()
    return {'message': 'Done'}


def select_from_db(session, **kwargs):
    '''
    Selecting packages from DB depending on the requirements
    kwargs can be: package_name, like_count, download_count, page_number
    '''
    if len(kwargs) == 0:
        Packages = session.query(Pack)
        packages_to_return = []

        for pack in Packages:
            pack_to_add = {}
            pack_to_add['id'] = str(pack.id)
            pack_to_add['name'] = str(pack.name)
            pack_to_add['description'] = str(pack.description)
            pack_to_add['download_link'] = str(pack.download_link)
            pack_to_add['like_count'] = str(pack.like_count)
            pack_to_add['download_count'] = str(pack.download_count)
            print(pack_to_add)
            packages_to_return.append(pack_to_add)
        return packages_to_return

    return {'Message': 'DB is empty'}


def delete_from_db(session, pack_id):
    '''
    Deleting packages from the DB
    '''
    Packages = session.query(Pack)
    for pack in Packages:
        if pack.id == pack_id:
            session.delete(pack)
            session.commit()
            return {'message': 'Done'}
    return {'message': 'The package not found'}


def add_like_to_package(session, pack_id):
    '''
    Adds like to package specified by id
    '''
    pass


def add_download_to_package(session, pack_id):
    '''
    Adds download to package specified by id
    '''
    pass
