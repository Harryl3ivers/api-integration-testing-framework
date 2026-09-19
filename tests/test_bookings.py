import requests
import pytest
from api.client import APIClient
from api.config import BASE_URL
from api.validators import validate_booking_dates, validate_booking_response


def test_get_bookings(client):
    response = client.get_bookings()
    assert response.status_code == 200
    assert response.json() is not None

def test_create_booking(client,booking_data):
    
    response = client.create_bookings(booking_data)
    assert response.status_code == 200
    response_data = response.json()
    assert "bookingid" in response_data
    assert response_data["booking"]["firstname"] == booking_data["firstname"]
    assert response_data["booking"]["lastname"] == booking_data["lastname"]
    assert response_data["booking"]["totalprice"] == 100
    assert response_data["booking"]["depositpaid"] is True

def test_get_booking_id(client,booking_data,booking_id):
    get_response = client.get_booking_id(booking_id)
    assert get_response.status_code == 200
    booking = get_response.json()
    assert booking["firstname"] == booking_data["firstname"]
    assert booking["lastname"] == booking_data["lastname"]
    assert booking["totalprice"] == 100

def test_update_booking(client,booking_data,booking_id, auth_token):
    create_response = client.create_bookings(booking_data)

    assert create_response.status_code == 200
    booking = create_response.json()["booking"]
    validate_booking_response(booking)
    validate_booking_dates(booking)

    booking_id = create_response.json()["bookingid"]

    updated_booking = {
        "firstname": "James",
        "lastname": "Smith",
        "totalprice": 150,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2026-10-01",
            "checkout": "2026-10-05"
        },
        "additionalneeds": "Lunch"
    }

    update_response = client.update_booking(
        booking_id,
        updated_booking,
        auth_token
    )

    assert update_response.status_code == 200

    response_data = update_response.json()

    assert response_data["firstname"] == "James"
    assert response_data["totalprice"] == 150
    assert response_data["depositpaid"] is False
    assert response_data["additionalneeds"] == "Lunch"

def test_delete_booking(client,booking_id,booking_data,auth_token):
    response = client.delete_booking(booking_id,booking_data,auth_token)
    assert response.status_code == 201
    get_response = client.get_booking_id(booking_id)
    assert get_response.status_code == 404
    

@pytest.mark.parametrize("booking_id",[99999999,0,-1])
def test_get_booking_with_invalid_id(client,booking_id):
    response = client.get_booking_id(booking_id)
    assert response.status_code == 404