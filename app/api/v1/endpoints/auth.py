""" authentication service middleware """
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.services.token_provider import TokenProvider
from app.repositories.people_repository import PeopleRepository


oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')


def get_logged_user(
        token: str = Depends(oauth2_schema),
        database: Session = Depends(get_database)
):
    """ Get logged user """

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Invalid data',
    )

    try:
        mobile = TokenProvider().verify_access_token(token)
    except JWTError:
        raise exception
    
    if not mobile:
        raise exception
        
    
    people = PeopleRepository(database).get_people_by_mobile(mobile)
    if not people:
        return people
