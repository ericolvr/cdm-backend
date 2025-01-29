""" Vehicle Service """
from sqlalchemy.orm import Session

from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate
from app.domain.model.vehicle import Vehicle


class VehicleService:
    """ Vehicle service """
    
    def __init__(self, db: Session):
        self.repository = VehicleRepository(db)


    async def create_vehicle(self, vehicle: VehicleCreate):
        """ Vehicle Create """
    
        vehicle = Vehicle(
            brand=vehicle.brand,
            model=vehicle.model,
            plate=vehicle.plate,
            complex_id=vehicle.complex_id,
            apartment_id=vehicle.apartment_id
        )
        return await self.repository.create_vehicle(vehicle)    
    
    
    async def get_vehicles(self):
        """ Get Vehicles """
    
        vehicles = await self.repository.get_vehicles()
        return vehicles
    

    async def get_vehicle_by_complex_apartment(self, complex, apartment):
        """ Get Vehicle By Complex And Apartment """

        vehicles = await self.repository.get_vehicle_by_complex_apartment(complex, apartment)
        return vehicles


    async def update_by_id(self, id: int, new_data):
        """ Update Vehicle By Id """
    
        config = await self.repository.update_by_id(id, new_data)
        return config
    
