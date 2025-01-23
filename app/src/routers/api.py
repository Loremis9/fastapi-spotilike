from fastapi import APIRouter
from . import albums, login, songs, artists
from fastapi import APIRouter

router = APIRouter()

def include_api_routes():
    router.include_router(albums.router)
    router.include_router(login.router)
    router.include_router(songs.router)
    router.include_router(artists.router)
    
include_api_routes()