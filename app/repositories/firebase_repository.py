""" Firebase Repository """
from typing import List
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.domain.model.people import People


class FirebaseRepository:
    """ Firebase Repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def get_mobile_number(self, mobile: str):
        """ Get Mobile Number """
        
        number = self.db.query(People).filter(People.mobile == mobile).first()
        if not number:
            raise HTTPException(
                status_code=404, detail=f'Mobile {mobile} not found'
            )
        
        return number
