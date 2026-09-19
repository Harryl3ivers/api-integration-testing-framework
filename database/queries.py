from database.connection import get_connection

def create_booking_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS bookings(booking_id INT PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    totalprice INTEGER,
    depositpaid BOOLEAN)""")

    connection.commit()
    connection.close()

def insert_bookings(booking):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO bookings(booking_id, firstname, lastname, totalprice, depositpaid)
    VALUES(?, ?, ?, ?, ?)
    """,
    (
        booking["bookingid"],
        booking["booking"]["firstname"],
        booking["booking"]["lastname"],
        booking["booking"]["totalprice"],
        booking["booking"]["depositpaid"]
    ))

    connection.commit()
    connection.close()

def get_booking_from_database(booking_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("""SELECT booking_id,firstname,lastname,totalprice,depositpaid FROM bookings WHERE booking_id = ? """,(booking_id,))
    result = cursor.fetchone()
    connection.close()
    return result