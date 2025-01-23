""" User routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.user import UserCreate, UserUpdate
from app.services.user_service import UserService


user_routes = APIRouter(
    prefix='/api/v1/users',
    tags=['Users']
)


@user_routes.post('/', status_code=201)
def create_user(
    user: UserCreate, 
    database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return user_service.create_user(user)


@user_routes.get('/')
def get_all_users(database: Session = Depends(get_database)):
    user_service = UserService(database)
    return user_service.get_all_users()


@user_routes.get('/mobile')
def get_user_by_mobile(
        mobile: str, 
        database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return user_service.get_user_by_mobile(mobile)


@user_routes.get('/id')
def get_user_by_id(
        id: str, 
        database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return user_service.get_user_by_id(id)


@user_routes.patch('/update/{id}')
def update_by_id(
        id: int, 
        new_data: UserUpdate, 
        database: Session = Depends(get_database)
):
    user_service = UserService(database)
    return user_service.update_by_id(id, new_data)