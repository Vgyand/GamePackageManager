from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

FakeDB = {
    '1': 'Pretend that this is a link to pack',
}


@app.get('/main_page/')
async def main_page():
    return FakeDB


@app.post('/main_page/')
async def upload_game_pack():
    '''
    Doesn't really upload anything for now,
    but I need to imagine the structure
    '''
    return {'message': 'Done'}


@app.get('/pack{pack_id}/')
async def get_pack(pack_id: int):
    return {'pack_id': FakeDB[pack_id]}
