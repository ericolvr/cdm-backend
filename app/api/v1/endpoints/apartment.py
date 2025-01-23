""" Apartment routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.apartment import ApartmentCreate, ApartmentUpdate
from app.services.apartment_service import ApartmentService


apartment_routes = APIRouter(
    prefix='/api/v1/apartments',
    tags=['Apartments']
)


@apartment_routes.post('/', status_code=201)
def create_apartment(
    apartment: ApartmentCreate, 
    database: Session = Depends(get_database)
):
    apartment_service = ApartmentService(database)
    return apartment_service.create_apartmemt(apartment)


@apartment_routes.get('/')
def get_all_apartments(database: Session = Depends(get_database)):
    apartment_service = ApartmentService(database)
    return apartment_service.get_all_apartments()


@apartment_routes.get('/tower/{number}')
def get_apartments_by_tower(
        number: str, 
        database: Session = Depends(get_database)
):
    apartment_service = ApartmentService(database)
    return apartment_service.get_apartments_by_tower(number)


@apartment_routes.get('/id')
def get_apartment_by_id(
        id: str, 
        database: Session = Depends(get_database)
):
    apartment_service = ApartmentService(database)
    return apartment_service.get_apartment_by_id(id)


@apartment_routes.patch('/update/{id}')
def update_by_id(
        id: int, 
        new_data: ApartmentUpdate, 
        database: Session = Depends(get_database)
):
    apartment_service = ApartmentService(database)
    return apartment_service.update_by_id(id, new_data)