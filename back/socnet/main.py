from fastapi.middleware.cors import CORSMiddleware
from socnet.DB_manipulations.db import db_init
from fastapi import FastAPI

from socnet.routers import authet,  users, common


def app_factory():
    '''Creates the database, if does not exists, returns a FastAPI object to run the app'''
    db_init()
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
    )

    # Add routes to the FastAPI app.
    app.include_router(users.router)
    app.include_router(authet.router)
    app.include_router(common.router)

    return FastAPI()


app = app_factory()

# From where you can send requests to the app
# Doesn't work yet for the test purposes
origins = [
    "http://localhost:3000",
    "localhost:3000"
]
