from fastapi.security import OAuth2PasswordBearer
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings
from fastapi import status

API_PREFIX = "/api"

JWT_TOKEN_PREFIX = "Authorization"
TOKEN_REFRESH = "Refresh"
TOKEN_BEARER = "Bearer "
config = Config(".env")

ALLOWED_HOSTS: list[str] = config(
    "ALLOWED_HOSTS",
    cast=CommaSeparatedStrings,
    default="",
)
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

NOT_FOUND = status.HTTP_404_NOT_FOUND
UNAUTHORIZED = status.HTTP_401_UNAUTHORIZED
BAD_REQUEST = status.HTTP_400_BAD_REQUEST