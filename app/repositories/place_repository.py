""" Place Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.domain.model.place import Place


class PlaceRepository:
    """ Place Repository """

    def __init__(self, db: Session):
        self.db = db


    async def create_place(self, place: Place) -> Place:
        """ Create place """

        self.db.add(place)
        self.db.commit()
        self.db.refresh(place)
        return place
    

    async def get_all_places(self) -> List[Place]:
        """ get Places """

        places = (
            self.db.query(Place)
            .order_by(Place.name)
        ).all()
        return places


    async def get_place_by_id(self, id: int) -> Place:
        """ Get Place by id """
        
        place = self.db.query(Place).filter(
            Place.id == id
        ).first()
        
        if not place:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Place id {id} not found'
            )
        return place
        

    async def update_by_id(self, id: int, new_data) -> Place:
        """ Update place by id """
        
        result = await self.get_place_by_id(id)
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result

    
    
    