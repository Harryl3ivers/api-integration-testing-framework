import pytest 
from api.config import BASE_URL
from api.client import APIClient
from faker import Faker
from database.connection import DATABASE_NAME
import os

@pytest.fixture
def client():
    return APIClient(BASE_URL)

@pytest.fixture
def booking_data():
    fake = Faker()
    return{
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
         "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-09-20",
            "checkout": "2026-09-25"
        },
        "additionalneeds": "Breakfast"
    }
@pytest.fixture
def auth_token(client):
    response = client.login("admin","password123")
    assert response.status_code == 200
    return response.json()["token"]

@pytest.fixture
def booking_id(client,booking_data):
    response = client.create_bookings(booking_data)
    assert response.status_code == 200
    return response.json()["bookingid"]

@pytest.fixture
def clean_database():
    if os.path.exists(DATABASE_NAME):
        os.remove(DATABASE_NAME)
    yield
    if os.path.exists(DATABASE_NAME):
         os.remove(DATABASE_NAME)