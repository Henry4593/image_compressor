from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.sql import func
from app.models.base_model import Base

class CompressionHistory(Base):
    __tablename__ = 'compression_history'
    
    history_id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))
    image_id = Column(String(255), ForeignKey('images.image_id'), nullable=False)
    compression_start_time = Column(DateTime, nullable=False, default=func.now())
    compression_end_time = Column(DateTime, nullable=True, default=func.now())
    duration = Column(Integer, nullable=False)  # Duration in seconds or appropriate unit
    result = Column(String(100), nullable=False)

    # Relationship to Images
    image = relationship('Images', back_populates='compression_histories')

    def __repr__(self):
        return f"CompressionHistory(history_id='{self.history_id}', image_id='{self.image_id}', compression_start_time='{self.compression_start_time}', compression_end_time='{self.compression_end_time}', duration={self.duration}, result='{self.result}')"
    