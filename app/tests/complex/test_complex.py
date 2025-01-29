import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_create_complex():
    """ Must be create complex and returns 201 """
    
    response = client.post('/api/v1/complexes/',
        json={
            'name': 'Test Complex',
            'floors': 10,
            'apartments_by_floor': 2
        }
    )
    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_all_complexes():
    """ Must be return all complexes and returns 200 """
    
    response = client.get('/api/v1/complexes')
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_get_complex_by_id():
    """ Must be return complex by id and returns 200 """
    
    response = client.get('/api/v1/complexes/id?id=1')
    assert response.status_code == 200


