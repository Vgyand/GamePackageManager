from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from passlib.context import CryptContext
from ..etc.readyaml import read_config_yaml
from ..models.auth_models import Token, TokenData, User, UserInDB
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..DB_manipulations.db import session_init
from ..DB_manipulations.db_methods2 import UserManipulator


ALGIRITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30
SECRET_KEY = read_config_yaml()['secret_key']

SESSION = session_init()
USERMANIPULATOR = UserManipulator(SESSION)

list_of_users = USERMANIPULATOR.select()


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/token')


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db, username: str):
    if username in db:
        user_dict = db[username]

        user_dict = {
            'hashed_password': user_dict['hashedpassword'],
            'username': user_dict['username'],
        }
        print('--------------------------', user_dict)
        return UserInDB(**user_dict)


def authenticate_user(db_of_users, username: str, password: str):
    user = get_user(db_of_users, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGIRITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate:': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGIRITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(list_of_users, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail='Inactive user')
    return current_user
