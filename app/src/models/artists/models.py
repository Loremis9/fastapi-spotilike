import uuid
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from ....core.database import Base

class Artist(Base):
    __tablename__ = "artists"
    
    artist_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    artist_name = Column(String(100),unique=True, nullable=False)
    avatar = Column(String(255),nullable= True)
    biography = Column(Text, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    albums = relationship("Album", back_populates="artist", cascade="all, delete-orphan")
    songs = relationship('Song', back_populates='artist', cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Artist(artist_name={self.artist_name})>"
