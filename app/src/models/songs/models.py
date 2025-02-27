import uuid
from sqlalchemy import  Column, Integer, String, DateTime, ForeignKey, Index
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy.dialects.postgresql import UUID
from ....core.database import Base


class Song(Base):
    __tablename__ = "songs"
    
    song_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100), nullable=False)
    duration = Column(Integer, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    artist_id = Column(UUID(as_uuid=True), ForeignKey('artists.artist_id', ondelete="CASCADE"))
    album_id = Column(UUID(as_uuid=True), ForeignKey('albums.album_id')) 

    artist = relationship('Artist', back_populates='songs')
    song_album_relationship = relationship("Album", back_populates="album_song_relationship")

    type_id = Column(UUID(as_uuid=True), ForeignKey('types.type_id', ondelete="CASCADE"))
    type = relationship('Type', back_populates='songs')

    __table_args__ = (
        Index('idx_artist_id', 'artist_id'),
    )
    __table_args__ = (
        Index('idx_album_id', 'album_id'),
    )
    
    def __repr__(self):
        return f"<song(title={self.title}, duration={self.duration})>"
    