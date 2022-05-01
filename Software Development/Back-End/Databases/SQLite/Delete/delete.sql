-- sqlite

-- Syntax
DELETE FROM table
WHERE search_condition;


/* ============================ < compile-time option > ============================ */
--NOTE  SQLITE_ENABLE_UPDATE_DELETE_LIMIT

--Syntax
DELETE FROM table
WHERE search_condition
ORDER BY criteria
LIMIT row_count OFFSET offset;


/* ============================ < Example > ============================ */


-- create artists backup table
CREATE TABLE artists_backup(
   artistid INTEGER PRIMARY KEY AUTOINCREMENT,
   name NVARCHAR
);
-- populate data from the artists table
INSERT INTO artists_backup 
SELECT artistid,name
FROM artists;

DELETE FROM artists_backup
WHERE artistid = 1;

-- LIKE
DELETE FROM artists_backup
WHERE name LIKE '%Santana%';

-- DELETE ALL rows   | just need to omit the WHERE clause
DELETE FROM artists_backup;