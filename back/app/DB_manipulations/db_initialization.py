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


def delete_from_db(session, pack_id):
    '''
    Deleting packages from the DB
    '''
    Packages = session.query(Pack)
    obj_to_remove = Pack()

    for pack in Packages:
        if pack.id == pack_id:
            obj_to_remove.id = pack.id
            obj_to_remove.name = pack.name
            obj_to_remove.description = pack.description
            obj_to_remove.download_link = pack.download_link
            obj_to_remove.like_count = pack.like_count
            obj_to_remove.download_count = pack.download_count
            session.delete(obj_to_remove)
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
