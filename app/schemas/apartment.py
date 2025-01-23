""" Apartment schema """
from pydantic import BaseModel
from typing import Optional


class ApartmentCreate(BaseModel):
    """ Apartment create schema """

    complex_id: str
    apartment_number: str


class ApartmentUpdate(BaseModel):
    """ apartment update schema """

    complex_id: Optional[str] = None
    apartment_number: Optional[str] = None
    