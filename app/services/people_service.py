""" People Service """
import os
import base64
from uuid import uuid4
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.repositories.people_repository import PeopleRepository
from app.schemas.people import PeopleCreate
from app.domain.model.people import People

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class PeopleService:
    """ People service """
    
    def __init__(self, db: Session):
        self.repository = PeopleRepository(db)


    def create_people(self, people: PeopleCreate):
        """ Create people """

        try:
            image_data = base64.b64decode(people.picture)
            file_name = f"{uuid4()}.png"
            file_path = os.path.join(UPLOAD_FOLDER, file_name)

            with open(file_path, 'wb') as f:
                f.write(image_data)
            
            people.picture = file_path
            people = People(
                name=people.name,
                document=people.document,
                picture=people.picture,
                complex_id=people.complex_id,
                apartment_id=people.apartment_id
            )
            return self.repository.create_people(people)
        
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"Error saving image: {str(e)}")

    

    def get_all_peoples(self):
        """ Get all peoples """

        peoples = self.repository.get_all_peoples()
        return peoples


    def get_people_by_id(self, id: str):
        """ Get people by id """

        people = self.repository.get_people_by_id(id)
        return people
    

    def update_by_id(self, id: int, new_data):
        """ Update people by id """
    
        people = self.repository.update_by_id(id, new_data)
        return people


    
