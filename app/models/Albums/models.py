import uuid
from sqlalchemy import Column, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from ...core.database import Base


class Album(Base):
    __tablename__ = "albums"
    
    album_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    pouch = Column(String(255))
    release_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.artist_id"), nullable=False)
    artist = relationship("Artist", back_populates="albums")
    
    album_song_relationship = relationship("Song", back_populates="song_album_relationship")
    
    def __repr__(self):
        return f"<Album(title={self.title})>"