from sqlalchemy.orm import Session
from . import models
import bcrypt
from ....core.security import return_http_error, hash_password
from ....core.log.metrics import log_info_console
from .schemas import UserCreate

def get_user_by_id(db: Session, user_id: int) -> models.User:
    return db.query(models.User).filter(models.User.id == user_id,models.User.deleted_atis_(None)).first()

def get_user_by_email(db: Session, email: str):
    if not email:
       raise return_http_error("User not found")
    return db.query(models.User).filter(models.User.email == email,models.User.deleted_at.is_(None)).first()

def create_user(db: Session, user : UserCreate) -> bool:
    db_user = models.User(user_name=user.name, email=user.email,password=user.password)
    db_user.password = db_user.password
    db_user.user_name = db_user.user_name
    db_user.password = hash_password(db_user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    log_info_console("create user")
    return db_user

def delete_user_by_id(db:Session, user_id: int)-> bool :
    user = get_user_by_id(user_id).filter(models.User.deleted_at.is_(None))
    if not user:
        raise return_http_error("User not found")
    db.delete(user)
    log_info_console("delete user")
    return True

def verify_password(db: Session, password: str, hashed_password: str) -> bool:
    if isinstance(hashed_password, str):
        hashed_password = hashed_password.encode() 
    return bcrypt.checkpw(password.encode(), hashed_password)

def authenticate_user(db : Session, email: str, password: str)-> models.User:
    db_user = get_user_by_email(db, email)
    if not db_user:
        return False
    if not verify_password(db,password, db_user.password):
        return False
    log_info_console("authenticate user")
    return db_user