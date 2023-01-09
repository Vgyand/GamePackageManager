from .db_abstract import DB_Manipulator
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

    def insert(self, pack_name, pack_description,
               pack_dl_url, like, download, pack_size):
        '''
        Inserts package into DB
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

    def delete(self, pack_id):
        '''
        Deletes package from the DB
        '''
        Packages = self.session.query(Pack)
        for pack in Packages:
            if str(pack.id) == pack_id:
                self.session.delete(pack)
                self.session.commit()
                return {'message': 'Done'}
        return {'message': 'The package not found'}

    def add_like_to_package(self, pack_id):
        '''
        Adds like to package specified by id
        '''
        Packages = self.session.query(Pack).filter(Pack.id == pack_id).all()
        if Packages:
            for pack in Packages:

                pack.like_count += 1
                self.session.commit()
            return {'message': 'Done'}
        return {'message': 'Wrong Id'}

    def add_download_to_package(self, pack_id):
        '''
        Adds download to package specified by id
        '''
        Packages = self.session.query(Pack).filter(Pack.id == pack_id).all()
        if Packages:
            for pack in Packages:
                pack.download_count += 1
                self.session.commit()
            return {'message': 'Done'}
        return {'message': 'Wrong Id'}

    def update_values_of_package(self, values_to_update):
        '''
        Receives values, id, values_to_update
        Updates them in DB.
        '''
        Packages = self.session.query(Pack).filter(
            Pack.id == values_to_update.id).all()
        if Packages:
            for pack in Packages:
                if values_to_update.name is not None:
                    pack.name = values_to_update.name

                if values_to_update.description is not None:
                    pack.description = values_to_update.description

                if values_to_update.download_link is not None:
                    pack.download_link = values_to_update.download_link

                if values_to_update.size is not None:
                    pack.package_size = values_to_update.size

                self.session.commit()
            return {'message': 'Done'}
        return {'message': 'Wrong Id'}


class UserManipulator(DB_Manipulator):
    def __init__(self, passed_session):
        self.session = passed_session

    def select(self):
        '''
        Selecting users from DB
        '''

        users_to_return = []

        Users = self.session.query(User)

        Users = Users.order_by(User.id)

        for user in Users:
            user_to_add = {}
            user_to_add['id'] = str(user.id)
            user_to_add['uuid_id'] = str(user.uuid_id)
            user_to_add['username'] = str(user.username)
            user_to_add['hashedpassword'] = str(user.hashedpassword)
            users_to_return.append(user_to_add)

        return users_to_return

    def insert(self, uusername, hhashedpassword):
        '''Inserts user into DB'''
        User_to_insert = User(
            username=uusername,
            hashedpassword=hhashedpassword,)
        self.session.add(User_to_insert)
        self.session.commit()
        return {'message': 'Done'}

    def delete(self, user_id):
        '''
        Deletes user from the DB
        '''
        Users = self.session.query(User)
        for user in Users:
            if str(user.id) == user_id:
                self.session.delete(user)
                self.session.commit()
                return {'message': 'Done'}
        return {'message': 'The package not found'}
