from fastapi import APIRouter, Depends, HTTPException, Depends
from sqlalchemy.orm import Session
from ...core.database import get_db
from ..models.users import service as service_user
from ..models.users import schemas as schemas_user
from ..models.user_sessions import schemas 
from ...core.security import create_access_token, return_http_error, verify_refresh_token
from ..models.user_sessions import service as service_user_session
from ...core.security import return_http_error
router = APIRouter(tags=["auth"])


@router.post("/login/", response_model=schemas.Token)
async def connect_user(user:schemas.Login , db: Session = Depends(get_db)) -> schemas.Token:
    db_user = service_user.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise return_http_error("Incorrect username or password")
    access_token = create_access_token(data={"sub": db_user.email})
    acces_refresh_token = service_user_session.save_refresh_token(db,email=db_user.email)
    return schemas.Token(access_token=access_token, refresh_token=acces_refresh_token)

@router.post("/signup/", response_model=schemas.Token)
def create_user(user: schemas_user.UserCreate, db: Session = Depends(get_db))-> schemas.Token:
    db_user_verify = service_user.get_user_by_email(db, email=user.email)
    if db_user_verify:
        raise  return_http_error("Email already registered")
    
    db_user = service_user.create_user(db, user)
    access_token = create_access_token(data={"sub": db_user.email})
    acces_refresh_token = service_user_session.save_refresh_token(db,email=db_user.email)
    return schemas.Token(access_token=access_token, refresh_token=acces_refresh_token)



@router.post("/refresh", response_model=schemas.TokenOutput)
async def refresh_token(refresh_token: schemas.RefreshToken, db: Session = Depends(get_db)) -> schemas.TokenOutput:
    email = verify_refresh_token(refresh_token=refresh_token.refresh_token)
    db_user =service_user.get_user_by_email(db,email)
    if not db_user:
        raise return_http_error("Incorrect username or password")
    new_access_token = create_access_token(data={"sub": db_user.email})
    return schemas.TokenOutput(access_token= new_access_token)