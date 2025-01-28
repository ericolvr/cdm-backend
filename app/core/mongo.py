""" Database configuration """
import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()


USER = os.environ.get('MONGO_USERNAME')
PWD = os.environ.get('MONGO_PASSWORD')
HOST = os.environ.get('MONGO_HOST')
PORT = os.environ.get('MONGO_PORT')
DB = os.environ.get('MONGO_DATABASE')

MONGO_URI = f'mongodb://{USER}:{PWD}@{HOST}:{PORT}/{DB}'

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[DB]


def get_mongo_database():
    """ Get MongoDB connection """
    try:
        yield mongo_db
    finally:
        mongo_client.close()
