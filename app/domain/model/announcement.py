""" Annoucement model """
from sqlalchemy import Column, Date, Integer, String, Text
from sqlalchemy.sql import func

from app.core.database import Base


class Announcement(Base):
    __tablename__ = 'announcements'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    type = Column(Integer)
    """ 0 - 1 - 2 """
    
    title = Column(String(70), nullable=False)
    description = Column(Text, nullable=True)
    created = Column(Date, default=func.now())




