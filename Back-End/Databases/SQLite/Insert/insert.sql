--sqlite

INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);


INSERT INTO artists (name)
VALUES
	("Buddy Rich"),
	("Candido"),
	("Charlie Byrd");


/* ============================ < INSERT Default VALUES  > ============================ */

INSERT INTO artists DEFAULT VALUES;


/* ============================ < INSERT Back Up Table  > ============================ */

CREATE TABLE artists_backup(
   ArtistId INTEGER PRIMARY KEY AUTOINCREMENT,
   Name NVARCHAR
);

INSERT INTO artists_backup 
SELECT ArtistId, Name
FROM artists;


SELECT * FROM artists_backup;