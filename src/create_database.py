from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config
from photoshop_database import setupPhotoShopDatabase

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

