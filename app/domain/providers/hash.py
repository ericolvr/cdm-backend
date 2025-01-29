""" Hashing user password """
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


class HashProvider:
    """ Make hashs from user password """

    @staticmethod
    def make_hash(password):
        """ Hash password """
        return pwd_context.hash(password)

    @staticmethod
    def verify_hash(password, user_hash):
        """ Verify hash from password """
        return pwd_context.verify(password, user_hash)