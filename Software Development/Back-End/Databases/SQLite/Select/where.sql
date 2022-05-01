WHERE column_1 = 100;

WHERE column_2 IN (1,2,3);

WHERE column_3 LIKE 'An%';

WHERE column_4 BETWEEN 10 AND 20;


/* ============================ < SQLite comparison operators > ============================ */


-- =	Equal to
-- <> or !=	Not equal to
-- <	Less than
-- >	Greater than
-- <=	Less than or equal to
-- >=	Greater than or equal to


/* ============================ < SQLite logical operators > ============================ */



-- ALL	returns 1 if all expressions are 1.

-- AND	returns 1 if both expressions are 1, and 0 if one of the expressions is 0.

-- ANY	returns 1 if any one of a set of comparisons is 1.

-- BETWEEN	returns 1 if a value is within a range.

-- EXISTS	returns 1 if a subquery contains any rows.

-- IN	returns 1 if a value is in a list of values.

-- LIKE	returns 1 if a value matches a pattern

-- NOT	reverses the value of other operators such as NOT EXISTS, NOT IN, NOT BETWEEN, etc.

-- OR	returns true if either expression is 1



/* ============================ < Or / in  > ============================ */
SELECT
	name,
	albumid,
	mediatypeid
FROM
	tracks
WHERE
	mediatypeid IN (2, 3);

SELECT
	TrackId,
	Name,
	MediaTypeId
FROM
	Tracks
WHERE
	MediaTypeId = 1 OR MediaTypeId = 2
ORDER BY
	Name ASC;

-- Subquery
SELECT
	TrackId, 
	Name, 
	AlbumId
FROM
	Tracks
WHERE
	AlbumId IN (
		SELECT
			AlbumId
		FROM
			Albums
		WHERE
			ArtistId = 12
	);

/* ============================ < LIKE  > ============================ */


SELECT
	column_list
FROM
	table_name
WHERE
	column_1 LIKE pattern ESCAPE;


SELECT
	name,
	albumid,
	composer
FROM
	tracks
WHERE
	composer LIKE '%Smith%'
ORDER BY
	albumid;


SELECT
	trackid,
	name	
FROM
	tracks
WHERE
	name LIKE '%Wild%';



SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name LIKE '%Br_wn%';


-- ESCAPE
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name LIKE '%10\%%' ESCAPE '\';;


/* ============================ < GLOB  > ============================ */

SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*Man';


SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '?ere*';


-- Digit BETWEEN
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[1-9]*';


--  end with digit
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[1-9]';


-- no digit
SELECT
	trackid,
	name
FROM
	tracks
WHERE
	name GLOB '*[^1-9]*';


/* ============================ < NULL  > ============================ */

SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer = NULL;
ORDER BY 
    Name; 


-- NOT NULL
SELECT
    Name, 
    Composer
FROM
    tracks
WHERE
    Composer IS NOT NULL
ORDER BY 
    Name;