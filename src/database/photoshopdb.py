import MySQLdb as mdb
import sys

def setupPhotoShopDatabase():
	HOST="localhost"
	USER="root"
	PASSWORD="Halo2014"
	
	try: 
		db = mdb.connect(host=HOST,user=USER,password=PASSWORD)
		cursor = db.cursor()
		query = "SELECT VERSION()"
		cursor.execute(query)
		data = cursor.fetchone()
		print("Version: ", data)

		# createPhotoshopDatabase(cursor)

		query = """SELECT DATABASE();"""
		cursor.execute(query)
		response = cursor.fetchone()
		print(response)




	except Exception as e:
		print(e)

	finally:
		db.close()


def createPhotoshopDatabase(cursor):
	query = """create database IF NOT EXIST PhotoShop;"""
	cursor.execute(query)
	response = cursor.fetchone()

	return response 


def createTables():
	createPhotoTable()
	createLandScapeTable()
	createLocationTable()
	createAbstractTable()
	createModelsTable()
	createModelTable()
	createPhotographerTable()
	createInfuencesTable()
	createTransactionTable()
	createCustomerTable()


def createPhotoTable():
	query = """CREATE TABLE IF NOT EXIST Photo( )
	"""
	cursor.execute(query)
	response = cursor.fetchone()
	
	return response 

def createLandScapeTable():
	pass


def createLocationTable():
	pass

def createAbstractTable():
	pass

def createModelsTable():
	pass

def createModelTable():
	pass

def createPhotographerTable():
	pass

def createInfuencesTable():
	pass

def createTransactionTable():
	pass

def createCustomerTable():
	pass





















