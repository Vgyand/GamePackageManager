from fastapi import APIRouter
from socnet.models import req_models, resp_models
from fastapi import Depends
from socnet.DB_manipulations.db import session_init
from socnet.dependence.mydepen import get_current_active_user
from socnet.DB_manipulations.db_methods2 import PackageManipulator, UserManipulator

router = APIRouter(
    prefix='/api',
    tags=['need to log in, user'],
    dependencies=[Depends(get_current_active_user)]
)


SESSION = session_init()

PACKAGEMANIPULATOR = PackageManipulator(SESSION)


@router.post('/packs/', response_model=resp_models.Message)
async def create_package(pack_to_create: req_models.CreatePackage):
    '''
    Receives parameters:
    name, description, download_link
    '''
    result = PACKAGEMANIPULATOR.insert(
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
    result = PACKAGEMANIPULATOR.delete(pack_id)
    return result


@router.put('/packs/like/{pack_id}', response_model=resp_models.Message)
async def add_like_to_pack(pack_id: int):
    '''
    Add 1 like to package with certain id
    '''
    result = PACKAGEMANIPULATOR.add_like_to_package(pack_id)
    return result


@router.put('/packs/download/{pack_id}', response_model=resp_models.Message)
async def add_download_to_pack(pack_id: int):
    '''
    Add 1 download to package with certain id
    '''
    result = PACKAGEMANIPULATOR.add_download_to_package(pack_id)
    return result


@router.put('/packs/', response_model=resp_models.Message)
async def modify_package(pack_to_update: req_models.UpdatePackage):
    '''
    Modify the values of specified package
    '''
    result = PACKAGEMANIPULATOR.update_values_of_package(pack_to_update)
    return result
