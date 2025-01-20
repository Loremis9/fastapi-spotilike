from fastapi import FastAPI
from .core.database import create_db
from .test.load_data.load_datas import load_all_test_data 
from .src.routers import api
from .core.config import API_PREFIX
from .core.dependencies import logger_errors

def get_app()->FastAPI:
    logger = logger_errors()
    app = FastAPI()
    create_db(logger)
    app.include_router(api.router, prefix=API_PREFIX)
    return app

app = get_app()

@app.on_event("startup")
async def load_test_data():
   load_all_test_data()

@app.get("/")
async def root():
    return {"running": "it's alive"}



