from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from .log.logging import logger
###
# Database Configuration
###

SQLALCHEMY_DATABASE_URL = "postgresql://admin:adminpassword@localhost/fastapi_spotilike"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db():
    try:
        Base.metadata.create_all(bind=engine)
    except SQLAlchemyError as e:
        logger.error(f"Database error: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")