""" Place schema """
from pydantic import BaseModel
from typing import Optional


class PlaceCreate(BaseModel):
    """ Place create schema """

    name: str
    price: float
    description: Optional[str] = None


class PlaceUpdate(BaseModel):
    """ Place update schema """

    name: Optional[str] = None
    price: Optional[float] = None
    description: Optional[str] = None