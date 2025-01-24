from datetime import datetime, timedelta
from .config import SECRET_KEY, ALGORITHM
import jwt
import bcrypt
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError,ExpiredSignatureError
from fastapi import  HTTPException, status
from .config import NOT_FOUND, UNAUTHORIZED
from .log import metrics
def create_access_token(data) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def create_refresh_token(data) -> str:
    payload = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60*24*30*6)
    payload.update({"exp": expire})
    encoded_jwt_refresh = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt_refresh

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def get_pwd_context() -> CryptContext:
    return CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_refresh_token_validity(refresh_token: str) -> bool:
    if not refresh_token:
        return False
    try:
        jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError:
        return False
    return True


def verify_refresh_token(refresh_token: str) -> str:
    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub") 
    except ExpiredSignatureError:
        raise return_http_error("Refresh token has expire")
    except InvalidTokenError:
        raise return_http_error("Invalid refresh token")


def return_http_error(message : str, status_http : status = NOT_FOUND) -> HTTPException :
    metrics.error_counter(list[message,status_http])
    raise  HTTPException(
        status_code=status_http,
        detail=message,
    )

def return_headers_error(message : str = "Could not validate credentials", status_http : status = UNAUTHORIZED) -> HTTPException :
    metrics.error_counter(list[message,status_http])
    raise  HTTPException(
        status_code=status_http,
        detail=message,
        headers={"WWW-Authenticate": "Bearer"}
    )
