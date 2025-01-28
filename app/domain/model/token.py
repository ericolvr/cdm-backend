""" Token model """
from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.core.database import Base


class Token(Base):
    __tablename__ = 'tokens'
    
    id = Column(Integer, primary_key=True, index=True)    
    mobile = Column(String(20), nullable=True)
    number = Column(String(6))
    used = Column(Boolean, default=False)
    created = Column(
        DateTime, default=datetime.utcnow, 
        nullable=True
    )
