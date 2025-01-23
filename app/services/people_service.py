""" People Service """
from sqlalchemy.orm import Session

from app.repositories.people_repository import PeopleRepository
from app.schemas.people import PeopleCreate
from app.domain.model.people import People


class PeopleService:
    """ People service """
    
    def __init__(self, db: Session):
        self.repository = PeopleRepository(db)


    def create_people(self, people: PeopleCreate):
        """ Create people """

        people = People(
            name=people.name,
            document=people.document,
            picture=people.picture,
            complex_id=people.complex_id,
            apartment_id=people.apartment_id
        )
        return self.repository.create_people(people)
    

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


    
