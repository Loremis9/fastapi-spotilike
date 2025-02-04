from . import models, schemas
from sqlalchemy.orm import Session
from datetime import datetime
from ....core.security import return_http_error
from uuid import UUID
from ....core.log import logging
from ....core.log.metrics import log_info


def get_type_by_name(db: Session, type_name: str) -> models.Type:
    type_name = type_name.lower()
    db_type =  db.query(models.Type).filter(models.Type.title.lower() == type_name, models.Type.deleted_at.is_(None)).first()
    if not db_type:
        raise return_http_error("type not found")
    log_info("getTypeName")
    return db_type

def get_all_types(db: Session, skip : int = 0, limit : int =100)-> list[models.Type]:
    db_types =  db.query(models.Type).filter(models.Type.deleted_at.is_(None)).offset(skip).limit(limit).all()
    if not db_types:
        raise return_http_error("type not found")
    log_info("getTypes")
    return db_types

def get_type_by_id(db: Session, type_id: UUID)-> models.Type:
    db_type= db.query(models.Type).filter(models.Type.type_id == type_id,models.Type.deleted_at.is_(None)).first()
    if not db_type:
        raise return_http_error("type not found")
    log_info("getTypeId")
    return db_type
    

def put_type(db : Session,genre_id : UUID, type: schemas.TypeOutput) -> models.Type:
    db_type = get_type_by_id(db,genre_id)
    if not db_type:
        raise return_http_error("type not found")
    db_type.description = type.description
    db_type.title = type.title
    db_type.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_type)
    log_info("createType")
    return db_type

def get_type_by_name(db: Session, type_name: str) -> models.Type:
    db_type =  db.query(models.Type).filter(models.Type.title == type_name, models.Type.deleted_at.is_(None)).first()
    if not db_type:
        raise return_http_error("type not found")
    log_info("getTypeByName")
    return db_type

def get_type_by_id(db: Session, id: str) -> models.Type:
    db_type= db.query(models.Type).filter(models.Type.type_id == id, models.Type.deleted_at.is_(None)).first()
    if not db_type:
        raise return_http_error("type not found")
    log_info("getTypeById")
    return db_type

def remove_type(db: Session, type_id: UUID) -> bool:
    db_type = get_type_by_id(db,type_id)
    if not db_type:
        return False
    logging.log_info_console(db_type.type_id)
    db.delete(db_type)
    db.commit()
    log_info("removeType")
    return True
