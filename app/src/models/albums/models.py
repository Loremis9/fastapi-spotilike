import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from ....core.database import Base


class Album(Base):
    __tablename__ = "albums"
    
    album_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    pouch = Column(String(255), nullable=True)
    release_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    artist_id = Column(UUID(as_uuid=True), ForeignKey("artists.artist_id", ondelete="CASCADE"))
    artist = relationship("Artist", back_populates="albums")
    
    album_song_relationship = relationship("Song", back_populates="song_album_relationship")
    
    __table_args__ = (
        Index('idx_album_artist_id', 'artist_id'),
    )
    def __repr__(self):
        return f"<Album(title={self.title})>"