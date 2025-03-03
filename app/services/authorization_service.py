""" Authorization Service """
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.domain.model.authorization import Authorization
from app.schemas.authorization import AuthorizationCreate
from app.repositories.authorization_repository import AuthorizationRepository



class AuthorizationService:
    """ Authorization service """
    
    def __init__(self, db: Session):
        self.repository = AuthorizationRepository(db)
        self.database = db


    def create_authorization(self, authorization: AuthorizationCreate):
        """ Create Authorization """

        if authorization.type == 1:
            picture = 10
        
        authorization = Authorization(
            type=authorization.type,
            name=authorization.name,
            authorization_date=authorization.authorization_date,
            hour_start=authorization.hour_start,
            hour_end=authorization.hour_end,
        )

        return self.repository.create_authorization(authorization)


    def get_all_authorizations(self):
        """ Get all authorizations """

        authorizations = self.repository.get_all_authorizations()
        return authorizations


    def get_authorization_by_id(self, id: str):
        """ Get authorization by id """

        authorization = self.repository.get_authorization_by_id(id)
        return authorization


    def update_by_id(self, id: int, new_data):
        """ Update authorization by id """
    
        authorization = self.repository.update_by_id(id, new_data)
        return authorization

