""" Reservation schema """
from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReservationCreate(BaseModel):
    """ Reservation create schema """

    place_id: int
    people_id: int
    reservation_date: date
    


class ReservationUpdate(BaseModel):
    """ Reservation update schema """

    place_id: Optional[int] = None
    people_id: Optional[int] = None
    reservation_date: Optional[str] = None