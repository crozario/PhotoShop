-- INSERT INTO Photographer(PName, PBDate, PBio, PAddress, PNationality)
-- VALUES ("John", "1990-08-01", "hello my name is john", "1 washington street", "American");

-- INSERT INTO Photographer(PName, PBDate, PBio, PAddress, PNationality)
-- VALUES ("Jake", "1990-02-01", "hello my name is jake", "1 jefferson street", "American");

-- INSERT INTO Influences(EPName, EPBDate, RPName, RPBDate)
-- VALUES("John", "1990-08-01", "Jake", "1990-02-01")


-- select * from Influences;
-- select * from Photographer;
-- DELETE FROM Photographer WHERE PName = "Jake" and PBDate = "1990-02-01";

CREATE TABLE IF NOT EXISTS `Photo` (
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
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Landscape` (
		`PhotoID` INT UNSIGNED,
		`Place` VARCHAR(45) NULL,
		`Country` VARCHAR(45) NULL,
		PRIMARY KEY (`PhotoID`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Location` (
		`Place` VARCHAR(45),
  		`Country` VARCHAR(45),
  		`Description` TEXT NULL,
  		PRIMARY KEY (`Place`, `Country`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Abstract` (
		`PhotoID` INT UNSIGNED,
		`Comment` Text NULL,
		PRIMARY KEY (`PhotoID`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Models` (
		`PhotoID` INT UNSIGNED,
		`MName` VARCHAR(25),
		`MBDate` DATE,
		`Agency` VARCHAR(45),
		PRIMARY KEY (`PhotoID`, `MName`, `MBDate`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Model` (
		`MName` VARCHAR(25),
  		`MBDate` DATE,
		`MBio` TEXT NULL,
  		`MSex` CHAR(1) NULL,
  		PRIMARY KEY (`MName`, `MBDate`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Photographer` (
		`PName` VARCHAR(25),
  		`PBDate` DATE,
  		`PBio` TEXT NULL,
 		`PAddress` TEXT NULL,
 		`PNationality` VARCHAR(45) NULL,
 		 PRIMARY KEY (`PName`, `PBDate`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Influences` (
		`EPName` VARCHAR(25),
  		`EPBDate` DATE,
		`RPName` VARCHAR(25),
  		`RPBDate` DATE,
  		PRIMARY KEY (`EPName`, `EPBDate`, `RPName`, `RPBDate`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Transaction` (
		`TransID` INT UNSIGNED,
  		`TDate` DATE,
  		`CardNo` INT UNSIGNED,
 		`CardType` VARCHAR(25),
  		`CardExpDate` DATE,
  		`TotalAmount` FLOAT UNSIGNED,
  		`LoginName` VARCHAR(25),
  		PRIMARY KEY (`TransID`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Customer` (
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
) ENGINE=InnoDB;

ALTER TABLE Photo
	ADD CONSTRAINT FK_PhotoID_Landscape FOREIGN KEY (PhotoID) REFERENCES Landscape(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_PhotoID_Abstract FOREIGN KEY (PhotoID) REFERENCES Abstract(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_PhotoID_Models FOREIGN KEY (PhotoID) REFERENCES Models(PhotoID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Location
	ADD CONSTRAINT FK_Place_Landscape FOREIGN KEY (Place) REFERENCES Landscape(Place) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_Country_Landscape FOREIGN KEY (Country) REFERENCES Landscape(Country) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Model
	ADD CONSTRAINT FK_MName_Models FOREIGN KEY (MName) REFERENCES Models(MName) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_MBDate_Models FOREIGN KEY (MBDate) REFERENCES Models(MBDate) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Photographer
	ADD CONSTRAINT FK_PName_Photo FOREIGN KEY (PName) REFERENCES Photo(PName) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_PBDate_Photo FOREIGN KEY (PBDate) REFERENCES Photo(PBDate) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_EPName_Influences FOREIGN KEY (PName) REFERENCES Influences(EPName) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_EPBDate_Influences FOREIGN KEY (PBDate) REFERENCES Influences(EPBDate) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_RPName_Influences FOREIGN KEY (PName) REFERENCES Influences(RPName) ON DELETE CASCADE ON UPDATE CASCADE,
	ADD CONSTRAINT FK_RPBDate_Influences FOREIGN KEY (PBDate) REFERENCES Influences(RPBDate) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Transaction
	ADD CONSTRAINT FK_TransID_Photo FOREIGN KEY (TransID) REFERENCES Photo(TransID) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE Customer
	ADD CONSTRAINT FK_LoginName_Transaction FOREIGN KEY (LoginName) REFERENCES Transaction(LoginName) ON DELETE CASCADE ON UPDATE CASCADE;