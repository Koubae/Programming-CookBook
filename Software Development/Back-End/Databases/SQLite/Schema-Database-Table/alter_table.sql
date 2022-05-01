-- sqlite

-- Syntax
ALTER TABLE existing_table
RENAME TO new_table;

-- syntax of ALTER TABLE ADD COLUMN statement
ALTER TABLE table_name
ADD COLUMN column_definition;


-- syntax of the ALTER TABLE RENAME COLUMN statement
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

/* ============================ < Example 1 > ============================ */


CREATE TABLE devices (
   name TEXT NOT NULL,
   model TEXT NOT NULL,
   Serial INTEGER NOT NULL UNIQUE
);

INSERT INTO devices (name, model, serial)
VALUES('HP ZBook 17 G3 Mobile Workstation','ZBook','SN-2015');


ALTER TABLE devices
RENAME TO equipment;

-- ADD COLUMN
ALTER TABLE equipment 
ADD COLUMN location text;

/* ============================ < RENAME COLUMN > ============================ */

CREATE TABLE Locations(
	LocationId INTEGER PRIMARY KEY,
	Address TEXT NOT NULL,
	City TEXT NOT NULL,
	State TEXT NOT NULL,
	Country TEXT NOT NULL
);

INSERT INTO Locations(Address,City,State,Country)
VALUES('3960 North 1st Street','San Jose','CA','USA');

ALTER TABLE Locations
RENAME COLUMN Address TO Street;

/* ============================ < ALTER TABLE Workarounds > ============================ */

-- disable foreign key constraint check
PRAGMA foreign_keys=off;

-- start a transaction
BEGIN TRANSACTION;

-- Here you can drop column
CREATE TABLE IF NOT EXISTS new_table( 
   column_definition,
   ...
);
-- copy data from the table to the new_table
INSERT INTO new_table(column_list)
SELECT column_list
FROM table;

-- drop the table
DROP TABLE table;

-- rename the new_table to the table
ALTER TABLE new_table RENAME TO table; 

-- commit the transaction
COMMIT;

-- enable foreign key constraint check
PRAGMA foreign_keys=on;



-- example
CREATE TABLE users(
	UserId INTEGER PRIMARY KEY,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Email TEXT NOT NULL,
	Phone TEXT NOT NULL
);

CREATE TABLE favorites(
	UserId INTEGER,
	PlaylistId INTEGER,
	FOREIGN KEY(UserId) REFERENCES users(UserId),
	FOREIGN KEY(PlaylistId) REFERENCES playlists(PlaylistId)
);

INSERT INTO users(FirstName, LastName, Email, Phone)
VALUES('John','Doe','john.doe@example.com','408-234-3456');

INSERT INTO favorites(UserId, PlaylistId)
VALUES(1,1);


CREATE TABLE IF NOT EXISTS persons (
	UserId INTEGER PRIMARY KEY,
	FirstName TEXT NOT NULL,
	LastName TEXT NOT NULL,
	Email TEXT NOT NULL
);

-- copy data from the users to persons table
INSERT INTO persons(UserId, FirstName, LastName, Email)
SELECT UserId, FirstName, LastName, Email 
FROM users;


DROP TABLE users;

ALTER TABLE persons RENAME TO users;

COMMIT;
PRAGMA foreign_keys=on;

-- FAQ:

These are important points you should know before you rename a table:

- The ALTER TABLE only renames a table within a database. You cannot use it to move the table between the attached databases.

- The database objects such as indexes and triggers associated with the table will be associated with the new table.

- If a table is referenced by views or statements in triggers, you must manually change the definition of views and triggers.

-- FAQ restrictions on the new column: 

- The new column cannot have a UNIQUE or PRIMARY KEY constraint.
    
- If the new column has a NOT NULL constraint, you must specify a default value for the column other than a NULL value.

- The new column cannot have a default of CURRENT_TIMESTAMP, CURRENT_DATE, and CURRENT_TIME, or an expression.

- If the new column is a foreign key and the foreign key constraint check is enabled, the new column must accept a default value NULL.

-- FAQ Using SQLite ALTER TABLE to rename a column:
SQLite added the support for renaming a column using ALTER TABLE RENAME COLUMN statement in version 3.20.0