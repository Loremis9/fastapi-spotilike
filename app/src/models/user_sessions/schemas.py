from pydantic import BaseModel
from typing import Optional
from typing import Union


class RefreshToken(BaseModel):
    refresh_token: str

class Token(BaseModel):
    access_token: str
    refresh_token: str

class TokenData(BaseModel):
    email: Union[str, None] = None

class Login(BaseModel):
    email: str
    password: str

class TokenOutput(BaseModel):
    access_token : str