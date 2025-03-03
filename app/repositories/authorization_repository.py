""" Authorization Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.domain.model.authorization import Authorization


class AuthorizationRepository:
    """ Authorization Repository """

    def __init__(self, db: Session):
        self.db = db


    async def create_authorization(self, authorization: Authorization) -> Authorization:
        """ Create Authorization """

        self.db.add(authorization)
        self.db.commit()
        self.db.refresh(authorization)
        return authorization
    

    async def get_all_authorizations(self) -> List[Authorization]:
        """ get Peoples """

        authorizations = (
            self.db.query(Authorization)
        ).all()
        return authorizations


    async def get_authorization_by_id(self, id: int) -> Authorization:
        """ Get Authorization by id """
        
        authorization = self.db.query(Authorization).filter(
            Authorization.id == id
        ).first()
        
        if not authorization:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Authorization id {id} not found'
            )
        return authorization   

    async def update_by_id(self, id: int, new_data) -> Authorization:
        """ Update authorization by id """
        
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

    
    
    