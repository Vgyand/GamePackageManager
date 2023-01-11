from fastapi import APIRouter
from ..models import resp_models

from ..DB_manipulations.db import session_init
from ..DB_manipulations.db_methods2 import PackageManipulator

from ..etc.randomstring import get_random_string
import random

router = APIRouter(
    prefix='/api',
    tags=['no login'],

)


SESSION = session_init()
DBMANIPULATOR = PackageManipulator(SESSION)


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


@router.get('/fill the db/')
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
    return {'message': 'Done'}
