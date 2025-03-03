""" Reservation Routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.reservation import ReservationCreate, ReservationUpdate
from app.services.reservation_service import ReservationService


reservation_routes = APIRouter(
    prefix='/api/v1/reservations',
    tags=['Reservations']
)

@reservation_routes.post('/', status_code=201)
async def create_reservation(
    reservation: ReservationCreate, 
    database: Session = Depends(get_database),
):
    reservation_service = ReservationService(database)
    return await reservation_service.create_reservation(reservation)


@reservation_routes.get('/')
async def get_all_reservations(database: Session = Depends(get_database)):
    reservation_service = ReservationService(database)
    return await reservation_service.get_all_reservations()


@reservation_routes.get('/id')
async def get_reservation_by_id(id: str, database: Session = Depends(get_database)):
    reservation_service = ReservationService(database)
    return await  reservation_service.get_reservation_by_id(id)


@reservation_routes.patch('/update/{id}')
async def update_by_id(
        id: int, 
        new_data: ReservationUpdate, 
        database: Session = Depends(get_database)
):
    reservation_service = ReservationService(database)
    return await reservation_service.update_by_id(id, new_data)
