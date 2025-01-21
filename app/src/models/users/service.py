from sqlalchemy.orm import Session
from . import models
from fastapi import HTTPException
from ....core.security import hash_password
import bcrypt

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id,models.User.deleted_at == False).first()

def get_user_by_email(db: Session, email: str):
    if not email:
       raise HTTPException(status_code=404, detail="User not found")
    return db.query(models.User).filter(models.User.email == email,models.User.deleted_at == False).first()

def create_user(db: Session, name: str, email: str) -> bool:
    db_user = models.User(name=name, email=email)
    db_user.password = db_user.password.encode('utf-8')
    db_user.user_name = db_user.user_name.encode('utf-8')
    db_user.password = hash_password(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return True

def delete_user_by_id(db:Session, user_id: int):
    user = get_user_by_id(user_id).filter(models.User.deleted_at == False)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    return True

def verify_password(db : Session,password: str, hashed_password: str,) -> bool:
    correct_password: bool = bcrypt.checkpw(password.encode(), hashed_password.encode())
    return correct_password

def authenticate_user(db : Session, email: str, password: str)-> models.User:
    db_user = get_user_by_email(db, email)
    if not db_user:
        return False
    if not verify_password(password, db_user.hashed_password):
        return False
    return db_user