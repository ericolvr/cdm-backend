""" Toekn Service """
import random
from sqlalchemy.orm import Session

from app.repositories.token_repository import TokenRepository
from app.schemas.token import TokenCreate
from app.domain.model.token import Token


class TokenService:
    """ Token Service """
    
    def __init__(self, db: Session):
        self.repository = TokenRepository(db)


    def create_token(self, mobile: str):
        """ Create Token """
    
        token = Token(
            mobile=mobile,
            number=self.generate_token(),
            used=False,
        )

        """
            Send message with token using background task
            Amazon SNS, Twilio ...
        """

        return self.repository.create_token(token)    
    
    
    def generate_token(self) -> int:
        """ Generate Token """

        number = random.randint(100000, 999999)
        return number


    def validate_user_token(self, mobile: str, number: int):
        """ Validate user token """
        
        return self.repository.validate_user_token(mobile, number)    
        