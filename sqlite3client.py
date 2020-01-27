import sqlite3
from datetime import datetime


def insert_variable_into_table(temperature, humidity, pressure, sensor_name):
    try:
        sqlite_connection = sqlite3.connect('ha.db')

        cursor = sqlite_connection.cursor()

        print("Successfully Connected to SQLite")

        now = datetime.now()

        # YYYY-MM-DD HH:MM:SS.SSS
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")

        sqlite_insert_query = """INSERT INTO aqaratempsensor
                              (id, temperature, humidity, pressure, created, sensor_name) 
                               VALUES 
                              (?,?,?,?,?,?)"""

        data_tuple = (id, temperature, humidity, pressure, now_string, sensor_name)

        count = cursor.execute(sqlite_insert_query)

        sqlite_connection.commit()

        print("Record inserted successfully into aqaratempsensor table ", cursor.rowcount)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert data into aqaratempsensor table", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("The SQLite connection is closed")
