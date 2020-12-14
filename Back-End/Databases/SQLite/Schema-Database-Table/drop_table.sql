-- sqlite

-- Syntax
DROP TABLE [IF EXISTS] [schema_name.]table_name;


/* ============================ < Example 1 > ============================ */

CREATE TABLE IF NOT EXISTS addresses (
   address_id INTEGER PRIMARY KEY,
   house_no TEXT,
   street TEXT,
   city TEXT,
   postal_code TEXT,
   country TEXT
);


CREATE TABLE IF NOT EXISTS people (
   person_id INTEGER PRIMARY KEY,
   first_name TEXT,
   last_name TEXT,
   address_id INTEGER,
   FOREIGN KEY (address_id) 
      REFERENCES addresses (address_id)
);


INSERT INTO addresses ( house_no, street, city, postal_code, country ) 
VALUES ( '3960', 'North 1st Street', 'San Jose ', '95134', 'USA ' ); 

INSERT INTO people ( first_name, last_name, address_id ) 
VALUES ('John', 'Doe', 1);

--  ERR
DROP TABLE addresses;
-- constraint failed

-- To remove the addresses table, you have to:

--     Disable foreign key constraints.
--     Drop the addresses table.
--     Update the address_id in the people table to NULL values.
--     Enable the foreign key constraints.

PRAGMA foreign_keys = OFF;

DROP TABLE addresses;

UPDATE people
SET address_id = NULL;

PRAGMA foreign_keys = ON;


-- FAQ:

SQLite allows you to drop only one table at a time. To remove multiple tables, you need to issue multiple DROP TABLE statements.

If you remove a non-existing table, SQLite issues an error. If you use IF EXISTS option, then SQLite removes the table only if the table exists, otherwise, it just ignores the statement and does nothing.

If you want to remove a table in a specific database, you use the [schema_name.] explicitly.

In case the table has dependent objects such as triggers and indexes, the DROP TABLE statement also removes all the dependent objects.

The DROP TABLE statement performs an implicit  DELETE statement before dropping the table. However, the DROP TABLE statement removes the triggers associated with the table before performing the implicit DELETE statement, therefore, the delete triggers will not fire.


-- NOTE: !!!
====================================================================================
Notice that the DROP TABLE statement deletes the table from the database and the file on disk completely. You will not be able to undo or recover from this action. Therefore, you should perform the DROP TABLE statement with extra caution.
====================================================================================