from fastapi import FastAPI
from .models import resp_models, req_models
from .DB_manipulations.db_initialization import insert_to_db, select_from_db, delete_from_db
from .DB_manipulations.db import db_init, session_init
from fastapi.middleware.cors import CORSMiddleware


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
        insert_to_db(SESSION, 'Incurso', 'Hey', 'Incurso')
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
async def recive_list_of_packages(page: int = 0):
    '''
    Returns a list of packages
    '''
    package_list = select_from_db(SESSION)
    print(package_list)
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
        pack_to_create.download_link)

    return result


@app.delete('/api/packs/', response_model=resp_models.Message)
async def delete_package(pack_id: req_models.delete_package):
    '''
    Receives id. 
    Deletes pack with this id
    '''
    result = delete_from_db(SESSION, pack_id)
    return result


@app.put('/api/packs/like/', response_model=resp_models.Message)
async def add_like_to_package(pack_id: req_models.add_like_down):
    pass


@app.put('/api/packs/download/', response_model=resp_models.Message)
async def add_download_to_package(pack_id: req_models.add_like_down):
    pass


@app.put('/api/packs/')
async def modify_package():
    '''
    Whatever. Not implemented yet. 
    '''
