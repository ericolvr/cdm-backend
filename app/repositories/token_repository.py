""" Token Repository """
from fastapi import status, HTTPException
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
        
        exists = self.db.query(Token).filter(
            Token.mobile == mobile,
            Token.number == number,
        ).first()

        if not exists:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Token  for mobile number {mobile} not found'
            )
        
        return exists
    

    