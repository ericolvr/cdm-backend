""" Vehicle routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.vehicle import VehicleCreate, VehicleUpdate
from app.services.vehicle_service import VehicleService


vehicle_routes = APIRouter(
    prefix='/api/v1/vehicles',
    tags=['Vehicles']
)


@vehicle_routes.post('/', status_code=201)
def create_vehicle(
    vehicle: VehicleCreate, 
    database: Session = Depends(get_database)
):
    vehicle_service = VehicleService(database)
    return vehicle_service.create_vehicle(vehicle)


@vehicle_routes.get('/')
def get_vehicles(database: Session = Depends(get_database)):
    vehicle_service = VehicleService(database)
    return vehicle_service.get_vehicles()


@vehicle_routes.get('/complex/{complex}/apartment/{apartment}')
def get_vehicle_by_complex_apartment(
    complex: int, 
    apartment: int, 
    database: Session = Depends(get_database)
):
    vehicle_service = VehicleService(database)
    return vehicle_service.get_vehicle_by_complex_apartment(complex, apartment)


@vehicle_routes.patch('/update/{id}')
def update_by_id(
        id: int, 
        new_data: VehicleUpdate, 
        database: Session = Depends(get_database)
):
    vehicle_service = VehicleService(database)
    return vehicle_service.update_by_id(id, new_data)