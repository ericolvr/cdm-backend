""" Database configuration """
import os
from dotenv import load_dotenv
from pymongo import MongoClient

env = os.getenv('ENV')

if env == 'local':
    load_dotenv('.env.local')
else:
    load_dotenv('.env.production')

USER = os.environ.get('USERNAME')
PWD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DB = os.environ.get('DATABASE')

MONGO_URI = f'mongodb://{USER}:{PWD}@{HOST}:{PORT}/{DB}'

mongo_client = MongoClient(MONGO_URI)
mongo_db = mongo_client[DB]


def get_mongo_database():
    """ Get MongoDB connection """
    try:
        yield mongo_db
    finally:
        mongo_client.close()
