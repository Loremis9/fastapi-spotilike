from pydantic import BaseModel
from uuid import UUID
from typing import Optional


class TypeCreate(BaseModel):
    title: str
    description: str
    
class TypeOutput(TypeCreate):
    type_id: UUID

class TypeModify(BaseModel):
    title: Optional[str]
    description: Optional[str]