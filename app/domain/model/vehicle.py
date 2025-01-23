""" Vehicle model """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Vehicle(Base):
    __tablename__ = 'vehicles'
    
    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(50))
    model = Column(String(50))
    plate = Column(String(9), nullable=True)
    
    complex_id = Column(
        Integer, 
        ForeignKey('complexes.id'), 
        nullable=True
    )

    apartment_id = Column(
        Integer, 
        ForeignKey('apartments.id'), 
        nullable=True
    )

    complex = relationship(
        'Complex', 
        back_populates='vehicles', 
        lazy='joined'
    )
    
    apartment = relationship(
        'Apartment', 
        back_populates='vehicles', 
        lazy='joined'
    )




