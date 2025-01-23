""" People schema """
from pydantic import BaseModel
from typing import Optional


class PeopleCreate(BaseModel):
    """ People create schema """

    name: str
    document: str
    picture: Optional[str] = None
    complex_id: str
    apartment_id: str


class PeopleUpdate(BaseModel):
    """ People update schema """

    name: Optional[str] = None
    document: Optional[str] = None
    people: Optional[str] = None
    picture: Optional[str] = None
    complex_id: Optional[str] = None
    apartment_id: Optional[str] = None