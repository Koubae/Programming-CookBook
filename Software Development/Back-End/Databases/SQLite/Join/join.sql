/* ============================ < INNER JOIN > ============================ */

SELECT 
    Title,
    Name
FROM 
    albums
INNER JOIN artists 
    ON artists.ArtistId = albums.ArtistId;


-- Alias
SELECT
    l.Title, 
    r.Name
FROM
    albums l
INNER JOIN artists r ON
    r.ArtistId = l.ArtistId;


-- In case the column names of joined tables are the same e.g., ArtistId,
-- NOTE: The clause USING(ArtistId) is equipvalent to the clause ON artists.ArtistId = albums.ArtistId.
SELECT
   Title, 
   Name
FROM
   albums
INNER JOIN artists USING(ArtistId);


/* ============================ < LEFT JOIN > ============================ */


SELECT
	a,
	b
FROM
	A
LEFT JOIN B ON A.f = B.f
WHERE search_condition;


SELECT
    Name, 
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
ORDER BY Name;


SELECT
    Name, 
    Title
FROM
    artists
LEFT JOIN albums USING (ArtistId)
ORDER BY
    Name;


SELECT
    Name,
    Title
FROM
    artists
LEFT JOIN albums ON
    artists.ArtistId = albums.ArtistId
WHERE Title IS NULL   
ORDER BY Name;


SELECT m.firstname || ' ' || m.lastname AS 'Manager',
       e.firstname || ' ' || e.lastname AS 'Direct report' 
FROM employees e
LEFT JOIN employees m ON m.employeeid = e.reportsto
ORDER BY manager;



/* ============================ < CROSS JOIN > ============================ */

SELECT
    select_list
FROM table1
CROSS JOIN table2;

CREATE TABLE products(
    product text NOT null
);

INSERT INTO products(product)
VALUES('P1'),('P2'),('P3');



CREATE TABLE calendars(
    y int NOT NULL,
    m int NOT NULL
);

INSERT INTO calendars(y,m)
VALUES 
    (2019,1),
    (2019,2),
    (2019,3),
    (2019,4),
    (2019,5),
    (2019,6),
    (2019,7),
    (2019,8),
    (2019,9),
    (2019,10),
    (2019,11),
    (2019,12);

SELECT * 
FROM products
CROSS JOIN calendars;

-- Card Deck

CREATE TABLE ranks (
    rank TEXT NOT NULL
);

CREATE TABLE suits (
    suit TEXT NOT NULL
);

INSERT INTO ranks(rank) 
VALUES('2'),('3'),('4'),('5'),('6'),('7'),('8'),('9'),('10'),('J'),('Q'),('K'),('A');

INSERT INTO suits(suit) 
VALUES('Clubs'),('Diamonds'),('Hearts'),('Spades');


SELECT rank,
       suit
  FROM ranks
       CROSS JOIN
       suits
ORDER BY suit;

/* ============================ < INNER JOIN > ============================ */

SELECT a1, a2, b1, b2
FROM A
INNER JOIN B on B.f = A.f;


SELECT
	trackid,
	name,
	title
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid;


SELECT
    trackid,
    name,
    tracks.albumid AS Tracks_id,
    albums.albumid AS Album_id,
    title
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid;


-- 3 Tables
SELECT
    trackid,
    tracks.name AS track,
    albums.title AS album,
    artists.name AS artist
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid
    INNER JOIN artists ON artists.artistid = albums.artistid;


SELECT
	trackid,
	tracks.name AS Track,
	albums.title AS Album,
	artists.name AS Artist
FROM
	tracks
INNER JOIN albums ON albums.albumid = tracks.albumid
INNER JOIN artists ON artists.artistid = albums.artistid
WHERE
	artists.artistid = 10;


SELECT
    trackid,
    tracks.name AS track,
    albums.title AS album,
    artists.name AS artist,
    artists.ArtistId AS artist_id
FROM
    tracks
    INNER JOIN albums ON albums.albumid = tracks.albumid
    INNER JOIN artists ON artists.artistid = albums.artistid
WHERE
    artists.ArtistId = 10;


SELECT m.firstname || ' ' || m.lastname AS 'Manager',
       e.firstname || ' ' || e.lastname AS 'Direct report' 
FROM employees e
LEFT JOIN employees m ON m.employeeid = e.reportsto
ORDER BY manager;


/* ============================ < FULL OUTER JOIN > ============================ */

-- create and insert data into the dogs table
CREATE TABLE dogs (
    type       TEXT,
    color TEXT
);

INSERT INTO dogs(type, color) 
VALUES('Hunting','Black'), ('Guard','Brown');

-- create and insert data into the cats table
CREATE TABLE cats (
    type       TEXT,
    color TEXT
);

INSERT INTO cats(type,color) 
VALUES('Indoor','White'), 
      ('Outdoor','Black');


-- Query
SELECT d.type,
         d.color,
         c.type,
         c.color
FROM dogs d
LEFT JOIN cats c USING(color)
UNION ALL
SELECT d.type,
         d.color,
         c.type,
         c.color
FROM cats c
LEFT JOIN dogs d USING(color)
WHERE d.color IS NULL;

-- Warning --> This won't work  SQLite does not support the RIGHT JOIN clause and also the FULL OUTER JOIN clause. 
SELECT *
FROM dogs 
FULL OUTER JOIN cats
    ON dogs.color = cats.color;

/* ============================ < SELF JOIN > ============================ */

SELECT DISTINCT
	e1.city,
	e1.firstName || ' ' || e1.lastname AS fullname
FROM
	employees e1
INNER JOIN employees e2 ON e2.city = e1.city 
   AND (e1.firstname <> e2.firstname AND e1.lastname <> e2.lastname)
ORDER BY
	e1.city;