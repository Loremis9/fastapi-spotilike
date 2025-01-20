import uuid
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from ....core.database import Base

class User(Base):
    __tablename__ = "user_session"
    
    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_token = Column(String(16), nullable=False)

    def __repr__(self):
        return f"<User(user_name={self.user_name})>"