from db_abstract import DB_Manipulator
from .db import Pack, User
from sqlalchemy import BigInteger, Boolean, Column, \
    ForeignKey, Integer, String, Enum, Float, \
    UniqueConstraint, and_, func, Date, DateTime, desc


class PackageManipulator(DB_Manipulator):
    def __init__(self, passed_session):
        self.session = passed_session

    def select(self, dic):
        '''
        Selecting packages from DB depending on the requirements
        kwargs can be: package_name, like_count, download_count, page_number
        '''

        packages_to_return = []

        Packages = self.session.query(Pack)

        if dic['likes'] is not None:
            if dic['likes'] == 'inc':
                Packages = Packages.order_by(Pack.like_count)

            if dic['likes'] == 'dec':
                print('we got here')
                Packages = Packages.order_by(Pack.like_count.desc())

        elif dic['downloads'] is not None:
            if dic['downloads'] == 'inc':
                Packages = Packages.order_by(Pack.download_count)
            if dic['downloads'] == 'dec':
                Packages = Packages.order_by(Pack.download_count.desc())

        elif dic['size'] is not None:
            if dic['size'] == 'inc':
                Packages = Packages.order_by(Pack.package_size)
            if dic['size'] == 'dec':
                Packages = Packages.order_by(Pack.package_size.desc())

        if dic['search'] is not None:
            Packages = Packages.filter(
                Pack.name.like(f"%{str(dic['search'])}%"))

        if all(dic.values()) is None:
            Packages = Packages.order_by(Pack.id)

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

    def insert_to_db(self, pack_name, pack_description,
                     pack_dl_url, like, download, pack_size):
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
        self.session.add(Pack_to_insert)
        self.session.commit()
        return {'message': 'Done'}

    def delete(self):
        pass


class UserManipulator(DB_Manipulator):
    def __init__(self, passed_session):
        self.session = passed_session

    def select(self, dic):
        '''
        Selecting users from DB depending on the requirements
        kwargs can be: package_name, like_count, download_count, page_number
        '''

        users_to_return = []

        Users = self.session.query(Pack)

        if dic['likes'] is not None:
            if dic['likes'] == 'inc':
                Users = Users.order_by(Pack.like_count)

            if dic['likes'] == 'dec':
                print('we got here')
                Users = Users.order_by(Pack.like_count.desc())

        elif dic['downloads'] is not None:
            if dic['downloads'] == 'inc':
                Users = Users.order_by(Pack.download_count)
            if dic['downloads'] == 'dec':
                Users = Users.order_by(Pack.download_count.desc())

        elif dic['size'] is not None:
            if dic['size'] == 'inc':
                Users = Users.order_by(Pack.package_size)
            if dic['size'] == 'dec':
                Users = Users.order_by(Pack.package_size.desc())

        if dic['search'] is not None:
            Users = Users.filter(
                Pack.name.like(f"%{str(dic['search'])}%"))

        if all(dic.values()) is None:
            Users = Users.order_by(Pack.id)

        for pack in Users:
            pack_to_add = {}
            pack_to_add['id'] = str(pack.id)
            pack_to_add['uuid_id'] = str(pack.uuid_id)
            pack_to_add['name'] = str(pack.name)
            pack_to_add['description'] = str(pack.description)
            pack_to_add['download_link'] = str(pack.download_link)
            pack_to_add['like_count'] = str(pack.like_count)
            pack_to_add['download_count'] = str(pack.download_count)
            pack_to_add['package_size'] = str(pack.package_size)
            users_to_return.append(pack_to_add)

        return users_to_return

    def insert(self):
        pass

    def delete(self):
        pass
