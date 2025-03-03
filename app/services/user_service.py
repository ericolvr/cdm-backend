""" User Service """
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks

from app.repositories.user_repository import UserRepository
from app.domain.providers.hash import HashProvider
from app.schemas.user import UserCreate
from app.domain.model.user import User
from app.domain.model.user import User
from app.services.token_service import TokenService


class UserService:
    """ User Service """
    
    def __init__(self, db: Session):
        self.repository = UserRepository(db)
        self.token_service = TokenService(db)


    async def create_user(self, user: UserCreate, background_tasks: BackgroundTasks):
        """ Create User """
    
        user = User(
            name=user.name, 
            mobile=user.mobile, 
            role=user.role, 
            password=HashProvider.make_hash(user.password),
            status=user.status
        )

        # Add the create_token task to the background tasks
        background_tasks.add_task(self.token_service.create_token, user.mobile)

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
    
