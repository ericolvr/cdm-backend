""" People model """
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class People(Base):
    __tablename__ = 'peoples'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    document = Column(String(20), nullable=True)
    mobile = Column(String(20), nullable=True)
    picture = Column(String(100), nullable=True)
    status = Column(Boolean, default=False)

    complex_id = Column(
        Integer, 
        ForeignKey('complexes.id'), 
        nullable=True)
    
    apartment_id = Column(
        Integer, 
        ForeignKey('apartments.id'), 
        nullable=True
    )

    complex = relationship(
        'Complex', 
        back_populates='residents', 
        lazy='joined'
    )
    
    apartment = relationship(
        'Apartment', 
        back_populates='residents', 
        lazy='joined'
    )

    reservations = relationship(
        'Reservation', 
        back_populates='people', 
        lazy='joined'
    )


from app.domain.model.reservation import Reservation