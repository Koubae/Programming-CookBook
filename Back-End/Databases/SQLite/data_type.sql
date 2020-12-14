-- sqlite 

SELECT
	typeof(100),
	typeof(10.0),
	typeof('100'),
	typeof(x'1000'),
	typeof(NULL);


/* ============================ < Example > ============================ */


CREATE TABLE test_datatypes (
	id INTEGER PRIMARY KEY,
	val
);


INSERT INTO test_datatypes (val)
VALUES
	(1), --int
	(2), -- int
	(10.1), --real
	(20.5), -- real
	('A'), --text
	('B'), --text
	(NULL), -- null
	(x'0010'), -- blob
	(x'0011'); -- blob

SELECT
	id,
	val,
	typeof(val)
FROM
	test_datatypes;


--Sort mixed data in the val column
SELECT
	id,
	val,
	typeof(val)
FROM
	test_datatypes
ORDER BY val;


-- FAQ:
-- NULL =>	NULL values mean missing information or unknown.

-- INTEGER => 	Integer values are whole numbers (either positive or negative). An integer can have variable sizes such as 1, 2,3, 4, or 8 bytes.

-- REAL => Real values are real numbers with decimal values that use 8-byte floats.

-- TEXT =>	TEXT is used to store character data. The maximum length of TEXT is unlimited. SQLite supports various character encodings.

-- BLOB => 	BLOB stands for a binary large object that can store any kind of data. The maximum size of BLOB is, theoretically, unlimited.


-- FAQ:
-- SQLite determines the data type of a value based on its data type according to the following rules:

-- >>> If a literal has no enclosing quotes and decimal point or exponent, SQLite assigns the INTEGER storage class.
    
-- >>> If a literal is enclosed by single or double quotes, SQLite assigns the TEXT storage class.
    
-- >>> If a literal does not have quote nor decimal point nor exponent, SQLite assigns REAL storage class.
    
-- >>> If a literal is NULL without quotes, it assigned NULL storage class.
    
-- >>> If a literal has the X’ABCD’ or x ‘abcd’, SQLite assigned BLOB storage class.


-- FAQ: 
-- SQLite provides the following set of rules when it comes to sorting:

-- >>> NULL storage class has the lowest value. It is lower than any other values. Between NULL values, there is no order.
    
-- >>> The next higher storage classes are INTEGER and REAL. SQLite compares INTEGER and REAL numerically.
    
-- >>> The next higher storage class is TEXT. SQLite uses the collation of TEXT values when it compares the TEXT values.
    
-- >>> The highest storage class is the BLOB. SQLite uses the C function memcmp() to compare BLOB values.

-- When you use the ORDER BY clause to sort the data in a column with different storage classes, SQLite performs the following steps:

-- 1. Group values based on storage class: NULL, INTEGER, and REAL, TEXT, and BLOB.
-- 2. Sort the values in each group.