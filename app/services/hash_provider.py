""" hashs for user """
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class HashProvider:
    @staticmethod
    def make_hash(password):
        """ Make Hash to User Password """

        return pwd_context.hash(password)


    @staticmethod
    def verify_hash(password, user_hash):
        """ Verify Hash to Generate User Token """
        
        return pwd_context.verify(password, user_hash)