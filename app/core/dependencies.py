from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Header, HTTPException
import jwt
import logging

def decode(token):
    striped_token = token.replace("Bearer ", "")
    return jwt.decode(token, "secret", algorithm="HS256")

def encode():
    return jwt.encode({"some": "payload"}, "secret", algorithm="HS256")

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")

async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

def logger_errors():
   return logging.basicConfig(
    level=logging.ERROR, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
