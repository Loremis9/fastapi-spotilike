from pydantic import BaseModel
from typing import Optional
from typing import Union

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserOutput(BaseModel):
    jwt_refresh: Optional[str]


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str

class TokenData(BaseModel):
    email: Union[str, None] = None

class Login(BaseModel):
    email: str
    password: str