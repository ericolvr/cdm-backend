''' Apartment model '''
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.core.database import Base


class Apartment(Base):
    __tablename__ = 'apartments'
    
    id = Column(Integer, primary_key=True, index=True)
    complex_id = Column(
        Integer, 
        ForeignKey('complexes.id')
    )

    apartment_number = Column(Integer)
    
    complex = relationship(
        'Complex', 
        back_populates='apartments'
    )
    
    residents = relationship(
        'People', 
        back_populates='apartment'
    )

    vehicles = relationship(
        'Vehicle', 
        back_populates='apartment'
    )
