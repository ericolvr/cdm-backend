""" Firebase Service """
from sqlalchemy.orm import Session
import firebase_admin
from firebase_admin import credentials, auth

from app.repositories.firebase_repository import FirebaseRepository


cred = credentials.Certificate('condowebchat-firebase-adminsdk-fbsvc-f741696d93.json')
firebase_admin.initialize_app(cred)


class FirebaseService:
    """ Firebase Service """

    def __init__(self, db: Session):
        self.repository = FirebaseRepository(db)
        self.database = db


    def generate_firebase_token(self, mobile: str):
        """ Create Firebase Token """

        number = self.verify_mobile_number(mobile)
        if not number:
            return
    
        return  auth.create_custom_token(mobile).decode('utf-8')
    

    def verify_mobile_number(self, mobile: str):
        """ Verify Mobile Number """
        
        return self.repository.get_mobile_number(mobile)
    
    
        