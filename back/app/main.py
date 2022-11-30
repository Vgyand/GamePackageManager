from fastapi import FastAPI
from .models import models
from .DB_manipulations.db_initialization import insert_to_db, select_from_db


app = FastAPI()


@app.get('/main_page/', response_model=models.EnteringMainPage)
async def main_page():
    '''
    Returns list of things necessary for the main page
    Reads those from config.yaml
    '''
    insert_to_db('Incurso', 'Hey', 'Incurso')
    return {'message': 'Done'}


@app.get('/receive_packages/',
         response_model=models.ListOfPackages,
         )
async def recive_list_of_packages(page: int = 0):
    '''
    Returns a list of packages
    '''
    package_list = select_from_db()
    print(package_list)
    return package_list
