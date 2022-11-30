from fastapi import FastAPI
from .models import models
from .DB_manipulations.db_initialization import insert_to_db, select_from_db
from .DB_manipulations.db import db_init
from fastapi.middleware.cors import CORSMiddleware


def app_factory():
    db_init()
    return FastAPI()


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
    for i in range(1, 10):
        insert_to_db('Incurso', 'Hey', 'Incurso')
    return {'message': 'Done'}


@app.get('/api/main_page/', response_model=models.EnteringMainPage)
async def main_page():
    '''
    Returns list of things necessary for the main page
    Reads those from config.yaml
    '''
    return {'message': 'Done'}


@app.get('/api/receive_packages/',
         response_model=models.ListOfPackages,
         )
async def recive_list_of_packages(page: int = 0):
    '''
    Returns a list of packages
    '''
    package_list = select_from_db()
    print(package_list)
    return package_list
