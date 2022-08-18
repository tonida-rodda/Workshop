CREATE TABLE IF NOT EXISTS User ( 
    Id int(11) NOT NULL AUTO_INCREMENT,
    Email varchar(250) UNIQUE NOT NULL,
    Password varchar(250) NOT NULL,
    PRIMARY KEY (Id)
)

CREATE TABLE IF NOT EXISTS invent (
    Id int(11) NOT NULL AUTO AUTO_INCREMENT,
    user_id int,
    todo varchar(250) NOT NULL
);

CREATE TABLE Orders (
    OrderID int,
    OrderNumber int NOT NULL,
    PersonID int,
    PRIMARY KEY (OrderID),
    FOREIGN KEY (PersonID) REFERENCES User(Id)
);