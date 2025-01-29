""" Complex Service """
from sqlalchemy.orm import Session

from app.repositories.complex_repository import ComplexRepository
from app.schemas.complex import ComplexCreate
from app.domain.model.complex import Complex
from app.services.apartment_service import ApartmentService


class ComplexService:
    """ Complex Service """
    
    def __init__(self, db: Session):
        self.repository = ComplexRepository(db)
        self.database = db


    def create_complex(self, complex: ComplexCreate):
        """ Create Complex """
    
        complex = Complex(
            name=complex.name,
            floors=complex.floors,
            apartments_by_floor=complex.apartments_by_floor
        )

        self.repository.create_complex(complex)

        ApartmentService(self.database).automatic_apartments(
            complex.id,
            complex.floors,
            complex.apartments_by_floor,
        )
        
        return {'message': 'Complex created successfully'} 
        # TODO -  Improve
    
    
    def get_all_complexes(self):
        """ Get All Complexes """
    
        complexes = self.repository.get_all_complexes()
        return complexes
    

    def get_complex_by_id(self, id: str):
        """ Get Complex By Id """
    
        complex = self.repository.get_complex_by_id(id)
        return complex
    

    def update_by_id(self, id: int, new_data):
        """ Update Complex By Id """
    
        comples = self.repository.update_by_id(id, new_data)
        return comples
    
