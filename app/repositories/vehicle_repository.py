""" Vehicle Repository """
from typing import List
from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload

from app.domain.model.vehicle import Vehicle
from app.domain.model.complex import Complex
from app.domain.model.apartment import Apartment


class VehicleRepository:
    """ Vehicle Repository"""
    
    def __init__(self, db: Session):
        self.db = db


    def create_vehicle(self, vehicle: Vehicle) -> Vehicle:
        """ Create Vehicle """
        
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle
    
    
    def get_vehicles(self) -> List[Vehicle]:
        """ Get Vehicles """
        
        vehicles = (
            self.db.query(Vehicle)
            .options(
                joinedload(Vehicle.complex)
                .load_only(Complex.name),
                joinedload(Vehicle.apartment)
                .load_only(Apartment.apartment_number)
            )
        ).all()
        return vehicles


    def get_vehicle_by_complex_apartment(
            self, 
            complex: 
            int, apartment: int
        ) -> List[Vehicle]:
        """ Get Vehicle By Complex And Apartment """
        
        vehicles = self.db.query(Vehicle).filter(
            Vehicle.complex_id == complex,
            Vehicle.apartment_id == apartment
        ).all()
        
        return vehicles
    

    def get_vehicle_by_id(self, id: int) -> Vehicle:
        """ Get Vehicle By Id """
        
        vehicle = self.db.query(vehicle).filter(Vehicle.id == id).first()
        if not vehicle:
            raise HTTPException(
                status_code=404, detail=f'Vehicle {id} not found'
            )
            return message
        return vehicle
           

    def update_by_id(self, id: int, new_data) -> Vehicle:
        """ Update Vehicle By Id """
        
        result = self.get_vehicle_by_id(id)
        
        if not result:
            return result
        
        data = new_data.dict(exclude_unset=True)

        for key, value in data.items():
            setattr(result, key, value)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)

        return result