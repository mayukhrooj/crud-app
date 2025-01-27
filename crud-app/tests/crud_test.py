import pytest
from app.app import create_app, data

# Fixture to set up the test client
@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

# Fixture to reset the in-memory `data` before each test
@pytest.fixture(autouse=True)
def reset_data():
    data.clear()

def test_create_item(client):
    response = client.post('/items', json={'name': 'Item 1'})
    assert response.status_code == 201
    assert response.json['item']['name'] == 'Item 1'

def test_get_all_items(client):
    client.post('/items', json={'name': 'Item 1'})
    response = client.get('/items')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_get_single_item(client):
    client.post('/items', json={'name': 'Item 1'})
    response = client.get('/items/1')
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Item 1'

def test_update_item(client):
    client.post('/items', json={'name': 'Item 1'})
    response = client.put('/items/1', json={'name': 'Updated Item'})
    assert response.status_code == 200
    assert response.json['item']['name'] == 'Updated Item'

def test_delete_item(client):
    client.post('/items', json={'name': 'Item 1'})
    response = client.delete('/items/1')
    assert response.status_code == 204
    response = client.get('/items/1')
    assert response.status_code == 404
