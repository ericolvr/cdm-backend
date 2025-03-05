""" Place Routes """
from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.place import PlaceCreate, PlaceUpdate
from app.services.place_service import PlaceService


place_routes = APIRouter(
    prefix='/api/v1/places',
    tags=['Places']
)

@place_routes.post('/', status_code=201)
async def create_place(
    place: PlaceCreate, 
    database: Session = Depends(get_database),
):
    place_service = PlaceService(database)
    return await place_service.create_place(place)


@place_routes.get('/')
async def get_all_places(database: Session = Depends(get_database)):
    place_service = PlaceService(database)
    return await place_service.get_all_places()


@place_routes.get('/id')
async def get_place_by_id(id: str, database: Session = Depends(get_database)):
    place_service = PlaceService(database)
    return await  place_service.get_place_by_id(id)


@place_routes.patch('/update/{id}')
async def update_by_id(
        id: int, 
        new_data: PlaceUpdate, 
        database: Session = Depends(get_database)
):
    place_service = PlaceService(database)
    return await place_service.update_by_id(id, new_data)

