""" Placle Service """
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.domain.model.place import Place
from app.schemas.place import PlaceCreate, PlaceUpdate
from app.repositories.place_repository import PlaceRepository



class PlaceService:
    """ Place service """
    
    def __init__(self, db: Session):
        self.repository = PlaceRepository(db)
        self.database = db


    def create_place(self, place: PlaceCreate):
        """ Create place """

        place = Place(
            name=place.name,
            price=place.price,
            description=place.description
        )

        return self.repository.create_place(place)


    def get_all_places(self):
        """ Get all places """

        places = self.repository.get_all_places()
        return places


    def get_place_by_id(self, id: str):
        """ Get place by id """

        place = self.repository.get_place_by_id(id)
        return place
    

    def update_by_id(self, id: int, new_data):
        """ Update place by id """
    
        place = self.repository.update_by_id(id, new_data)
        return place

