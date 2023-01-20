from fastapi import APIRouter
from socnet.models import resp_models

from socnet.DB_manipulations.db import session_init
from socnet.DB_manipulations.db_methods2 import PackageManipulator, UserManipulator

from socnet.etc.randomstring import get_random_string
import random

router = APIRouter(
    prefix='/api',
    tags=['no login'],

)


SESSION = session_init()
DBMANIPULATOR = PackageManipulator(SESSION)
DBUSERMANIPULATOR = UserManipulator(SESSION)


@router.get('/packs/',
            response_model=resp_models.ListOfPackages,
            )
async def recive_list_of_packages(
    likes: str = None,
    downloads: str = None,
    search: str = None,
    size: str = None,
):
    '''
    Returns a list of packages
    '''
    dic = {'likes': likes,
           'downloads':  downloads,
           'search': search,
           'size': size
           }

    package_list = DBMANIPULATOR.select(dic)
    return package_list


@router.get('/fill_the_db/')
async def fill():
    '''Weird bad solution used to fill the empty DB'''
    for i in range(1, 40):
        name = get_random_string()
        desc = get_random_string()
        link = f'https://{get_random_string()}'
        like = random.randint(1, 100)
        download = random.randint(1, 100)
        size = round(random.uniform(1.0, 50.0), 2)
        DBMANIPULATOR.insert(name, desc, link, like, download, size)

    try:
        DBUSERMANIPULATOR.insert(
            "Admin", "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW")
    except:
        print('well')
        return {'message': 'Done'}
    return {'message': 'Done'}
