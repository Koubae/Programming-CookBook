-- sqlite


.databases

--  create a new database
attach database 'c:\sqlite\db\contacts.db' as contacts;

-- Create table + Insert Values

CREATE TABLE contacts.people(first_name text, last_name text);

INSERT INTO contacts.people SELECT firstName, lastName FROM customers;

-- Query Data

SELECT * FROM contacts.people;



-- FAQ:  https://www.sqlite.org/lang_attach.html
-- In case you want to create a new memory database and attach it to the current database connection, you use :memory: filename.

-- If you specify an empty file name '', the statement creates a temporary file-backed database.

-- Note that SQLite automatically deletes all temporary and memory databases when the database connection is closed.