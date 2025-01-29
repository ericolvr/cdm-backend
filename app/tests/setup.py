import pytest
from app.domain.model.complex import Complex
from app.domain.model.people import People
from app.domain.model.vehicle import Vehicle


@pytest.fixture(autouse=True)
def create_data():
    from conftest import override_get_database
    db = next(override_get_database())

    complex = Complex(
        name='Complex 1',
        floors=10,
        apartments_by_floor=4
    )
    db.add(complex)
    db.commit()
    
    people = People(
        name='John Doe',
        document='123456789',
        mobile='123456789',
        picture=None,
        complex_id=1,
        apartment_id=1
    )
    db.add(people)
    db.commit()

    vehicle = Vehicle(
        brand='BMW',
        model='X5',
        plate='ABC1234',
        complex_id=1,
        apartment_id=1
    )
    db.add(vehicle)
    db.commit()

    yield
