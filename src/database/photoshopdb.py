import MySQLdb as mdb
import sys

def setupPhotoShopDatabase(cursor):
	createTables(cursor)

def createTables(cursor):
	createPhotoTable(cursor)
	createLandScapeTable(cursor)
	createLocationTable(cursor)
	createAbstractTable(cursor)
	createModelsTable(cursor)
	createModelTable(cursor)
	createPhotographerTable(cursor)
	createInfuencesTable(cursor)
	createTransactionTable(cursor)
	createCustomerTable(cursor)


def createPhotoTable(cursor):
	query = """CREATE TABLE IF NOT EXIST Photo( )
	"""
	cursor.execute(query)
	response = cursor.fetchone()
	
	return response 

def createLandScapeTable(cursor):
	pass


def createLocationTable(cursor):
	pass

def createAbstractTable(cursor):
	pass

def createModelsTable(cursor):
	pass

def createModelTable(cursor):
	pass

def createPhotographerTable(cursor):
	pass

def createInfuencesTable(cursor):
	pass

def createTransactionTable(cursor):
	pass

def createCustomerTable(cursor):
	pass





















