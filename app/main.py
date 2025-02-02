from fastapi import FastAPI
from .core.database import create_db
from .test.load_data.load_datas import load_all_test_data 
from .src.routers import api
from .core.config import API_PREFIX
from fastapi.middleware.cors import CORSMiddleware

def get_app()->FastAPI:

    app = FastAPI()
    origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
    ]

    app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
    create_db()
    app.include_router(api.router, prefix=API_PREFIX)
    return app

app = get_app()

@app.on_event("startup")
async def load_test_data():
   load_all_test_data()

@app.get("/")
async def root():
    return {"running": "it's alive"}



