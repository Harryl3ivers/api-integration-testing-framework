import sqlite3


DATABASE_NAME = "database/test_database.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection
connection = get_connection()
connection.close()