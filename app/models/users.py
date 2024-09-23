from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from sqlalchemy.sql import func
from app.models.base_model import Base

class Users(Base):
    __tablename__ = 'users'
    
    user_id = Column(String(255), primary_key=True, default=lambda: str(uuid4()))
    first_name = Column(String(150), nullable=False)
    last_name = Column(String(150), nullable=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now())

    # Relationship to Images
    images = relationship('Images', back_populates='user', cascade="all, delete-orphan", lazy=True)
    compression_histories = relationship('CompressionHistory', back_populates='user', cascade="all, delete-orphan", lazy=True)

    def __repr__(self):
        return f"User(user_id='{self.user_id}', first_name='{self.first_name}', last_name='{self.last_name}', username='{self.username}', email='{self.email}')"
    



