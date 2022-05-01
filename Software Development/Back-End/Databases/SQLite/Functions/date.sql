--sqlite

-- Syntax
-- date(datetimestring, [modifier1, modifier2…, modifierN])
--  https://www.tutlane.com/tutorial/sqlite/sqlite-date-function

-- SO8601 string format i.e. 2016-01-01 10:20:05.123
'YYYY-MM-DD HH:MM:SS.SSS';


/* ============================ < Functions > ============================ */

SELECT datetime('now');


-- Local time
SELECT datetime('now', 'localtime');


-- Julianday
SELECT julianday('now');


-- date | time
date();
time();


--strftime
SELECT strftime('%s','now');

/* ============================ < Example 1 > ============================ */


CREATE TABLE datetime_text(
   d1 text, 
   d2 text
);


INSERT INTO datetime_text (d1, d2)
VALUES(datetime('now'),datetime('now', 'localtime'));


SELECT
	d1,
	typeof(d1),
	d2,
	typeof(d2)
FROM
	datetime_text;

/* ============================ < Example 2 > ============================ */

CREATE TABLE datetime_real(
   d1 real
);

INSERT INTO datetime_real (d1)
VALUES(julianday('now'));

SELECT
	date(d1),
	time(d1)
FROM
	datetime_real;

/* ============================ < Example 3 > ============================ */

--  INTEGER to store UNIX time | number of seconds since 1970-01-01 00:00:00 UTC

CREATE TABLE datetime_int (d1 int);

INSERT INTO datetime_int (d1)
VALUES(strftime('%s','now'));

SELECT datetime(d1,'unixepoch')
FROM datetime_int;

/* ============================ < Many-to-Many Relationships > ============================ */


SELECT date('now');

SELECT date('2016-08-30 12:54:12') as 'DATE()';


-- last day of the year 
SELECT date('now','start of month','+1 month','-1 day') as 'Last Date of the Month';

-- last date of current month for next year.
SELECT date('now','start of month','+13 month','-1 day') as 'Last Date of the Month next year';

-- -date after 4 month from the current date.
SELECT date('now','+4 month');

-- Friendship Day
SELECT date('now', 'start of year', '+7 month', 'weekday 0') as 'Friendship day'