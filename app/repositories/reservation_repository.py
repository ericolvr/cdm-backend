""" Reservation Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.domain.model.reservation import Reservation


class ReservationRepository:
    """ Reservation Repository """

    def __init__(self, db: Session):
        self.db = db


    async def create_reservation(self, reservation: Reservation) -> Reservation:
        """ Create Reservation """

        self.db.add(reservation)
        self.db.commit()
        self.db.refresh(reservation)
        return reservation
    

    async def get_all_reservations(self) -> List[Reservation]:
        """ get Reservations """

        reservations = self.db.query(Reservation).all()
        return reservations


    async def get_reservation_by_id(self, id: int) -> Reservation:
        """ Get Reservation by id """
        
        reservation = self.db.query(Reservation).filter(
            Reservation.id == id
        ).first()
        
        if not reservation:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Reservation id {id} not found'
            )
        return reservation
    

    async def update_by_id(self, id: int, new_data) -> Reservation:
        """ Update reservation by id """
        
        result = await self.get_people_by_id(id)
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result

    
    
    