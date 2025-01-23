""" User model """
from sqlalchemy import Boolean, Column, Integer, String
from app.core.database import Base


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    mobile = Column(String(20), unique=True, nullable=False)
    role = Column(String(20), nullable=False)
    password = Column(String(255), nullable=False)
    status = Column(Boolean, default=True)
    