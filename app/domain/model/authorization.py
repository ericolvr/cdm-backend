""" Authorization model """
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Authorization(Base):
    __tablename__ = 'authorizations'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    type = Column(Integer)
    """
        0 - single people
        1 - service provider
        2 - party - .xls contains many names
    """
    
    name = Column(String(50), nullable=False)
    document = Column(String(20), nullable=True)

    authorization_date = Column(Date)

    hour_start = Column(String(15), nullable=True)
    hour_end = Column(String(15), nullable=True)



