""" User Service """
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.repositories.providers.hash import HashProvider
from app.schemas.user import UserCreate
from app.domain.model.user import User


class UserService:
    """ User service """
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)


    def create_user(self, user: UserCreate):
        """ Create User """
    
        user = User(
            name=user.name, 
            mobile=user.mobile, 
            role=user.role, 
            password=HashProvider.make_hash(user.password),
            status=user.status
        )
        return self.repository.create_user(user)    
    
    
    def get_all_users(self):
        """ Get all users"""
    
        users = self.repository.get_all_users()
        return users


    def get_user_by_mobile(self, mobile: str):
        """ Get user by mobile """
    
        user = self.repository.get_user_by_mobile(mobile)
        return user
    

    def get_user_by_id(self, id: str):
        """ Get user by id """
    
        user = self.repository.get_user_by_id(id)
        return user
    

    def update_by_id(self, id: int, new_data):
        """ Update user by id """
    
        user = self.repository.update_by_id(id, new_data)
        return user
    
