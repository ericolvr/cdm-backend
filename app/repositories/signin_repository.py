""" Signin Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.domain.model.authorization import Authorization


class SigninRepository:
    """ SignIn Repository """

    def __init__(self, db: Session):
        self.db = db

    

    def validate_people(self) -> List[Authorization]:
        """ Validate Login Data From Peoples """

        people = 


        

