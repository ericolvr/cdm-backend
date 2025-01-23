""" Apartment Service """
from sqlalchemy.orm import Session

from app.repositories.apartment_repository import ApartmentRepository
from app.schemas.apartment import ApartmentCreate
from app.domain.model.apartment import Apartment


class ApartmentService:
    """ Apartment service """
    
    def __init__(self, db: Session):
        self.repository = ApartmentRepository(db)


    def automatic_apartments(
        self, 
        complex_id: int, 
        floors: int, 
        apartments_by_floor: int
    ):
        """ Automatic apartments """
        
        for floor in range(1, floors + 1):
            for apartment_number in range(1, apartments_by_floor + 1):                
                apartment_number_full = int(f"{floor}{apartment_number}")
                apartment = Apartment(
                    complex_id=complex_id,
                    apartment_number=apartment_number_full
                )
                self.repository.create_apartment(apartment)


    def create_apartment(self, apartment: ApartmentCreate):
        """ Create Apartment """
    
        apartment = Apartment(
            complex_id=apartment.complex_id,
            apartment_number=apartment.apartment_number
        )
        return self.repository.create_apartment(apartment)    
    
    
    def get_all_apartments(self):
        """ Get all apartments """
    
        apartments = self.repository.get_all_apartments()
        return apartments


    def get_apartments_by_tower(self, number: int):
        """ Get apartments by tower """
    
        apartments = self.repository.get_apartments_by_tower(number)
        return apartments
    

    def get_apartment_by_id(self, id: str):
        """ Get apartment by id """
    
        apartment = self.repository.get_apartment_by_id(id)
        return apartment
    

    def update_by_id(self, id: int, new_data):
        """ Update apartment by id """
    
        apartment = self.repository.update_by_id(id, new_data)
        return apartment
    
