from typing import List
from fastapi.security import OAuth2PasswordBearer
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

###
# Properties configurations
###

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"

config = Config(".env")

ROUTE_PREFIX_V1 = "/v1"

ALLOWED_HOSTS: List[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
SECRET_KEY = "poissonchat"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")