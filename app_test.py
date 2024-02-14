import pytest
import json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_greeting(client):
    response = client.get('/')
    assert response.status_code == 200
    assert "<h2> Hello </h2>" in response.data.decode('utf-8')

def test_fruits(client):
    response = client.get('/fruits')
    assert response.status_code == 200
    data = json.loads(response.data)
    expected_fruits = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    assert data['fruits'] == expected_fruits
