-- sqlite

-- Syntax
INSERT OR REPLACE INTO table(column_list)
VALUES(value_list);

-- Equivalen -short form-
REPLACE INTO table(column_list)
VALUES(value_list);



/* ============================ < Example > ============================ */

CREATE TABLE IF NOT EXISTS positions (
	id INTEGER PRIMARY KEY,
	title TEXT NOT NULL,
	min_salary NUMERIC
);


INSERT INTO positions (title, min_salary)
VALUES ('DBA', 120000),
       ('Developer', 100000),
       ('Architect', 150000);


-- Create unique index
CREATE UNIQUE INDEX idx_positions_title 
ON positions (title);

-- Add a title that already exists --DBA--
REPLACE INTO positions (title, min_salary)
VALUES('DBA', 170000);

-- This won't REPLACE the 'Developer' Row because title is not specified hence SQLite rolls back the transaction
REPLACE INTO positions (id, min_salary)
VALUES(2, 110000);

