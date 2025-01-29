import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from app.core.database import Base, get_database
from app.main import app


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


SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{USER}:{PWD}@{HOST}:{PORT}/{DB}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine, 
    future=True
)

Base.metadata.create_all(bind=engine)

def override_get_database():
    """get database connection"""
    database = SessionLocal()
    try:
        yield database
    finally:
        database.close()

app.dependency_overrides[get_database] = override_get_database