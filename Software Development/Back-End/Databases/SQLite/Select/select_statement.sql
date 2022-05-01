-- sqlite

SELECT DISTINCT /* COLUMN_LIST*/

FROM /* TABLE_LIST*/
    JOIN TABLE ON /*JOIN_CONDITION*/

WHERE /*left_expression COMPARISON_OPERATOR right_expression*/
    = BETWEEN /*int*/ AND /*int*/ |  IN (/*1, 2, 3, ...*/)  | LIKE /*'%ES OR %as'*/

ORDER BY 
    /*COLUMN  OR COLUM INDEX*/ ASC, /*ascending*/
    /*COLUMN OR COLUM INDEX*/ DESC, /*descending*/
    COALESCE (col1,col2,col3,etc)  IS NULL /*OR*/ IS NOT NUll
    CASE WHEN /*col*/ IS NULL 1 ELSE 0 END, /*col..*/
    IFNULL(/*col.., -9999*/)

LIMIT /*COUNT INT*/  OFFSET /*OFFSET*/

GROUP BY /*COLUMN*/

HAVING /*GROUP_FILTER*/
;



SELECT DISTINCT

FROM AS 
    JOIN TABLE ON
WHERE 

ORDER BY


LIMIT  OFFSET

GROUP BY 

HAVING


SELECT
    name,
    milliseconds,
    albumid
FROM 
    tracks
ORDER BY
    3, 2 DESC;




SELECT
	column_1, 
        column_2,
	aggregate_function (column_3)
FROM
	table
GROUP BY
	column_1,
        column_2
HAVING
	search_condition;


/* ============================ < Subquery  > ============================ */


SELECT column_1
FROM table_1
WHERE column_1 = (
   SELECT column_1 
   FROM table_2
);


-- WHERE

SELECT trackid,
       name,
       albumid
FROM tracks
WHERE albumid = (
   SELECT albumid
   FROM albums
   WHERE title = 'Let There Be Rock'
);

SELECT customerid,
       firstname,
       lastname
  FROM customers
 WHERE supportrepid IN (
           SELECT employeeid
             FROM employees
            WHERE country = 'Canada'
);


SELECT albumid,
       title
  FROM albums
 WHERE 10000000 > (
                      SELECT sum(bytes) 
                        FROM tracks
                       WHERE tracks.AlbumId = albums.AlbumId
                  )
 ORDER BY title;


-- FROM 

SELECT
	AVG(album.size),
    SIZE
FROM
	(
		SELECT
			SUM(bytes) SIZE
		FROM
			tracks
		GROUP BY
			albumid
	) AS album;


-- SELECT

SELECT albumid,
       title,
       (
           SELECT count(trackid) 
             FROM tracks
            WHERE tracks.AlbumId = albums.AlbumId
       ) AS tracks_count

FROM albums

ORDER BY tracks_count DESC;


/* ============================ < EXISTS | NOT EXISTS  > ============================ */

NOT EXISTS (subquery)

SELECT
    CustomerId,
    FirstName,
    LastName,
    Company
FROM
    Customers c
WHERE
    EXISTS (
        SELECT 
            1 
        FROM 
            Invoices
        WHERE 
            CustomerId = c.CustomerId
    )
ORDER BY
    FirstName,
    LastName;


-- Variation with IN operator, get the same results

SELECT
   CustomerId, 
   FirstName, 
   LastName, 
   Company
FROM
   Customers c
WHERE
   CustomerId IN (
      SELECT
         CustomerId
      FROM
         Invoices
   )
ORDER BY
   FirstName, 
   LastName;

-- Once the subquery returns the first row, the EXISTS operator stops searching because it can determine the result. On the other hand, the IN operator must scan all rows returned by the subquery to determine the result.

-- Generally speaking, the EXISTS operator is faster than IN operator if the result set returned by the subquery is large. By contrast, the IN operator is faster than the EXISTS operator if the result set returned by the subquery is small.


-- NOT EXISTS

SELECT
   *
FROM
   Artists a
WHERE
   NOT EXISTS(
      SELECT
         1
      FROM
         Albums
      WHERE
         ArtistId = a.ArtistId
   )
ORDER BY Name;