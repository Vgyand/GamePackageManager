from fastapi import FastAPI
from .models import models
from .DB_manipulations import db_work


app = FastAPI()


@app.get('/main_page/', response_model=models.RespModels.RM_MainPage)
async def main_page():
    return {'message': 'Done'}


@app.get('/api/packs/', response_model=models.RespModels.RM_Package_list)
async def package_list_recievement():
    return {'message': 'Done'}


@app.post('/main_page/', response_model=models.RespModels.RM_Package_list)
async def changing_package_page():
    return {'message': 'Done'}


@app.get('/main_page/', response_model=models.RespModels.RM_Package_list)
async def filter_search_apply():
    return {'message': 'Done'}
