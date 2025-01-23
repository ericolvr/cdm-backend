""" User schema """
from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    """ User create schema """

    name: str
    mobile: str
    role: str
    password: str
    status: bool


class UserResponse(BaseModel):
    """ User response schema """

    id: int
    name: str
    mobile: str
    role: str
    status: bool


class UserUpdate(BaseModel):
    """ User update schema """

    name: Optional[str] = None
    mobile: Optional[str] = None
    role:  Optional[int] = None
    password:  Optional[str] = None
    status:  Optional[bool] = None


