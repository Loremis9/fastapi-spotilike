import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from ....core.database import Base

class UserSession(Base):
    __tablename__ = "user_session"
    
    user_session_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_refresh_token = Column(String(500), nullable=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", back_populates="user_session")
    def __repr__(self):
        return f"<User(user_name={self.user_name})>"