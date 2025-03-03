""" Authorization schema """
from pydantic import BaseModel
from typing import Optional
from datetime import date


class AuthorizationCreate(BaseModel):
    """ Authorization create schema """

    type: int
    name: str
    document: str
    authorization_date: date
    hour_start: str
    hour_end: str


class AuthorizationUpdate(BaseModel):
    """ Authorization create schema """

    type: Optional[int] = None
    name: Optional[str] = None
    document: Optional[str] = None
    authorization_date: Optional[date] = None
    hour_start: Optional[str] = None
    hour_end: Optional[str] = None

