from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    mdp: str

class UserOutput(BaseModel):
    jwt: str
    jwt_refresh: Optional[str]
    