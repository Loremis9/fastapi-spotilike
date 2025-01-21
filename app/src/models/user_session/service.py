import jwt
from fastapi import  Depends
from typing import Annotated
from ..users.service import get_user_by_email
from .models import UserSession
from sqlalchemy.orm import Session
from jwt.exceptions import InvalidTokenError
from fastapi.security import OAuth2PasswordBearer
from ....core.config import SECRET_KEY, ALGORITHM
from ..users.schemas import TokenData
from ....core.security import create_refresh_token, verify_refresh_token_validity, return_credentials_exception

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def save_refresh_token(db: Session,email =str) -> str:
    db_user = get_user_by_email(db,email)
    db_token = db.query(UserSession).filter(UserSession.user_id == db_user.id).first()
    if not db_token or not db_token.refresh_token:
        db_token.user_refresh_token = create_refresh_token(data={"sub": email})
        db.add(db_token)
        db.commit()
        db.refresh(db_token)
    if verify_refresh_token_validity(db_token):
        return db_token.refresh_token
    return db_token.refresh_token

def get_refresh_token(db: Session, email:str) -> bool:
    db_user = get_user_by_email(db,email)
    db_token = db.query(UserSession).filter(UserSession.user_id == db_user.id).first()
    if not db_token.user_refresh_token:
        False
    return True


#vérifie dans le header s'il y'a un token
async def get_current_user(db, Session, token: Annotated[str, Depends(oauth2_scheme)])-> UserSession:
    credentials_exception = return_credentials_exception()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user_by_email(db=db, email=token_data.email)
    if user is None:
        raise credentials_exception
    return user






