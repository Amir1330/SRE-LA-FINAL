import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    """Test the health check endpoint"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert 'status' in data
    assert data['status'] == 'healthy'
    assert 'timestamp' in data

def test_data_endpoint(client):
    """Test the data endpoint"""
    response = client.get('/api/data')
    # Since we have random errors, we should accept both 200 and 500
    assert response.status_code in [200, 500]
    data = response.get_json()
    
    if response.status_code == 200:
        assert 'data' in data
        assert isinstance(data['data'], list)
        assert len(data['data']) == 3
        assert 'timestamp' in data
    else:
        assert 'error' in data
        assert 'timestamp' in data 