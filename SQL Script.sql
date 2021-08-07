DROP DATABASE IF EXISTS `book2`;
CREATE DATABASE book2;
USE book2;

DROP TABLE IF EXISTS `User`;

CREATE TABLE User(
UserID    VARCHAR(10) NOT NULL,
Pass      VARCHAR(10) NOT NULL,
Uname     VARCHAR(10) NOT NULL,
PRIMARY KEY(UserID));
    
DROP TABLE IF EXISTS `Admin`;
CREATE TABLE Admin(
  AdminID   VARCHAR(10) NOT NULL,
  Pass      VARCHAR(10) NOT NULL,
  Aname 	VARCHAR(10) NOT NULL,
  PRIMARY KEY(AdminID));

DROP TABLE IF EXISTS `Book`;

CREATE TABLE Book(
  BookID    VARCHAR(25) NOT NULL,
  Title     VARCHAR(60) NOT NULL,
  Author    VARCHAR(100) NOT NULL,
  Category  VARCHAR(50),
  Publisher VARCHAR(10),
  YearOfPublication INT(4) NOT NULL,
  PRIMARY KEY(BookID));

DROP TABLE IF EXISTS `BorrowedBooks`;

CREATE TABLE BorrowedBooks(
  BorrowedBookID    VARCHAR(25) NOT NULL,
  BorrowedUserID VARCHAR(10) NOT NULL,
  isExtended TINYINT(1),
  DueDate DATE NOT NULL,
  BorrowedDate DATE NOT NULL,
  PRIMARY KEY (BorrowedBookID, BorrowedUserID),
  FOREIGN KEY (`BorrowedBookID`) REFERENCES `Book` (`BookID`) ON DELETE CASCADE
  ON UPDATE CASCADE);
  
DROP TABLE IF EXISTS `ReservedBooks`;
  
  CREATE TABLE ReservedBooks(
  ReservedBookID    VARCHAR(25) NOT NULL,
  ReservedUserID  VARCHAR(10) NOT NULL,
  ReservedDate DATE NOT NULL,
  PRIMARY KEY (ReservedBookID, ReservedUserID),
  FOREIGN KEY (`ReservedBookID`) REFERENCES `Book` (`BookID`) ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (`ReservedUserID`) REFERENCES `User` (`UserID`) ON DELETE CASCADE
  ON UPDATE CASCADE);

    
DROP TABLE IF EXISTS `Fine`;
    
CREATE TABLE Fine(
  UserID    VARCHAR(10) NOT NULL,
  FineAmount INT DEFAULT 0,
  MemberUserID VARCHAR(10) NOT NULL,
  PRIMARY KEY(UserID),
  FOREIGN KEY (`MemberUserID`) REFERENCES `User` (`UserID`) ON DELETE CASCADE
  ON UPDATE CASCADE);
    
DROP TABLE IF EXISTS `Payment`;

CREATE TABLE Payment(
  PaymentMethod VARCHAR(10) NOT NULL,
  UserID    VARCHAR(10) NOT NULL,
  TransactionID INT AUTO_INCREMENT PRIMARY KEY, 
  PaymentAmount INT,
  FineUserID 	VARCHAR(10) NOT NULL,
  FOREIGN KEY (`UserID`) REFERENCES `Fine` (`UserID`) ON DELETE CASCADE
  ON UPDATE CASCADE,
  FOREIGN KEY (`FineUserID`) REFERENCES `User` (`UserID`) ON DELETE CASCADE
  ON UPDATE CASCADE);
  
INSERT INTO book
VALUES (1, "Unlocking Android", "['W. Frank Ableson', 'Charlie Collins', 'Robi Sen']" , "['Open Source', 'Mobile']", NULL,  2004),
(3, "Specification by Example", "['Gojko Adzic']" , "['Software Engineering']", NULL,  2011),
 (2, "Android in Action, Second Edition", "['W. Frank Ableson', 'Robi Sen']" , "['Java']", NULL, 2011),
(4, "Flex 3 in Action", "['Tariq Ahmed with Jon Hirschi', 'Faisal Abid']" , "['Internet']", NULL, 2009),
 (5, "Flex 4 in Action", "['Tariq Ahmed', 'Dan Orlando', 'John C. Bland II', 'Joel Hooks']" , "['Internet']", NULL, 2009),
 (6, "Specification by Example", "['Gojko Adzic']" , "['Software Engineering']", NULL,  2011),
 (7, "Android in Action, Second Edition", "['W. Frank Ableson', 'Robi Sen']" , "['Java']", NULL, 2011),
(8, "Flex 3 in Action", "['Tariq Ahmed with Jon Hirschi', 'Faisal Abid']" , "['Internet']", NULL, 2009),
 (9, "Flex 4 in Action", "['Tariq Ahmed', 'Dan Orlando', 'John C. Bland II', 'Joel Hooks']" , "['Internet']", NULL, 2009);
INSERT INTO user
VALUES ("User1", "pass1", "John"),
("User2", "pass2", "Patrick"),
("User3", "pass3", "Bob");

INSERT INTO borrowedbooks
VALUES (2, "User1", 0, "2021-03-29","2021-03-01" ),
(3, "User2", 0, "2021-03-29","2021-03-01" ),
(4, "User3", 0, "2021-03-28","2021-02-28" );

INSERT INTO reservedbooks
VALUES (3, "User3",  "2021-03-23"),
(1, "User3", "2021-03-24");

INSERT INTO fine
VALUES ("User1", 10, "User1"),
("User2", 0, "User2"),
("User3", 0, "User3");

INSERT INTO admin
VALUES ("Admin1", "pass", "Tom");

#DROP EVENT `event_name`;
CREATE EVENT `event_name` 
ON SCHEDULE EVERY 1 DAY
ON COMPLETION PRESERVE 
DO
update fine
set FineAmount = (FineAmount + (SELECT COUNT(*) FROM borrowedbooks WHERE ((curdate() > DueDate) AND (BorrowedUserID = UserID))));

#DROP EVENT `event_name2`;
CREATE EVENT `event_name2` 
ON SCHEDULE EVERY 10 SECOND
ON COMPLETION PRESERVE 
DO
delete from reservedbooks WHERE ReservedUserID IN (SELECT UserID FROM fine WHERE (FineAmount > 0))