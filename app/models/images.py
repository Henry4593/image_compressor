from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.sql import func
from app.models.base_model import Base

class Images(Base):
    __tablename__ = 'images'
    
    image_id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))
    user_id = Column(String(255), ForeignKey('users.user_id'), nullable=False)
    filename = Column(String(255), nullable=False)
    original_path = Column(String(255), nullable=False)
    compressed_path = Column(String(255), nullable=False)
    upload_date = Column(DateTime, nullable=False, default=func.now())
    compression_date = Column(DateTime, nullable=True, default=func.now())
    original_size = Column(Integer, nullable=False)
    compressed_size = Column(Integer, nullable=False)
    compression_status = Column(String(50), nullable=False, default="pending")
    image_format = Column(String(20), nullable=False)

    # Relationship to Users
    user = relationship('Users', back_populates='images')

    # Relationship to CompressionHistory
    compression_histories = relationship('CompressionHistory', back_populates='image')

    def __repr__(self):
        return f"Images(image_id='{self.image_id}', user_id='{self.user_id}', original_file_name='{self.original_file_name}', compressed_file_name='{self.compressed_file_name}', upload_date='{self.upload_date}', compression_date='{self.compression_date}', original_file_size={self.original_file_size}, compressed_file_size={self.compressed_file_size}, compression_status='{self.compression_status}', image_format='{self.image_format}')"