""" Apartment Repository """
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.domain.model.apartment import Apartment
from app.domain.model.complex import Complex
from app.domain.model.people import People

class ApartmentRepository:
    """ Apartment repository"""
    
    def __init__(self, db: Session):
        self.db = db


    async def create_apartment(self, apartment: Apartment) -> Apartment:
        """ Create apartment """
        
        self.db.add(apartment)
        self.db.commit()
        self.db.refresh(apartment)
        return apartment
    
    
    async def get_all_apartments(self) -> List[Apartment]:
        """ Get All Apartments """
        
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
        

    async def get_apartments_by_tower(self, number: int) -> Apartment:
        """ Get Apartments By Tower """
        
        apartments = self.db.query(Apartment).filter(
            Apartment.complex_id == number
        ).all()
        return apartments
    

    async def get_apartment_by_id(self, id: int) -> Apartment:
        """ Get apartment by id """
        
        apartment = self.db.query(Apartment).filter(Apartment.id == id).first()
        
        if not apartment:
            raise HTTPException(
                status_code=404, detail=f'Apartment {id} not found'
            )
        return apartment
    

    async def update_by_id(self, id: int, new_data) -> Apartment:
        """ Update Apartment By Id id """
        
        result = await self.get_apartment_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result