from api.client import APIClient
from api.config import BASE_URL
def test_longin_with_correct_credentials(client):
    response = client.login("admin","password123")
    assert response.status_code == 200
    response_data = response.json()
    assert "token" in response_data
    assert response_data["token"] is not None

def test_login_with_invalid_credentials(client):
    response = client.login(
        "wrong_username","wrong_password")
    assert response.status_code == 200
    response_data = response.json()
    assert "reason" in response_data
    assert response_data["reason"] == "Bad credentials"