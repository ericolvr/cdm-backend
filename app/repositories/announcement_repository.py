""" Announcement Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.domain.model.announcement import Announcement


class AnnouncementRepository:
    """ Announcement Repository """

    def __init__(self, db: Session):
        self.db = db


    async def create_announcement(self, announcement: Announcement) -> Announcement:
        """ Create Announcement """

        self.db.add(announcement)
        self.db.commit()
        self.db.refresh(announcement)
        return Announcement
    

    async def get_all_announcements(self) -> List[Announcement]:
        """ get Announcement """

        announcements = self.db.query(Announcement).all()
        return announcements


    async def get_announcement_by_id(self, id: int) -> Announcement:
        """ Get Announcement by id """
        
        announcement = self.db.query(Announcement).filter(
            Announcement.id == id
        ).first()
        
        if not announcement:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Announcement id {id} not found'
            )
        return announcement
       

    async def update_by_id(self, id: int, new_data) -> Announcement:
        """ Update Announcement by id """
        
        result = await self.get_people_by_id(id)
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result

    
    
    