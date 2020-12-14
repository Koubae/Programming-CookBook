-- sqlite

-- Syntax

CREATE [UNIQUE] INDEX index_name 
ON table_name(column_list);

-- Remove Index From Database
DROP INDEX [IF EXISTS] index_name;
-- i.E
DROP INDEX idx_contacts_name;

CREATE TABLE contacts (
	first_name text NOT NULL,
	last_name text NOT NULL,
	email text NOT NULL
);

CREATE UNIQUE INDEX idx_contacts_email 
ON contacts (email);


--To check if SQLite uses the index or not, you use the EXPLAIN QUERY PLAN statement
EXPLAIN QUERY PLAN 
SELECT
	first_name,
	last_name,
	email
FROM
	contacts
WHERE
	email = 'lisa.smith@sqlitetutorial.net';


-- creates a multicolumn index 
CREATE INDEX idx_contacts_name 
ON contacts (first_name, last_name);

-- SQLite Show Indexes
PRAGMA index_list('table_name');

PRAGMA index_list('playlist_track');

--  get all indexes from a databasequery from the sqlite_master
SELECT
   type, 
   name, 
   tbl_name, 
   sql
FROM
   sqlite_master
WHERE
   type= 'index';