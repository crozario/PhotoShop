INSERT INTO Photographer(PName, PBDate, PBio, PAddress, PNationality)
VALUES ("John", "1990-08-01", "hello my name is john", "1 washington street", "American");

INSERT INTO Photographer(PName, PBDate, PBio, PAddress, PNationality)
VALUES ("Jake", "1990-02-01", "hello my name is jake", "1 jefferson street", "American");

INSERT INTO Influences(EPName, EPBDate, RPName, RPBDate)
VALUES("John", "1990-08-01", "Jake", "1990-02-01")


select * from Influences;
select * from Photographer;
DELETE FROM Photographer WHERE PName = "Jake" and PBDate = "1990-02-01";