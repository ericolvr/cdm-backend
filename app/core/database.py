""" Database configuration """
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DB}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    future=True
)

Base = declarative_base()


def make_database():
    """ Create models """
    
    Base.metadata.create_all(bind=engine)


def get_database():
    """ Get database connection """

    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()