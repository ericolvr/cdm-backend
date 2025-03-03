""" Reservation Service """
from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.domain.model.reservation import Reservation
from app.schemas.reservation import ReservationCreate, ReservationUpdate
from app.repositories.reservation_repository import ReservationRepository


class ReservationService:
    """ Reservation service """
    
    def __init__(self, db: Session):
        self.repository = ReservationRepository(db)
        self.database = db


    def create_reservation(self, reservation: ReservationCreate):
        """ Create Reservation """

        reservation = Reservation(
            people_id=reservation.people_id,
            place_id=reservation.place_id,
            reservation_date=reservation.reservation_date
        )

        return self.repository.create_reservation(reservation)


    def get_all_reservations(self):
        """ Get all reservations """

        reservations = self.repository.get_all_reservations()
        return reservations


    def get_reservation_by_id(self, id: str):
        """ Get reservation by id """

        reservation = self.repository.get_reservation_by_id(id)
        return reservation
        

    def update_by_id(self, id: int, new_data):
        """ Update reservation by id """
    
        reservation = self.repository.update_by_id(id, new_data)
        return reservation
