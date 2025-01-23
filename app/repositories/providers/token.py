""" JWT Token generation """
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt
load_dotenv()


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
EXPIRES = os .getenv("EXPIRES")


class TokenProvider:
    """ Provide a token to authenticate user """

    @staticmethod
    def create_access_token(data: dict):
        """ Generate access_token """
        
        user_data = data.copy()
        expires = datetime.utcnow() + timedelta(hours=int(EXPIRES))

        user_data.update({"exp": expires})
        jwt_token = jwt.encode(
            user_data, SECRET_KEY, algorithm=ALGORITHM
        )
        return jwt_token

    @staticmethod
    def verify_access_token(token: str):
        """ Verify if is a valid token """
        
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload.get("sub")