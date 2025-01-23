""" Complex schema """
from pydantic import BaseModel
from typing import Optional


class ComplexCreate(BaseModel):
    """ Complex create schema """

    name: str
    floors: int
    apartments_by_floor: int


class ComplexUpdate(BaseModel):
    """ Complex update schema """

    name: Optional[str] = None
    floors: Optional[int] = None
    apartments_by_floor: Optional[int] = None
    