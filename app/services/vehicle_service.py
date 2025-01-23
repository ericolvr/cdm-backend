""" Vehicle Service """
from sqlalchemy.orm import Session

from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate
from app.domain.model.vehicle import Vehicle


class VehicleService:
    """ Vehicle service """
    
    def __init__(self, db: Session):
        self.repository = VehicleRepository(db)


    def create_vehicle(self, vehicle: VehicleCreate):
        """ Vehicle Config """
    
        vehicle = Vehicle(
            brand=vehicle.brand,
            model=vehicle.model,
            plate=vehicle.plate,
            complex_id=vehicle.complex_id,
            apartment_id=vehicle.apartment_id
        )
        return self.repository.create_vehicle(vehicle)    
    
    
    def get_vehicles(self):
        """ Get vehicles """
    
        vehicles = self.repository.get_vehicles()
        return vehicles


    def update_by_id(self, id: int, new_data):
        """ Update vehicle by id """
    
        config = self.repository.update_by_id(id, new_data)
        return config
    
