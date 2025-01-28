""" Token Repository """
from typing import List
from fastapi import status
from sqlalchemy.orm import Session
from app.domain.model.token import Token


class TokenRepository:
    """ Token repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def create_token(self, token: Token) -> Token:
        """ Create token """
        
        self.db.add(token)
        self.db.commit()
        self.db.refresh(token)
        return token
            

    def validate_user_token(self, mobile: str, number: int) -> Token:
        """ Validate user token """
        
        result = self.db.query(Token).filter(
            Token.mobile == mobile,
            Token.number == number,
        ).first()

        if not result:
            message = {
                f'Token for {mobile} is invalid',
                status.HTTP_404_NOT_FOUND
            }
            return message
        return result
    

    