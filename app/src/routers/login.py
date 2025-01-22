from fastapi import APIRouter, Depends, HTTPException, Depends
from sqlalchemy.orm import Session
from ...core.database import get_db
from ..models.users import service as service_user, schemas
from ...core.security import create_access_token, return_credentials_exception, verify_refresh_token
from ..models.user_session import service as service_user_session

router = APIRouter(tags=["auth"])


@router.post("/login/", response_model=schemas.Token)
async def connect_user(user:schemas.Login , db: Session = Depends(get_db)):
    db_user = service_user.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(
            return_credentials_exception(message="Incorrect username or password")
        )
    access_token = create_access_token(data={"sub": db_user.email})
    acces_refresh_token = service_user_session.save_refresh_token(db,email=db_user.email)
    return schemas.Token(access_token=access_token, refresh_token=acces_refresh_token)

@router.post("/signup/", response_model=schemas.UserOutput)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user_verify = service_user.get_user_by_email(db, email=user.email)
    if db_user_verify:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = service_user.create_user(db, user)
    access_token = create_access_token(data={"sub": db_user.email})
    acces_refresh_token = service_user_session.save_refresh_token(db,email=db_user.email)
    return schemas.Token(access_token=access_token, refresh_token=acces_refresh_token)



@router.post("/refresh", response_model=schemas.UserOutput)
async def refresh_token(refresh_token: schemas.RefreshToken, db: Session = Depends(get_db)):
    email = verify_refresh_token(refresh_token=refresh_token.refresh_token)
    db_user =service_user.get_user_by_email(db,email)
    if not db_user:
        raise HTTPException(
            return_credentials_exception(message="Incorrect username or password")
        )
    new_access_token = create_access_token(data={"sub": db_user.email})
    return {"access_token": new_access_token, "token_type": "bearer"}