import MySQLdb as mdb
import sys

db = mdb.connect(host="localhost",user="testuser",passwd="password",db="test")
cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()
print("Version: ", data)

sql = """CREATE TABLE Person(
         FIRSTNAME  CHAR(20) NOT NULL,
         LASTNAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1))"""

cursor.execute(sql)

db.close()

    
