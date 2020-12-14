-- sqlite

-- Syntax

CREATE TABLE [IF NOT EXISTS] [schema_name].table_name (
	column_1 data_type PRIMARY KEY,
   	column_2 data_type NOT NULL,
	column_3 data_type DEFAULT 0,
	column_3 data_type CHECK,
	table_constraints [PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK] 
) [WITHOUT ROWID];



CREATE TABLE author (
    author_id INTEGER NOT NULL PRIMARY KEY,
    first_name VARCHAR,
    last_name VARCHAR
);

CREATE TABLE book (
    book_id INTEGER NOT NULL PRIMARY KEY,
    author_id INTEGER REFERENCES author,
    title VARCHAR
);

CREATE TABLE publisher (
    publisher_id INTEGER NOT NULL PRIMARY KEY,
    name VARCHAR
);


/* ============================ < Example 1 > ============================ */


CREATE TABLE contacts (
	contact_id INTEGER PRIMARY KEY,
	first_name TEXT NOT NULL,
	last_name TEXT NOT NULL,
	email TEXT NOT NULL UNIQUE,
	phone TEXT NOT NULL UNIQUE
);


CREATE TABLE groups (
   group_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);


CREATE TABLE contact_groups(
   contact_id INTEGER,
   group_id INTEGER,
   PRIMARY KEY (contact_id, group_id),
   FOREIGN KEY (contact_id) 
      REFERENCES contacts (contact_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION,
   FOREIGN KEY (group_id) 
      REFERENCES groups (group_id) 
         ON DELETE CASCADE 
         ON UPDATE NO ACTION
);


-- Defining a UNIQUE constraint for multiple columns example
CREATE TABLE shapes(
    shape_id INTEGER PRIMARY KEY,
    background_color TEXT,
    foreground_color TEXT,
    UNIQUE(background_color,foreground_color)
);


/* ============================ < Many-to-Many Relationships > ============================ */

CREATE TABLE IF NOT EXISTS (
    author_id INTEGER REFERENCES author,
    publisher_id INTEGER REFERENCES publisher
)


-- FAQ: 

-- The name of the table cannot start with sqlite_ because it is reserved for the internal use of SQLite.

-- Specify the schema_name to which the new table belongs. The schema can be the main database, temp database or any attached databas

-- Finally, optionally use the WITHOUT ROWID option. By default, a row in a table has an implicit column, which is referred to as the rowid, oid or _rowid_ column. The rowid column stores a 64-bit signed integer key that uniquely identifies the row inside the table. If you don’t want SQLite creates the rowid column, you specify the WITHOUT ROWID option. A table that contains the rowid column is known as a rowid table. Note that the WITHOUT ROWID option is only available in SQLite 3.8.2 or later.

/*============================================================================*/
/* ============================ < AUTOINCREMENT > ============================ */
/*============================================================================*/


CREATE TABLE people (
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);


INSERT INTO people (first_name, last_name)
VALUES('John', 'Doe');


SELECT
   rowid, -- SQLite implicitly  creates a column named rowid
   first_name,
   last_name
FROM
   people;


DROP TABLE people;

CREATE TABLE people (
   person_id INTEGER PRIMARY KEY,
   first_name TEXT NOT NULL,
   last_name TEXT NOT NULL
);



-- FAQ:
-- Whenever you create a table without specifying the WITHOUT ROWID option, you get an implicit auto-increment column called rowid. The rowid column store 64-bit signed integer that uniquely identifies a row in the table.

-- When you create a table that has an INTEGER PRIMARY KEY column, this column is the alias of the rowid column.

-- The maximum value of  therowid column is 9,223,372,036,854,775,807

-- SQLite will find an unused integer and uses it. If SQLite cannot find any unused integer, it will issue an SQLITE_FULL error. On top of that, if you delete some rows and insert a new row, SQLite will try to reuse the rowid values from the deleted rows.


-- FAQ:
-- SQLite recommends that you should not use AUTOINCREMENT attribute because:

-- "The AUTOINCREMENT keyword imposes extra CPU, memory, disk space, and disk I/O overhead and should be avoided if not strictly needed. It is usually not needed."

-- When should you use the AUTOINCREMENT column attribute?

-- The main purpose of using attribute AUTOINCREMENT is to prevent SQLite to reuse a value that has not been used or a value from the previously deleted row.

-- If you don’t have any requirement like this, you should not use the AUTOINCREMENT attribute in the primary key.


/*==========================================================================*/
/* ============================ < Primary Key > ============================ */
/*==========================================================================*/

-- Syntax
CREATE TABLE table_name(
   column_1 INTEGER NOT NULL PRIMARY KEY,
--    ...
);


CREATE TABLE countries (
   country_id INTEGER PRIMARY KEY,
   name TEXT NOT NULL
);

CREATE TABLE languages (
   language_id INTEGER,
   name TEXT NOT NULL,
   PRIMARY KEY (language_id)
);

-- primary key consists of two columns
CREATE TABLE country_languages (
	country_id INTEGER NOT NULL,
	language_id INTEGER NOT NULL,
	PRIMARY KEY (country_id, language_id),
	FOREIGN KEY (country_id) REFERENCES countries (country_id) 
            ON DELETE CASCADE ON UPDATE NO ACTION,
	FOREIGN KEY (language_id) REFERENCES languages (language_id) 
            ON DELETE CASCADE ON UPDATE NO ACTION
);


/* ============================ < ALTER TABLE Workaround > ============================ */

PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE table_name RENAME TO old_table;

-- define the primary key constraint here
CREATE TABLE table_name ( ... );

INSERT INTO table_name SELECT * FROM old_table;

DROP TABLE old_cities;

COMMIT;

PRAGMA foreign_keys=on;

-- Example

CREATE TABLE cities (
PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE cities RENAME TO old_cities;

CREATE TABLE cities (
   id INTEGER NOT NULL PRIMARY KEY,
   name TEXT NOT NULL
);

INSERT INTO cities 
SELECT * FROM old_cities;

DROP TABLE old_cities;

COMMIT;

PRAGMA foreign_keys=on;

-- SQLite GUI tool, you can use the following statement to show the table’s information.
PRAGMA table_info([cities]);

-- FAQ:
-- Notice that if you assign another integer type such as BIGINT and UNSIGNED INT to the primary key column, this column will not be an alias for the rowid column.

-- Because the rowid table organizes its data as a B-tree, querying and sorting data of a rowid table are very fast. It is faster than using a primary key which is not an alias of the rowid.

-- Another important note is that if you declare a column with the INTEGER type and PRIMARY KEY DESC clause, this column will not become an alias for the rowid column.

-- FAQ ALTER TABLE Workaround:

-- Unlike other database systems e.g., MySQL and PostgreSQL, you cannot use the ALTER TABLE statement to add a primary key to an existing table.

-- 1. Set the foreign key constarint check off.

-- 2. Rename the table to another table name (old_table).

-- 3. Create a new table (table) with exact structure of the table that you have been renamed.

-- 4. Copy data from the old_table to the table.

-- 5. Turn on the foreign key constraint check on


/*==========================================================================*/
/* ============================ < Foreign Key > ============================ */
/*==========================================================================*/

--Check SQLite Foreing Key support -> 1: enable, 0: disabled
PRAGMA foreign_keys;

-- disable foreign key constraint
PRAGMA foreign_keys = OFF;
-- enable foreign key constraint
PRAGMA foreign_keys = ON;

-- SQLite foreign key constraint actions
-- Syntax
FOREIGN KEY (foreign_key_columns)
   REFERENCES parent_table(parent_key_columns)
      ON UPDATE action 
      ON DELETE action;


/* ============================ < one-to-many > ============================ */


-- Parent Table 
CREATE TABLE supplier_groups (
	group_id integer PRIMARY KEY, -- Parent Key
	group_name text NOT NULL
);


-- Chile Table 
CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY, 
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER NOT NULL, -- Child Key 
    FOREIGN KEY (group_id)
       REFERENCES supplier_groups (group_id) 
);

INSERT INTO supplier_groups (group_name)
VALUES
   ('Domestic'),
   ('Global'),
   ('One-Time');

INSERT INTO suppliers (supplier_name, group_id)
VALUES ('HP', 2);


/* ============================ < SET NULL > ============================ */


-- Parent Table 
CREATE TABLE supplier_groups (
	group_id integer PRIMARY KEY, -- Parent Key
	group_name text NOT NULL
);


CREATE TABLE suppliers (
    supplier_id   INTEGER PRIMARY KEY,
    supplier_name TEXT    NOT NULL,
    group_id      INTEGER,
    FOREIGN KEY (group_id)
    REFERENCES supplier_groups (group_id) 
       ON UPDATE SET NULL
       ON DELETE SET NULL
);


INSERT INTO suppliers (supplier_name, group_id)
VALUES('XYZ Corp', 3);

INSERT INTO suppliers (supplier_name, group_id)
VALUES('ABC Corp', 3);

DELETE FROM supplier_groups 
WHERE group_id = 3;


-- FAQ:
-- Error if add child Key to Parent Key that doesn't exists.
-- [SQLITE_CONSTRAINT]  Abort due to constraint violation (FOREIGN KEY constraint failed)

-- FAQ:
-- SQLite supports the following actions:

--     SET NULL
-- When the parent key changes, delete or update, the corresponding child keys of all rows in the child table set to NULL.

--     SET DEFAULT
-- The SET DEFAULT action sets the value of the foreign key to the default value specified in the column definition when you create the table.

--     RESTRICT
-- The RESTRICT action does not allow you to change or delete values in the parent key of the parent table.
-- Err:
-- [SQLITE_CONSTRAINT]  Abort due to constraint violation (FOREIGN KEY constraint failed)

--     NO ACTION
-- The NO ACTION does not mean by-pass the foreign key constraint. It has the similar effect as the RESTRICT.

--     CASCADE
-- The CASCADE action propagates the changes from the parent table to the child table when you update or delete the parent key.


/*=====================================================================*/
/* ============================ < CHECK  > ============================ */
/*=====================================================================*/

-- Syntax Table Level
CREATE TABLE table_name(
    ...,
    CHECK(expression)
);

-- Syntax Column Level
CREATE TABLE table_name(
    ...,
    column_name data_type CHECK(expression),
    ...
);

-- Adding CHECK constraints to an existing table
-- o get the structure of the old table, you can use the .schema command
CREATE TABLE new_table (
    [...],
    CHECK ([...])
);

-- Copy Data from old table to new table
INSERT INTO new_table SELECT * FROM old_table;

-- Drop old table
DROP TABLE old_table;

-- rename new table to old dropped table
ALTER TABLE new_table RENAME TO old_table;

-- transaction-safe
BEGIN;
-- create a new table 
CREATE TABLE new_table (
    [...],
    CHECK ([...])
);
-- copy data from old table to the new one
INSERT INTO new_table SELECT * FROM old_table;

-- drop the old table
DROP TABLE old_table;

-- rename new table to the old one
ALTER TABLE new_table RENAME TO old_table;

-- commit changes
COMMIT;

/* ============================ < Example 1 > ============================ */

-- The following statement creates a new table
CREATE TABLE contacts (
    contact_id INTEGER PRIMARY KEY,
    first_name TEXT    NOT NULL,
    last_name  TEXT    NOT NULL,
    email      TEXT,
    phone      TEXT    NOT NULL
                    CHECK (length(phone) >= 10) 
);


/* ============================ < Example 2 > ============================ */

CREATE TABLE products (
    product_id   INTEGER         PRIMARY KEY,
    product_name TEXT            NOT NULL,
    list_price   DECIMAL (10, 2) NOT NULL,
    discount     DECIMAL (10, 2) NOT NULL
                                DEFAULT 0,
    CHECK (list_price >= discount AND 
        discount >= 0 AND 
        list_price >= 0) 
);


-- FAQ:
SQLite CHECK constraints allow you to define expressions to test values whenever they are inserted into or updated within a column.

If the values do not meet the criteria defined by the expression, SQLite will issue a constraint violation and abort the statement.

The CHECK constraints allow you to define additional data integrity checks beyond UNIQUE or NOT NULL to suit your specific application.

SQLite allows you to define a CHECK constraint at the column level or the table level.



/*==========================================================================*/
/* ============================ < Show Tables > ============================ */
/*==========================================================================*/

-- Command
.tables
.table
.ta


--  create a new temporary

CREATE TEMPORARY TABLE temp_table1( name TEXT );


.table 'a%'


-- Showing tables using SQL statement


SELECT 
    name
FROM 
    sqlite_master 
WHERE 
    type ='table' AND 
    name NOT LIKE 'sqlite_%';


/*=============================================================================*/
/* ============================ < Describe Table > ============================ */
/*=============================================================================*/


-- Syntax

.schema table_name

-- show the structure of a table is to use the following PRAGMA command

.header on
.mode column
pragma table_info('albums');

-- structure of a table using the SQL statement
SELECT sql 
FROM sqlite_master 
WHERE name = 'albums';

