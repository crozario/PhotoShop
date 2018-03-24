import MySQLdb as mdb
import sys


HOST="localhost"
USER="testuser"
PASSWORD="password"
DATABASE="test"

try: 
	db = mdb.connect(host=HOST,user=USER,passwd=PASSWORD,db=DATABASE)
	cursor = db.cursor()

	cursor.execute("SELECT VERSION()")

	data = cursor.fetchone()
	print("Version: ", data)

except Exception as e:
    print(e)

finally:
    db.close()

    
