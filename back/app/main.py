import random
from .etc.randomstring import get_random_string
from fastapi.middleware.cors import CORSMiddleware
from .DB_manipulations.db import db_init
from fastapi import FastAPI
from .models import resp_models
from .DB_manipulations.db_methods import insert_to_db, select_from_db

from .routers import authet,  users


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

app.include_router(users.router)
app.include_router(authet.router)


# Needs to be removed later
# @app.get('/api/fill_the_db/')
# async def fill_db():
#     for i in range(1, 40):
#         name = get_random_string()
#         desc = get_random_string()
#         link = f'https://{get_random_string()}'
#         like = random.randint(1, 100)
#         download = random.randint(1, 100)
#         size = round(random.uniform(1.0, 50.0), 2)
#         insert_to_db(SESSION, name, desc, link, like, download, size)
#     return {'message': 'Done'}
