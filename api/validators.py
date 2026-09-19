def validate_booking_response(booking):
    required_structure = [
        "firstname",
        "lastname",
        "totalprice",
        "depositpaid",
        "bookingdates",
    ]
    for field in required_structure:
        assert field in booking

def validate_booking_dates(booking):
    assert "checkin" in booking["bookingdates"]
    assert "checkout" in booking["bookingdates"]