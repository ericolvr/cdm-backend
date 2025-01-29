""" People Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.domain.model.people import People
from app.domain.model.complex import Complex
from app.domain.model.apartment import Apartment


class PeopleRepository:
    """ People Repository """

    def __init__(self, db: Session):
        self.db = db


    async def create_people(self, people: People) -> People:
        """ Create people """

        self.db.add(people)
        self.db.commit()
        self.db.refresh(people)
        return people
    

    async def get_all_peoples(self) -> List[People]:
        """ get Peoples """

        peoples = (
            self.db.query(People)
            .options(
                joinedload(People.complex)
                .load_only(Complex.name),
                joinedload(People.apartment)
                .load_only(Apartment.apartment_number)
            )
        ).all()
        return peoples


    async def get_people_by_id(self, id: int) -> People:
        """ Get People by id """
        
        people = self.db.query(People).filter(
            People.id == id
        ).first()
        
        if not people:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'People id {id} not found'
            )
        return people
    
    
    async def get_people_by_complex_apartment(
            self, 
            complex: 
            int, apartment: int
        ) -> List[People]:
        """ Get People by complex and apartment """
        
        peoples = self.db.query(People).filter(
            People.complex_id == complex,
            People.apartment_id == apartment
        ).all()
        
        return peoples
    

    async def update_by_id(self, id: int, new_data) -> People:
        """ Update peoplew by id """
        
        result = await self.get_people_by_id(id)
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result

    
    
    