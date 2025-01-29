""" People Service """
import os
import base64
from uuid import uuid4
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks

from app.domain.model.people import People
from app.schemas.people import PeopleCreate
from app.repositories.people_repository import PeopleRepository
from app.services.token_service import TokenService


class PeopleService:
    """ People Service """
    
    def __init__(self, db: Session):
        self.repository = PeopleRepository(db)
        self.database = db


    async def create_people(self, people: PeopleCreate, background_tasks: BackgroundTasks):
        """ Create People """

        if people.picture:
            picture = self.process_image(people.picture)
        else:
            picture = ''

        people = People(
            complex_id=people.complex_id,
            apartment_id=people.apartment_id,
            name=people.name,
            document=people.document,
            mobile=people.mobile,
            picture=picture
        )
        
        background_tasks.add_task(
            TokenService(self.database).create_token, people.mobile
        )

        return await self.repository.create_people(people)


    async def get_all_peoples(self):
        """ Get All People """

        peoples = await self.repository.get_all_peoples()
        return peoples


    async def get_people_by_id(self, id: str):
        """ Get People By Id """

        people = await self.repository.get_people_by_id(id)
        return people
    

    async def get_people_by_complex_apartment(self, complex, apartment):
        """ Get people complex and apartment """

        peoples = await self.repository.get_people_by_complex_apartment(complex, apartment)
        return peoples
    

    async def update_by_id(self, id: int, new_data):
        """ Update people by id """
    
        people = await self.repository.update_by_id(id, new_data)
        return people


    async def process_image(self, picture: str):
        """ Process image """

        # TODO: Should be use a S3 Bucket
        FOLDER = 'uploads'
        os.makedirs(FOLDER, exist_ok=True)
        
        try:
            data = base64.b64decode(picture)
            name = f'{uuid4()}.png'
            path = os.path.join(FOLDER, name)
            
            with open(path, 'wb') as f:
                f.write(data)
            picture = path
            return picture
        
        except Exception as e:
            raise HTTPException(
                status_code=400, detail=f'Error saving image: {str(e)}'
            )
