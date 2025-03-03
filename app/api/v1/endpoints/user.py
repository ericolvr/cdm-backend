""" User routes """
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from fastapi import BackgroundTasks

from app.core.database import get_database
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService


user_routes = APIRouter(
    prefix='/api/v1/users',
    tags=['Users']
)


@user_routes.post('/', status_code=201)
async def create_user(
    user: UserCreate, 
    background_tasks: BackgroundTasks,
    database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return await user_service.create_user(user, background_tasks)


@user_routes.get('/')
async def get_all_users(database: Session = Depends(get_database)):
    user_service = UserService(database)
    return await user_service.get_all_users()


@user_routes.get('/mobile')
async def get_user_by_mobile(
    mobile: str, 
    database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return await user_service.get_user_by_mobile(mobile)


@user_routes.get('/id')
async def get_user_by_id(
    id: str, 
    database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return await user_service.get_user_by_id(id)


@user_routes.patch('/update/{id}')
async def update_by_id(
    id: int, 
    new_data: UserUpdate, 
    database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return await user_service.update_by_id(id, new_data)