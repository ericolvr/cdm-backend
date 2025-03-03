""" Announcement Service """
from sqlalchemy.orm import Session
from fastapi import HTTPException, BackgroundTasks

from app.domain.model.announcement import Announcement
from app.schemas.announcement import AnnouncementCreate, AnnouncementUpdate
from app.repositories.announcement_repository import AnnouncementRepository


class AnnouncementService:
    """ Announcement service """
    
    def __init__(self, db: Session):
        self.repository = AnnouncementRepository(db)
        self.database = db


    def create_announcement(self, announcement: AnnouncementCreate):
        """ Create Announcement """

        announcement = Announcement(
            type=announcement.type,
            title=announcement.title,
            description=announcement.description
        )

        return self.repository.create_announcement(announcement)


    def get_all_announcements(self):
        """ Get all Announcements """

        announcements = self.repository.get_all_announcements()
        return announcements


    def get_announcement_by_id(self, id: str):
        """ Get announcement by id """

        announcement = self.repository.get_announcement_by_id(id)
        return announcement
    

    def update_by_id(self, id: int, new_data):
        """ Update announcement by id """
    
        announcement = self.repository.update_by_id(id, new_data)
        return announcement

