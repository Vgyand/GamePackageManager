import random
from .etc.randomstring import get_random_string
from fastapi.middleware.cors import CORSMiddleware
from .DB_manipulations.db import db_init, session_init
from fastapi import FastAPI
from .models import resp_models, req_models
from .DB_manipulations.db_initialization import insert_to_db, select_from_db, \
    delete_from_db, add_like_to_package, add_download_to_package


def app_factory():
    db_init()
    return FastAPI()


SESSION = session_init()

app = app_factory()


origins = [
    "http://localhost:3000",
    "localhost:3000"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/api/fill_the_db/')
async def fill_db():
    for i in range(1, 40):
        name = get_random_string()
        desc = get_random_string()
        link = f'https://{get_random_string()}'
        like = random.randint(1, 100)
        download = random.randint(1, 100)
        size = round(random.uniform(1.0, 50.0), 2)
        insert_to_db(SESSION, name, desc, link, like, download, size)
    return {'message': 'Done'}


@app.get('/api/main_page/', response_model=resp_models.EnteringMainPage)
async def main_page():
    '''
    Returns list of things necessary for the main page
    Reads those from config.yaml
    '''
    return {'message': 'Done'}


@app.get('/api/packs/',
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

    package_list = select_from_db(SESSION, dic)
    return package_list


@app.post('/api/packs/', response_model=resp_models.Message)
async def create_package(pack_to_create: req_models.create_package):
    '''
    Receives parameters:
    name, description, download_link
    '''
    result = insert_to_db(
        SESSION,
        pack_to_create.name,
        pack_to_create.description,
        pack_to_create.download_link,
        0, 0,
        pack_to_create.size,)

    return result


@app.delete('/api/packs/delete/{id}', response_model=resp_models.Message)
async def delete_package(id):
    '''
    Receives id
    Deletes pack with this id
    '''
    result = delete_from_db(SESSION, id)
    return result


@app.put('/api/packs/like/{pack_id}', response_model=resp_models.Message)
async def add_like_to_pack(pack_id: int):
    result = add_like_to_package(SESSION, pack_id)
    return result


@app.put('/api/packs/download/{pack_id}', response_model=resp_models.Message)
async def add_download_to_pack(pack_id: int):
    result = add_download_to_package(SESSION, pack_id)
    return result


@app.put('/api/packs/')
async def modify_package():
    '''
    Whatever. Not implemented yet.
    '''
