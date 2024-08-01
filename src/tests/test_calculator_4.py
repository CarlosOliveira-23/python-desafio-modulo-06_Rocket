import json
import pytest
from src.server import create_app

app = create_app()


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_calculate_average(client):
    response = client.post('/calculator_4', json={'numbers': [1, 2, 3, 4, 5]})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data == {'data': {'Calculator': 4, 'average': 3.0}}


def test_calculate_average_invalid_input(client):
    response = client.post('/calculator_4', json={'invalid': [1, 2, 3, 4, 5]})
    assert response.status_code == 422
    data = json.loads(response.data)
    assert 'message' in data
