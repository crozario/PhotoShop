from mysql.connector import Error, MySQLConnection
from database_config_parser import read_db_config

def setupPhotoShopDatabase(conn):
	createTables(conn)
	print("Created PhotoShop Tables")

	createConstraints(conn)
	print("Created Constraints")

def createTables(conn):
	createPhotoTable(conn)
	createLandScapeTable(conn)
	createLocationTable(conn)
	createAbstractTable(conn)
	createModelsTable(conn)
	createModelTable(conn)
	createPhotographerTable(conn)
	createInfluencesTable(conn)
	createTransactionTable(conn)
	createCustomerTable(conn)


def createPhotoTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Photo` (
		`PhotoID` INT UNSIGNED,
  		`Speed` VARCHAR(45),
  		`Film` VARCHAR(45),
  		`F-Stop` VARCHAR(10),
  		`Color/B&W` VARCHAR(10),
		`Resolution` VARCHAR(25),
  		`Price` FLOAT UNSIGNED,
  		`Date` DATE,
  		`TransID` INT UNSIGNED NULL,
		`PName` VARCHAR(25) NULL,
		`PBDate` DATE NULL,
  		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoTable Failed")
		print(e)
	finally:
		cursor.close()

def createLandScapeTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Landscape` (
		`PhotoID` INT UNSIGNED,
		`Place` VARCHAR(45) NULL,
		`Country` VARCHAR(45) NULL,
		PRIMARY KEY (`PhotoID`)
	) 
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createLandscapeTable Failed")
		print(e)
	finally:
		cursor.close()

def createLocationTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Location` (
		`Place` VARCHAR(45),
  		`Country` VARCHAR(45),
  		`Description` TEXT NULL,
  		PRIMARY KEY (`Place`, `Country`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createLocationTable Failed")
		print(e)
	finally:
		cursor.close()

def createAbstractTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Abstract` (
		`PhotoID` INT UNSIGNED,
		`Comment` Text NULL,
		PRIMARY KEY (`PhotoID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createAbstractTable Failed")
		print(e)
	finally:
		cursor.close()

def createModelsTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Models` (
		`PhotoID` INT UNSIGNED,
		`MName` VARCHAR(25),
		`MBDate` DATE,
		`Agency` VARCHAR(45),
		PRIMARY KEY (`PhotoID`, `MName`, `MBDate`)
	)
	ENGINE=InnoDB;
	"""

	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createModelsTable Failed")
		print(e)
	finally:
		cursor.close()

def createModelTable(conn):
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
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createModelTable Failed")
		print(e)
	finally:
		cursor.close()

def createPhotographerTable(conn):
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
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotographerTable Failed")
		print(e)
	finally:
		cursor.close()

def createInfluencesTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Influences` (
		`EPName` VARCHAR(25),
  		`EPBDate` DATE,
		`RPName` VARCHAR(25),
  		`RPBDate` DATE,
  		PRIMARY KEY (`EPName`, `EPBDate`, `RPName`, `RPBDate`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createInfuencesTable Failed")
		print(e)
	finally:
		cursor.close()

def createTransactionTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Transaction` (
		`TransID` INT UNSIGNED,
  		`TDate` DATE,
  		`CardNo` INT UNSIGNED,
 		`CardType` VARCHAR(25),
  		`CardExpDate` DATE,
  		`TotalAmount` FLOAT UNSIGNED,
  		`LoginName` VARCHAR(25),
  		PRIMARY KEY (`TransID`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createTransactionTable Failed")
		print(e)
	finally:
		cursor.close()

def createCustomerTable(conn):
	query = """CREATE TABLE IF NOT EXISTS `Customer` (
		`LoginName` VARCHAR(25),
  		`Password` VARCHAR(25),
  		`CName` VARCHAR(25),
  		`CType` VARCHAR(45),
  		`BillingAddress` TEXT,
  		`Str1` VARCHAR(45),
  		`Str2` VARCHAR(45),
  		`City` VARCHAR(45),
  		`State` CHAR(2),
  		`Zip` VARCHAR(12),
  		PRIMARY KEY (`LoginName`)
	)
	ENGINE=InnoDB;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createCustomerTable Failed")
		print(e)
	finally:
		cursor.close()
	
def createConstraints(conn):
	createPhotoConstraints(conn) 
	createLocationConstraints(conn) 
	createModelConstraints(conn) 
	createPhotographerConstraints(conn)
	createTransactionConstraints(conn) 
	createCustomerConstraints(conn) 

def createPhotoConstraints(conn):
	query = """
		ALTER TABLE Photo
		ADD CONSTRAINT FK_PhotoID_Landscape FOREIGN KEY (PhotoID) REFERENCES Landscape(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_PhotoID_Abstract FOREIGN KEY (PhotoID) REFERENCES Abstract(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_PhotoID_Models FOREIGN KEY (PhotoID) REFERENCES Models(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()

def createLocationConstraints(conn):
	query = """
		ALTER TABLE Location
		ADD CONSTRAINT FK_Place_Landscape FOREIGN KEY (Place) REFERENCES Landscape(Place) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_Country_Landscape FOREIGN KEY (Country) REFERENCES Landscape(Country) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()

def createModelConstraints(conn):
	query = """
		ALTER TABLE Model
		ADD CONSTRAINT FK_MName_Models FOREIGN KEY (MName) REFERENCES Models(MName) ON DELETE CASCADE ON UPDATE CASCADE,
		ADD CONSTRAINT FK_MBDate_Models FOREIGN KEY (MBDate) REFERENCES Models(MBDate) ON DELETE CASCADE ON UPDATE CASCADE;
	"""

	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()


def createPhotographerConstraints(conn):
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
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()


def createTransactionConstraints(conn):
	query = """
		ALTER TABLE Transaction
		ADD CONSTRAINT FK_TransID_Photo FOREIGN KEY (TransID) REFERENCES Photo(TransID) ON DELETE CASCADE ON UPDATE CASCADE;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()



def createCustomerConstraints(conn):
	query = """
		ALTER TABLE Customer
		ADD CONSTRAINT FK_LoginName_Transaction FOREIGN KEY (LoginName) REFERENCES Transaction(LoginName) ON DELETE CASCADE ON UPDATE CASCADE;
	"""
	try:
		cursor = conn.cursor()
		cursor.execute(query)
	except Error as e:
		print("createPhotoConstraints Failed")
		print(e)
	finally:
		cursor.close()


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

		setupPhotoShopDatabase(conn)
		print("Created PhotoShop Database")
	except Error as error:
		print(error)
	finally:
		conn.close()

def main():
    SetupDatabase()

if __name__ == '__main__':
	main()

