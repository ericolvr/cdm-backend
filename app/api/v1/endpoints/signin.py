""" Signin Routes """
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.signin import SigninInput
from app.services.signin_service import SigninService


signin_routes = APIRouter(
    prefix='/api/v1/signin',
    tags=['Sign In']
)


@signin_routes.post('/token', status_code=status.HTTP_201_CREATED)
def signin(data: SigninInput, database: Session = Depends(get_database)):
    """ Create People Token """
    
    signin_service = SigninService(database)
    return signin_service.validate_user(data)