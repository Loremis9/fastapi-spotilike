from . import models, schemas
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime

def get_all_types(db: Session, skip : int = 0, limit : int =100):
    return db.query(models.Type).filter(models.Type.deleted_at.is_(None)).offset(skip).limit(limit).all()

def get_type_by_id(db: Session, type_id: int):
    return db.query(models.Type.type_id == type_id).filter(models.Type.deleted_at.is_(None)).first()

def put_type(db : Session, type: schemas.TypeOutput):
    db_type = get_type_by_id(type.type_id)
    if not db_type:
        raise HTTPException(status_code=404, detail="type not found")
    db_type.description = type.description
    db_type.title = type.title
    db_type.artist_id = type.artist_id
    db_type.updated_at = datetime.now(datetime.timezone.utc)
    db.commit()
    return db_type