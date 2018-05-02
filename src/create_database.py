from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config

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
	createInfluencesTable(cursor)
	createTransactionTable(cursor)
	createCustomerTable(cursor)


def createPhotoTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Photo` (
		`PhotoID` INT UNSIGNED AUTO_INCREMENT,
  		`Speed` VARCHAR(45) NULL,
  		`Film` VARCHAR(45) NULL,
  		`F-Stop` VARCHAR(10) NULL,
  		`Color/B&W` VARCHAR(10) NULL,
		`Resolution` VARCHAR(25) NULL,
  		`Price` FLOAT UNSIGNED,
  		`Date` DATE NULL,
  		`TransID` INT UNSIGNED NOT NULL UNIQUE,
		`PName` VARCHAR(25) NOT NULL UNIQUE,
		`PBDate` DATE NOT NULL UNIQUE,
  		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoTable Failed")
		print(e)

def createLandScapeTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Landscape` (
		`PhotoID` INT UNSIGNED,
		`Place` VARCHAR(45) NULL UNIQUE,
		`Country` VARCHAR(45) NULL UNIQUE,
		PRIMARY KEY (`PhotoID`)
	) 
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createLandscapeTable Failed")
		print(e)

def createLocationTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Location` (
		`Place` VARCHAR(45),
  		`Country` VARCHAR(45),
  		`Description` TEXT NULL,
  		PRIMARY KEY (`Place`, `Country`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createLocationTable Failed")
		print(e)

def createAbstractTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Abstract` (
		`PhotoID` INT UNSIGNED,
		`Comment` Text NULL,
		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createAbstractTable Failed")
		print(e)

def createModelsTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Models` (
		`PhotoID` INT UNSIGNED,
		`MName` VARCHAR(25) UNIQUE,
		`MBDate` DATE UNIQUE,
		`Agency` VARCHAR(45) NULL,
		PRIMARY KEY (`PhotoID`, `MName`, `MBDate`)
	)
	ENGINE=InnoDB;
	"""

	try:
		cursor.execute(query)
	except Error as e:
		print("createModelsTable Failed")
		print(e)

def createModelTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Model` (
		`MName` VARCHAR(25),
  		`MBDate` DATE,
		`MBio` TEXT NULL,
  		`MSex` CHAR(1) NULL,
  		PRIMARY KEY (`MName`, `MBDate`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createModelTable Failed")
		print(e)

def createPhotographerTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Photographer` (
		`PName` VARCHAR(25),
  		`PBDate` DATE,
  		`PBio` TEXT NULL,
 		`PAddress` TEXT NULL,
 		`PNationality` VARCHAR(45) NULL,
 		 PRIMARY KEY (`PName`, `PBDate`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotographerTable Failed")
		print(e)

def createInfluencesTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Influences` (
		`EPName` VARCHAR(25) UNIQUE,
  		`EPBDate` DATE UNIQUE,
		`RPName` VARCHAR(25) UNIQUE,
  		`RPBDate` DATE UNIQUE,
  		PRIMARY KEY (`EPName`, `EPBDate`, `RPName`, `RPBDate`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createInfuencesTable Failed")
		print(e)

def createTransactionTable(cursor):
	query = """CREATE TABLE IF NOT EXISTS `Transaction` (
		`TransID` INT UNSIGNED,
  		`TDate` DATE NOT NULL,
  		`CardNo` INT UNSIGNED NOT NULL,
 		`CardType` VARCHAR(25) NOT NULL,
  		`CardExpDate` DATE NOT NULL,
  		`TotalAmount` FLOAT UNSIGNED NOT NULL,
  		`LoginName` VARCHAR(25) NOT NULL UNIQUE,
  		PRIMARY KEY (`TransID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createTransactionTable Failed")
		print(e)

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
	try:
		cursor.execute(query)
	except Error as e:
		print("createCustomerTable Failed")
		print(e)
	
def createConstraints(cursor):
	createPhotoConstraints(cursor) 
	createLocationConstraints(cursor) 
	createModelConstraints(cursor) 
	createPhotographerConstraints(cursor)
	createTransactionConstraints(cursor) 
	createCustomerConstraints(cursor) 

def createPhotoConstraints(cursor):
	query = """
		ALTER TABLE Photo
		ADD CONSTRAINT FK_PhotoID_Landscape FOREIGN KEY (PhotoID) REFERENCES Landscape(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_PhotoID_Abstract FOREIGN KEY (PhotoID) REFERENCES Abstract(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_PhotoID_Models FOREIGN KEY (PhotoID) REFERENCES Models(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)

def createLocationConstraints(cursor):
	query = """
		ALTER TABLE Location
		ADD CONSTRAINT FK_Place_Landscape FOREIGN KEY (Place) REFERENCES Landscape(Place) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_Country_Landscape FOREIGN KEY (Country) REFERENCES Landscape(Country) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)

def createModelConstraints(cursor):
	query = """
		ALTER TABLE Model
		ADD CONSTRAINT FK_MName_Models FOREIGN KEY (MName) REFERENCES Models(MName) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_MBDate_Models FOREIGN KEY (MBDate) REFERENCES Models(MBDate) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)


def createPhotographerConstraints(cursor):
	query = """
		ALTER TABLE Photographer
		ADD CONSTRAINT FK_PName_Photo FOREIGN KEY (PName) REFERENCES Photo(PName) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_PBDate_Photo FOREIGN KEY (PBDate) REFERENCES Photo(PBDate) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_EPName_Influences FOREIGN KEY (PName) REFERENCES Influences(EPName) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_EPBDate_Influences FOREIGN KEY (PBDate) REFERENCES Influences(EPBDate) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_RPName_Influences FOREIGN KEY (PName) REFERENCES Influences(RPName) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_RPBDate_Influences FOREIGN KEY (PBDate) REFERENCES Influences(RPBDate) ON DELETE CASCADE ON UPDATE CASCADE;

	"""
	
	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)


def createTransactionConstraints(cursor):
	query = """
		ALTER TABLE Transaction
		ADD CONSTRAINT FK_TransID_Photo FOREIGN KEY (TransID) REFERENCES Photo(TransID) ON DELETE SET NULL ON UPDATE CASCADE;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)



def createCustomerConstraints(cursor):
	query = """
		ALTER TABLE Customer
		ADD CONSTRAINT FK_LoginName_Transaction FOREIGN KEY (LoginName) REFERENCES Transaction(LoginName) ON DELETE CASCADE ON UPDATE CASCADE;
	"""
	try:
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)


def SetupDatabase():

	try:
		#windows/mac/linux
		conn = MySQLConnection(user='root', password='Halo2014', host='localhost', database='test')

		#mac/linux
		# db_config = read_db_config()
        # conn = MySQLConnection(**db_config)

		if conn.is_connected:
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

