""" Token schema """
from pydantic import BaseModel


class TokenCreate(BaseModel):
    """ Token create schema """

    mobile: str



