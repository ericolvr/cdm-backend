""" User Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from app.domain.model.user import User


class UserRepository:
    """ User Repository"""
    
    def __init__(self, db: Session):
        self.db = db


    async def create_user(self, user: User) -> User:
        """ Create User """
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    
    async def get_all_users(self) -> List[User]:
        """ Get All Users """
        
        users = self.db.query(User).all()
        return users
        

    async def get_user_by_mobile(self, mobile: str) -> User:
        """ Get User By Mobile """
        
        user = self.db.query(User).filter(User.mobile == mobile).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'User with mobile {mobile} not found'
            )
        return user
    

    async def get_user_by_id(self, id: int) -> User:
        """ Get user by id """
        
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'User with id {id} not found'
            )
        return user
    

    async def update_by_id(self, id: int, new_data) -> User:
        """ Update user by id """
        
        result = await self.get_user_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result