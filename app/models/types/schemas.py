from pydantic import BaseModel

class TypeCreate(BaseModel):
    title: str
    description: str
    
class TypeOutput(TypeCreate):
    type_id: str