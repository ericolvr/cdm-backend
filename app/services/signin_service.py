""" Signin Service """
from fastapi import status
from sqlalchemy.orm import Session

from app.repositories.people_repository import PeopleRepository
from app.schemas.signin import SigninInput
from app.services.hash_provider import HashProvider
from app.services.token_provider import TokenProvider

class SigninService:
    """ Signin Service """
    
    def __init__(self, db: Session):
        self.repository = PeopleRepository(db)
        self.database = db


    def validate_user(self, signin: SigninInput):
        """ Create Token """

        
        people = self.repository.get_people_by_mobile(signin.mobile)
        password = HashProvider.verify_hash(signin.password, people.password)
        print(people.password, 'weqweqeqw')

        if not password:
            message = {
                "detail": "Invalid credentials",
                "status_code": status.HTTP_401_UNAUTHORIZED,
            }
            return message
        
        token = TokenProvider.create_access_token({'sub': people.mobile})
        return {
            'name': people.name,
            'mobile': people.mobile,
            'access_token': token,
            'complex_id': people.complex_id,
            'apartment_id': people.apartment_id,
            'role': "0",
            'user_id': people.id
        }

        