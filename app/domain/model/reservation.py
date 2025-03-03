""" Reservation Model """
from sqlalchemy import Column, Date, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Reservation(Base):
    __tablename__ = 'reservations'
    
    id = Column(Integer, primary_key=True, index=True)
    
    place_id = Column(
        Integer, 
        ForeignKey('places.id')
    )

    people_id = Column(
        Integer,
        ForeignKey('peoples.id')
    )

    reservation_date = Column(Date)

    place = relationship(
        'Place', 
        back_populates='reservations'
    )

    people = relationship(
        'People', 
        back_populates='reservations'
    )


from app.domain.model.people import People
