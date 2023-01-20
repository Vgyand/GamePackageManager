from pydantic import BaseModel


class Token(BaseModel):
    # Token
    access_token: str
    token_type: str


class TokenData(BaseModel):
    # Data from Token
    username: str | None = None


class User(BaseModel):
    # User
    username: str
    disabled: bool | None = None


class UserInDB(User):
    hashed_password: str
