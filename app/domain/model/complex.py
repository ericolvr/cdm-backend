""" Complex model """
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Complex(Base):
    __tablename__ = 'complexes'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(String(50), nullable=False)
    floors = Column(Integer)
    apartments_by_floor = Column(Integer)
    
    apartments = relationship(
        'Apartment', 
        back_populates='complex'
    )
    
    residents = relationship(
        'People', 
        back_populates='complex'
    )

    vehicles = relationship(
        'Vehicle', 
        back_populates='complex'
    )


