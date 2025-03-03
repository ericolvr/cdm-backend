""" Authorization Routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.authorization import AuthorizationCreate, AuthorizationUpdate
from app.services.authorization_service import AuthorizationService


authorization_routes = APIRouter(
    prefix='/api/v1/authorizations',
    tags=['Authorizations']
)


@authorization_routes.post('/', status_code=201)
async def create_authorization(
    authorization: AuthorizationCreate, 
    database: Session = Depends(get_database)
):
    authorization_service = AuthorizationService(database)
    return await authorization_service.create_authorization(authorization)


@authorization_routes.get('/')
async def get_all_authorizations(database: Session = Depends(get_database)):
    authorization_service = AuthorizationService(database)
    return await authorization_service.get_all_authorizations()


@authorization_routes.get('/id')
async def get_authorization_by_id(
        id: str, 
        database: Session = Depends(get_database)
):
    authorization_service = AuthorizationService(database)
    return await authorization_service.get_authorization_by_id(id)


@authorization_routes.patch('/update/{id}')
async def update_by_id(
        id: int, 
        new_data: AuthorizationUpdate, 
        database: Session = Depends(get_database)
):
    authorization_service = AuthorizationService(database)
    return await authorization_service.update_by_id(id, new_data)