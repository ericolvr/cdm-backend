""" jwt token """
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from jose import jwt
load_dotenv()


# SECRET_KEY = os.getenv("SECRET_KEY")
# ALGORITHM = os.getenv("ALGORITHM")
# EXPIRES = os .getenv("EXPIRES")

# HASH
SECRET_KEY='super_secret'
ALGORITHM='HS256'
EXPIRES=120


class TokenProvider:
    """provide token to authenticate user"""

    @staticmethod
    def create_access_token(data: dict):
        """generate access_token"""
        
        user_data = data.copy()
        expires = datetime.utcnow() + timedelta(hours=int(EXPIRES))

        user_data.update({"exp": expires})
        jwt_token = jwt.encode(
            user_data, SECRET_KEY, algorithm=ALGORITHM
        )
        return jwt_token

    @staticmethod
    def verify_access_token(token: str):
        """verify if is a valid token"""
        
        payload = jwt.decode(
            token, SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload.get("sub")