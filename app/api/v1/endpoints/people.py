""" People routes """
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.people import PeopleCreate, PeopleUpdate
from app.services.people_service import PeopleService


people_routes = APIRouter(
    prefix='/api/v1/peoples',
    tags=['Peoples']
)

@people_routes.post('/', status_code=201)
def create_people(
    people: PeopleCreate, 
    background_tasks: BackgroundTasks,
    database: Session = Depends(get_database),
):
    people_service = PeopleService(database)
    return people_service.create_people(people, background_tasks)


@people_routes.get('/')
def get_all_peoples(database: Session = Depends(get_database)):
    people_service = PeopleService(database)
    return people_service.get_all_peoples()


@people_routes.get('/id')
def get_people_by_id(id: str, database: Session = Depends(get_database)):
    people_service = PeopleService(database)
    return people_service.get_people_by_id(id)


@people_routes.get('/complex/{complex}/apartment/{apartment}')
def get_people_by_complex_apartment(
    complex: int, 
    apartment: int, 
    database: Session = Depends(get_database)
):
    people_service = PeopleService(database)
    return people_service.get_people_by_complex_apartment(complex, apartment)


@people_routes.patch('/update/{id}')
def update_by_id(
        id: int, 
        new_data: PeopleUpdate, 
        database: Session = Depends(get_database)
):
    people_service = PeopleService(database)
    return people_service.update_by_id(id, new_data)
