from database.connection import get_connection
from database.queries import create_booking_table,insert_bookings, get_booking_from_database


def test_create_booking_table(clean_database):
    create_booking_table()
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' AND name ='bookings'""")
    result = cursor.fetchone()
    connection.close()
    assert result is not None

def test_api_booking_matches_db(client,booking_data,clean_database):
    create_booking_table()
    response = client.create_bookings(booking_data)
    assert response.status_code == 200
    booking = response.json()
    insert_bookings(booking)
    database_booking = get_booking_from_database(booking["bookingid"])
    assert database_booking is not None

    assert database_booking[0] == booking["bookingid"]
    assert database_booking[1] == booking["booking"]["firstname"]
    assert database_booking[2] == booking["booking"]["lastname"]
    assert database_booking[3] == booking["booking"]["totalprice"]
    assert bool(database_booking[4]) == booking["booking"]["depositpaid"]
