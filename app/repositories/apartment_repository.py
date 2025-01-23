""" Apartment Repository """
from typing import List
from fastapi import status
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.domain.model.apartment import Apartment
from app.domain.model.complex import Complex
from app.domain.model.people import People

class ApartmentRepository:
    """ Apartment repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def create_apartment(self, apartment: Apartment) -> Apartment:
        """ Create apartment """
        
        self.db.add(apartment)
        self.db.commit()
        self.db.refresh(apartment)
        return apartment
    
    
    def get_all_apartments(self) -> List[Apartment]:
        """ Get all apartments """
        
        apartments = (
            self.db.query(Apartment)
            .options(
                joinedload(Apartment.complex)
                .load_only(Complex.name),
                joinedload(Apartment.residents)
                .load_only(People.name, People.document)
            )
        ).all()
        return apartments
        

    def get_apartments_by_tower(self, number: int) -> Apartment:
        """ Get apartments by tower """
        
        apartments = self.db.query(Apartment).filter(
            Apartment.complex_id == number
        ).all()
        return apartments
    

    def get_apartment_by_id(self, id: int) -> Apartment:
        """ Get apartment by id """
        
        apartment = self.db.query(apartment).filter(Apartment.id == id).first()
        if not apartment:
            message = {
                f'apartment {id} not found',
                status.HTTP_404_NOT_FOUND
            }
            return message
        return apartment
    

    def update_by_id(self, id: int, new_data) -> Apartment:
        """ Update apartment by id """
        
        result = self.get_apartment_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result