from fastapi import APIRouter
from ..models import req_models, resp_models
from fastapi import Depends
from ..DB_manipulations.db import session_init
from ..DB_manipulations.db_methods import insert_to_db, \
    delete_from_db, add_like_to_package, add_download_to_package, \
    update_values_of_package
from ..dependence.mydepen import get_current_active_user

router = APIRouter(
    prefix='/api',
    tags=['need to log in, user'],
    dependencies=[Depends(get_current_active_user)]
)


SESSION = session_init()


@router.post('/packs/', response_model=resp_models.Message)
async def create_package(pack_to_create: req_models.CreatePackage):
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


@router.delete('/packs/delete/{pack_id}', response_model=resp_models.Message)
async def delete_package(pack_id):
    '''
    Receives id
    Deletes pack with this id
    '''
    result = delete_from_db(SESSION, pack_id)
    return result


@router.put('/packs/like/{pack_id}', response_model=resp_models.Message)
async def add_like_to_pack(pack_id: int):
    '''
    Add 1 like to package with certain id
    '''
    result = add_like_to_package(SESSION, pack_id)
    return result


@router.put('/packs/download/{pack_id}', response_model=resp_models.Message)
async def add_download_to_pack(pack_id: int):
    '''
    Add 1 download to package with certain id
    '''
    result = add_download_to_package(SESSION, pack_id)
    return result


@router.put('/packs/', response_model=resp_models.Message)
async def modify_package(pack_to_update: req_models.UpdatePackage):
    '''
    Modify the values of specified package
    '''
    result = update_values_of_package(SESSION, pack_to_update)
    return result
