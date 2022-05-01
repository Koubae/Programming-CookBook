--sqlite

SELECT  
    id,
    name
FROM
    tracks
LIMIT 10 OFFSET 10;


SELECT  
    id,
    name
FROM
    tracks
LIMIT 10, 10;