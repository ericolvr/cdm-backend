""" Place Model """
from sqlalchemy import Column, Integer, NUMERIC, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Place(Base):
    __tablename__ = 'places'
    
    id = Column(Integer, primary_key=True, index=True)    
    name = Column(String(50))
    price = Column(NUMERIC(10, 2))
    description = Column(String(200))

    reservations = relationship(
        'Reservation', 
        back_populates='place'
    )


from app.domain.model.reservation import Reservation
