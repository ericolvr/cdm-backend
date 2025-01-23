""" Database configuration """
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

user = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')
host = os.environ.get('HOST')
port = os.environ.get('PORT')
database = os.environ.get('DATABASE')

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://root:{password}@{host}:{port}/{database}'

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, future=True)

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