from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def connect_to_database():

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        if not conn.is_connected():
            print("Database connection failed")
        else:
            print("Connected to Database")

    except Error as error:
        print(error)
 
    finally:
        return conn

def disconnect_from_database(conn):
    conn.close()
