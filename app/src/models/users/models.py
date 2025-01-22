import uuid
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ....core.database import Base
import enum

class StrEnum(str, enum.Enum):
    pass
class Genre(StrEnum):
    male = 'M'
    female = 'F'

class Role(Base):
    __tablename__ = "roles"
    
    role_id = Column(Integer, primary_key=True, autoincrement=True)
    role_name = Column(String(20), nullable=False, unique=True)
    
    users = relationship("User", back_populates="role")

    def __repr__(self):
        return f"<Role(role={self.role})>"
    

class User(Base):
    __tablename__ = "users"
    
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_name = Column(String(16), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(50), nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    age = role_id = Column(Integer, nullable=True)
    genre =  Column(Enum(Genre,native_enum=False), nullable=True)
    role_id = Column(Integer, ForeignKey('roles.role_id'), default=1)
    role = relationship("Role", back_populates="users") 

    user_session = relationship("UserSession", back_populates="user")
    def __repr__(self):
        return f"<User(user_name={self.user_name})>"

