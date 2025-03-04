""" People schema """
from pydantic import BaseModel
from typing import Optional


class PeopleCreate(BaseModel):
    """ People create schema """

    complex_id: int
    apartment_id: int
    name: str
    document: str
    mobile: Optional[str] = None
    picture: Optional[str] = None
    status: Optional[bool] = False
    password: str


class PeopleUpdate(BaseModel):
    """ People update schema """

    name: Optional[str] = None
    document: Optional[str] = None
    people: Optional[str] = None
    picture: Optional[str] = None
    complex_id: Optional[str] = None
    apartment_id: Optional[str] = None
    status: Optional[bool] = False
    password: Optional[str] = None