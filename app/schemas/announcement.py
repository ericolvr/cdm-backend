""" Announcement schema """
from pydantic import BaseModel
from typing import Optional


class AnnouncementCreate(BaseModel):
    """ Announcement create schema """

    type: str
    title: str
    description: str


class AnnouncementUpdate(BaseModel):
    """ Announcement update schema """

    type: Optional[int] = None
    title: Optional[str] = None
    description: Optional[int] = None
    