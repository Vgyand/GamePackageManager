from datetime import datetime, timedelta

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from ..etc.readyaml import read_config_yaml
from ..models.auth_models import Token, TokenData, User, UserInDB
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..dependence import mydepen

ALGIRITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = read_config_yaml()['secret_key']

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={404: {'desctiption': 'Not Found'}},
)

fake_users_db = {
    "johndoe": {
        "username": "Admin",
        "full_name": "Admin",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}


@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = mydepen.authenticate_user(
        fake_users_db, form_data.username, form_data.password)
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


@router.get("/users/me/items/")
async def read_own_items(current_user: User = Depends(
        mydepen.get_current_active_user)):
    return [{"item_id": "Foo", "owner": current_user.username}]
