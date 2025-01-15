# app/services/user_service.py
from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException
from datetime import datetime, timedelta
from ...core.config import SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
import jwt
import bcrypt

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id,models.User.deleted_at == False).first()


def get_user_by_email(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id,models.User.deleted_at == False).first()

def create_user(db: Session, name: str, email: str):
    db_user = models.User(name=name, email=email)
    db_user.password = salt_password(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user_by_id(db:Session, user_id: int):
    user = get_user_by_id(user_id).filter(models.User.deleted_at == False)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    return True

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    to_encode = data.copy()
    expire = datetime.now(datetime.timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def salt_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)