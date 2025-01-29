""" Complex Routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.complex import ComplexCreate, ComplexUpdate
from app.services.complex_service import ComplexService


complex_routes = APIRouter(
    prefix='/api/v1/complexes',
    tags=['Complexes']
)


@complex_routes.post('/', status_code=201)
async def create_complex(
    complex: ComplexCreate, 
    database: Session = Depends(get_database)
):
    complex_service = ComplexService(database)
    return await complex_service.create_complex(complex)


@complex_routes.get('/')
async def get_all_complxes(database: Session = Depends(get_database)):
    complex_service = ComplexService(database)
    return await complex_service.get_all_complexes()


@complex_routes.get('/id')
async def get_complex_by_id(
        id: str, 
        database: Session = Depends(get_database)
):
    complex_service = ComplexService(database)
    return await complex_service.get_complex_by_id(id)


@complex_routes.patch('/update/{id}')
async def update_by_id(
        id: int, 
        new_data: ComplexUpdate, 
        database: Session = Depends(get_database)
):
    complex_service = ComplexService(database)
    return await complex_service.update_by_id(id, new_data)