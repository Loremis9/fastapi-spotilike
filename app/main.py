from fastapi import FastAPI
from fastapi import FastAPI, Request, Response
from .routers import albums, login, songs
from .core.database import engine, Base,get_db
import logging
from sqlalchemy.exc import SQLAlchemyError

#from .test.insert_data import (
#    insert_data_users_role,
#    insert_data_artists,
#    insert_data_albums,
#    insert_type_data,
#    insert_songs_data)
logging.basicConfig(
    level=logging.INFO,  # Niveau de log : DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Format du log
)
logger = logging.getLogger(__name__)
def get_app()->FastAPI:

    app = FastAPI()
    try:
        # Tentative de création des tables
        Base.metadata.create_all(bind=engine)
        logger.info("Tables created successfully.")
    except SQLAlchemyError as e:
        # En cas d'erreur dans la base de données
        logger.error(f"Database error: {str(e)}")
    except Exception as e:
        # Pour capturer d'autres erreurs possibles
        logger.error(f"Unexpected error: {str(e)}")

    app.include_router(albums.router)
    app.include_router(login.router)
    app.include_router(songs.router)

    return app

app = get_app()

#@app.on_event("startup")
#async def load_test_data():
#    db = next(get_db()) 
#    try:
#        insert_data_users_role(db)
#        insert_data_artists(db)
#        insert_data_albums(db)
#        insert_type_data(db)
#        insert_songs_data(db)
#    finally:
#        db.close()

#    print("Test data loaded successfully.")

@app.get("/error")
async def trigger_error():
    logger.error("Une erreur s'est produite.")
    return {"message": "Erreur rencontrée."}





@app.get("/")
async def root():
    return {"running": "it's alive"}



