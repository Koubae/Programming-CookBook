


/*===================================================================*/
/* ============================ < Dump > ============================ */
/*===================================================================*/

.output c:/sqlite/chinook.sql
.dump
.exit


-- Dump a specific table 
.output c:/sqlite/albums.sql
.dump albums
.quit

-- Dump tables structure
.output c:/sqlite/chinook_structure.sql
.schema
.quit

-- From now on, every SELECT statement will issue the result as the INSERT statements instead of pure text data.
.mode insert
.output data.sql
select * from artists;



-- FAQ:
.dump command that gives you the ability to dump the entire database or tables into a text file.

To dump a database into a file, you use the .dump command. The .dump command converts the entire structure and data of an SQLite database into a single text file.

/*=========================================================================================*/
/* ============================ < Import | Export a CSV File > ============================ */
/*=========================================================================================*/

-- Import
.mode csv
.import c:/sqlite/city_no_header.csv cities


-- Export

.headers on
.mode csv
.output data.csv

SELECT 
    customerid,
    firstname,
    lastname,
    company
FROM
    customers;

.quit

-- Short form
 -header -csv c:/sqlite/chinook.db "select * from tracks;" > tracks.csv

-- file named query.sql that contains the script to query data, you can execute the statements in the file and export data to a CSV file.
 
 -header -csv c:/sqlite/chinook.db < query.sql > data.csv
