""" Token routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.services.token_service import TokenService


token_routes = APIRouter(
    prefix='/api/v1/token',
    tags=['Token']
)


@token_routes.post('/', status_code=200)
def validate_user_token(
    mobile: str,
    number: int,
    database: Session = Depends(get_database)
):
    token_service = TokenService(database)
    return token_service.validate_user_token(mobile, number)
