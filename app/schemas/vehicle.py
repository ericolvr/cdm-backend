""" Vehicle schema """
from pydantic import BaseModel
from typing import Optional


class VehicleCreate(BaseModel):
    """ Vehicle create schema """

    brand: str
    model: str
    plate: str
    complex_id: int
    apartment_id: int


class VehicleUpdate(BaseModel):
    """ Vehicle update schema """

    brand: Optional[str] = None
    model: Optional[str] = None
    plate: Optional[str] = None
    complex_id: Optional[int] = None
    apartment_id: Optional[int] = None
