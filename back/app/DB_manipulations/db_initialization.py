from .db import Pack
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime, desc
# from sqlalchemy.orm import relationship


def insert_to_db(session, pack_name, pack_description, pack_dl_url, like, download, pack_size):
    '''
    Inserting package into DB
    '''
    Pack_to_insert = Pack(
        name=pack_name,
        description=pack_description,
        download_link=pack_dl_url,
        like_count=like,
        download_count=download,
        package_size=pack_size,)
    session.add(Pack_to_insert)
    session.commit()
    return {'message': 'Done'}


def select_from_db(session, **kwargs):
    '''
    Selecting packages from DB depending on the requirements
    kwargs can be: package_name, like_count, download_count, page_number
    '''

    packages_to_return = []

    if len(kwargs) == 0:
        Packages = session.query(Pack).order_by(Pack.id).all()

    keys = kwargs.keys()
    if 'lik' in keys:
        if kwargs['lik'] == 'inc':
            Packages = session.query(
                Pack).order_by(Pack.like_count).all()

        if kwargs['lik'] == 'dec':
            Packages = session.query(
                Pack).order_by(Pack.like_count.desc()).all()

    if 'down' in keys:
        if kwargs['down'] == 'inc':
            Packages = session.query(
                Pack).order_by(Pack.download_count).all()
        if kwargs['down'] == 'dec':
            Packages = session.query(
                Pack).order_by(Pack.download_count.desc()).all()

    if 'siz' in keys:
        if kwargs['siz'] == 'inc':
            Packages = session.query(
                Pack).order_by(Pack.package_size).all()
        if kwargs['siz'] == 'dec':
            Packages = session.query(
                Pack).order_by(Pack.package_size.desc()).all()

    if 'sea' in keys:
        Packages = session.query(
            Pack).filter(Pack.name == kwargs['sea']).all()

    for pack in Packages:
        pack_to_add = {}
        pack_to_add['id'] = str(pack.id)
        pack_to_add['uuid_id'] = str(pack.uuid_id)
        pack_to_add['name'] = str(pack.name)
        pack_to_add['description'] = str(pack.description)
        pack_to_add['download_link'] = str(pack.download_link)
        pack_to_add['like_count'] = str(pack.like_count)
        pack_to_add['download_count'] = str(pack.download_count)
        pack_to_add['package_size'] = str(pack.package_size)
        packages_to_return.append(pack_to_add)

    return packages_to_return


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
    Packages = session.query(Pack).filter(Pack.id == pack_id).all()
    if Packages:
        for pack in Packages:

            pack.like_count += 1
            session.commit()
        return {'message': 'Done'}
    return {'message': 'Wrong Id'}


def add_download_to_package(session, pack_id):
    '''
    Adds download to package specified by id
    '''
    Packages = session.query(Pack).filter(Pack.id == pack_id).all()
    if Packages:
        for pack in Packages:
            pack.download_count += 1
            session.commit()
        return {'message': 'Done'}
    return {'message': 'Wrong Id'}
