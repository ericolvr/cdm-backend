""" Complex Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from app.domain.model.complex import Complex


class ComplexRepository:
    """ Complex repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def create_complex(self, complex: Complex) ->Complex:
        """ Create Complex """
        
        self.db.add(complex)
        self.db.commit()
        self.db.refresh(complex)
        return complex
    
    
    def get_all_complexes(self) -> List[Complex]:
        """ Get All complex """
        
        complex = self.db.query(Complex).all()
        return complex
        

    def get_complex_by_id(self, id: int) -> Complex:
        """ Get Complex By Id """
        
        complex = self.db.query(Complex).filter(Complex.id == id).first()
        if not complex:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, 
                detail=f'Complex id {id} not found'
            )
        return complex
    

    def update_by_id(self, id: int, new_data) -> Complex:
        """ Update complex by id """
        
        result = self.get_complex_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result