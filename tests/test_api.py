from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test the health check endpoint"""
    response = client.get("/health_check/")
    assert response.status_code == 200
    data = response.json()
    assert "status" in data
    assert data["status"] == "healthy"
    assert "timestamp" in data
    assert "message" in data


def test_user_profile():
    """Test the user profile endpoint"""
    # Test with known user ID
    response = client.get("/user/profile/123")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "123"
    assert data["username"] == "sample_user"
    assert data["email"] == "user@example.com"
    assert data["name"] == "Sample User"
    assert data["level"] == 5
    
    # Test with random user ID
    response = client.get("/user/profile/456")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "456"
    assert data["username"] == "user_456"
    assert data["level"] == 1
