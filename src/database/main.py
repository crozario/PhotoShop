from mysql.connector import Error, MySQLConnection
from dbconfigparser import read_db_config
from photoshopdb import setupPhotoShopDatabase

def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row


def SetupDatabase():

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        if conn.is_connected():
            print("Database Connection Success")
        else:
            print("Database Connection Failed")
        
        cursor = conn.cursor()
        setupPhotoShopDatabase(cursor)
        print("Created PhotoShop Database")


    except Error as error:
        print(error)
 
    finally:
        cursor.close()
        conn.close()

def main():
    SetupDatabase()

if __name__ == '__main__':
	main()

