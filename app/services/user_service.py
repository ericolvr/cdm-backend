""" User Service """
from sqlalchemy.orm import Session

from app.repositories.user_repository import UserRepository
from app.domain.providers.hash import HashProvider
from app.schemas.user import UserCreate
from app.domain.model.user import User


class UserService:
    """ User Service """
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)


    async def create_user(self, user: UserCreate):
        """ Create User """
    
        user = User(
            name=user.name, 
            mobile=user.mobile, 
            role=user.role, 
            password=HashProvider.make_hash(user.password),
            status=user.status
        )
        return await self.repository.create_user(user)    
    
    
    async def get_all_users(self):
        """ Get All Users"""
    
        users = await self.repository.get_all_users()
        return users


    async def get_user_by_mobile(self, mobile: str):
        """ Get user by mobile """
    
        user = await self.repository.get_user_by_mobile(mobile)
        return user
    

    async def get_user_by_id(self, id: str):
        """ Get user by id """
    
        user = await self.repository.get_user_by_id(id)
        return user
    

    async def update_by_id(self, id: int, new_data):
        """ Update user by id """
    
        user = await self.repository.update_by_id(id, new_data)
        return user
    
