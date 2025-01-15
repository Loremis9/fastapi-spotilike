from pydantic import BaseModel
from uuid import UUID
class TypeCreate(BaseModel):
    title: str
    description: str
    
class TypeOutput(TypeCreate):
    type_id: UUID