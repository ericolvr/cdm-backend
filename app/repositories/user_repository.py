""" User Repository """
from typing import List
from fastapi import status
from sqlalchemy.orm import Session
from app.domain.model.user import User


class UserRepository:
    """ User repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def create_user(self, user: User) -> User:
        """ Create user """
        
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
    
    
    def get_all_users(self) -> List[User]:
        """ get all users """
        
        users = self.db.query(User).all()
        return users
        

    def get_user_by_mobile(self, mobile: str) -> User:
        """ Get user by mobile """
        
        user = self.db.query(User).filter(User.mobile == mobile).first()
        if not user:
            message = {
                f'User {mobile} not found',
                status.HTTP_404_NOT_FOUND
            }
            return message
        return user
    

    def get_user_by_id(self, id: int) -> User:
        """ Get user by id """
        
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            message = {
                f'User {id} not found',
                status.HTTP_404_NOT_FOUND
            }
            return message
        return user
    

    def update_by_id(self, id: int, new_data) -> User:
        """ Update user by id """
        
        result = self.get_user_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result