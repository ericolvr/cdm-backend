""" Firebase Routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.services.firebase_service import FirebaseService


firebase_routes = APIRouter(
    prefix='/api/v1/firebase',
    tags=['Firebase']
)

@firebase_routes.get('/', status_code=201)
def create_firebase_token(
    mobile: str,
    database: Session = Depends(get_database),
):
    firebase_service = FirebaseService(database)
    return firebase_service.generate_firebase_token(mobile)

