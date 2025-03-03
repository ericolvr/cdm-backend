""" Announcement Routes """
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate
from app.services.announcement_service import AnnouncementService


announcement_routes = APIRouter(
    prefix='/api/v1/announcements',
    tags=['Announcements']
)

@announcement_routes.post('/', status_code=201)
async def create_people(
    announcement: AnnouncementCreate, 
    database: Session = Depends(get_database),
):
    announcement_service = AnnouncementService(database)
    return await announcement_service.create_announcement(announcement)


@announcement_routes.get('/')
async def get_all_peoples(database: Session = Depends(get_database)):
    announcement_service = AnnouncementService(database)
    return await announcement_service.get_all_announcements()


@announcement_routes.get('/id')
async def get_announcement_by_id(id: str, database: Session = Depends(get_database)):
    announcement_service = AnnouncementService(database)
    return await  announcement_service.get_people_by_id(id)


@announcement_routes.patch('/update/{id}')
async def update_by_id(
        id: int, 
        new_data: AnnouncementUpdate, 
        database: Session = Depends(get_database)
):
    announcement_service = AnnouncementService(database)
    return await announcement_service.update_by_id(id, new_data)
