""" signin schema """
from pydantic import BaseModel
from typing import Optional


class SigninInput(BaseModel):
    """ Signin Input """

    mobile: str
    password: str


class SigninOutput(BaseModel):
    """ Responde data """

    mobile: str
    password: str
    token: Optional[str] = None

    