use db;
DROP TABLE IF EXISTS Room;
CREATE TABLE Room(
    Id INT NOT NULL PRIMARY KEY,
    Name VARCHAR(50)
);

CREATE TABLE Student(
    Id INT NOT NULL PRIMARY KEY,
    Birthday DATE NOT NULL,
    Name VARCHAR(50) NOT NULL,
    Sex VARCHAR(5) NOT NULL,
    RoomId INT NOT NULL,
    FOREIGN KEY (RoomId) REFERENCES Room (Id));

CREATE INDEX Student_Room_Id ON Student(RoomId);