from datetime import timedelta

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status

from passlib.context import CryptContext
from socnet.etc.readyaml import read_config_yaml
from socnet.models.auth_models import Token, TokenData, User, UserInDB
from fastapi.security import OAuth2PasswordRequestForm
from socnet.dependence import mydepen
from socnet.DB_manipulations.db import session_init
from socnet.DB_manipulations.db_methods2 import UserManipulator

ALGIRITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = read_config_yaml()['secret_key']


SESSION = session_init()
USERMANIPULATOR = UserManipulator(SESSION)

list_of_users = USERMANIPULATOR.select()


router = APIRouter(
    prefix='/api',
    tags=['auth'],
    responses={404: {'desctiption': 'Not Found'}},
)


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    '''Returns JWT token when passed login and password'''
    user = mydepen.authenticate_user(
        list_of_users, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = mydepen.create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=User)
async def read_users_me(
        current_user: User = Depends(mydepen.get_current_active_user)):
    return current_user
