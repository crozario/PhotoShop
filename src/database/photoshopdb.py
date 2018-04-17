import MySQLdb as mdb
import sys

def setupPhotoShopDatabase(cursor):
	createTables(cursor)
	print("Created PhotoShop Tables")

	createConstraints(cursor)
	print("Created Constraints")

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
	query = """CREATE TABLE IF NOT EXISTS `Photo` (
		`PhotoID` INT UNSIGNED AUTO_INCREMENT,
  		`Speed` VARCHAR(45) NULL,
  		`Film` VARCHAR(45) NULL,
  		`F-Stop` VARCHAR(12) NULL,
  		`Color/B&W` VARCHAR(10) NULL,
		`Resolution` VARCHAR(25) NULL,
  		`Price` FLOAT UNSIGNED,
  		`Date` DATE NULL,
  		`TransID` INT UNSIGNED NULL,
		`PName` VARCHAR(25) NOT NULL,
		`PBDate` DATE NOT NULL,
  		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createLandScapeTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Landscape` (
		`PhotoID` INT UNSIGNED,
		`Place` VARCHAR(45) NULL,
		`Country` VARCHAR(45) NULL,
		PRIMARY KEY (`PhotoID`)
	) 
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createLocationTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Location` (
		`Place` VARCHAR(45),
  		`Country` VARCHAR(45),
  		`Description` TEXT NULL,
  		PRIMARY KEY (`Place`, `Country`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createAbstractTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Abstract` (
		`PhotoID` INT UNSIGNED,
		`Comment` Text NULL,
		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createModelsTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Models` (
		`PhotoID` INT UNSIGNED,
		`MName` VARCHAR(25),
		`MBDate` DATE,
		`Agency` VARCHAR(45) NULL,
		PRIMARY KEY (`PhotoID`, `MName`, `MBDate`)
	)
	ENGINE=InnoDB;
	"""

	cursor.execute(query)

def createModelTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Model` (
		`MName` VARCHAR(25) NOT NULL,
  		`MBDate` DATE NOT NULL,
		`MBio` TEXT NULL,
  		`MSex` CHAR(1) NULL,
  		PRIMARY KEY (`MName`, `MBDate`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createPhotographerTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Photographer` (
		`PName` VARCHAR(25),
  		`PBDate` DATE,
  		`PBio` TEXT NULL,
 		`PBAddress` TEXT NULL,
 		`PNationality` VARCHAR(45) NULL,
 		 PRIMARY KEY (`PName`, `PBDate`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createInfuencesTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Influences` (
		`EPName` VARCHAR(25),
  		`EPBDate` DATE,
		`RPName` VARCHAR(25),
  		`RPBDate` DATE,
  		PRIMARY KEY (`EPName`, `EPBDate`, `RPName`, `RPBDate`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createTransactionTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Transaction` (
		`TransID` INT UNSIGNED AUTO_INCREMENT,
  		`TDate` DATE NOT NULL,
  		`CardNo` INT UNSIGNED NOT NULL,
 		`CardType` VARCHAR(25) NOT NULL,
  		`CardExpDate` DATE NOT NULL,
  		`TotalAmount` INT UNSIGNED NOT NULL,
  		`LoginName` VARCHAR(25) NOT NULL,
  		PRIMARY KEY (`TransID`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

def createCustomerTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Customer` (
		`LoginName` VARCHAR(25) NOT NULL,
  		`Password` VARCHAR(25) NOT NULL,
  		`CName` VARCHAR(25) NOT NULL,
  		`CType` VARCHAR(45) NULL,
  		`BillingAddress` TEXT NOT NULL,
  		`Str1` VARCHAR(45) NULL,
  		`Str2` VARCHAR(45) NULL,
  		`City` VARCHAR(45) NULL,
  		`State` CHAR(2) NULL,
  		`Zip` VARCHAR(12) NULL,
  		PRIMARY KEY (`LoginName`)
	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)


def createConstraints(cursor):
	query = """


	)
	ENGINE=InnoDB;
	"""
	cursor.execute(query)

















