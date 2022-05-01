-- sqlite

-- By default, SQLite operates in auto-commit mode. It means that for each command, SQLite starts, processes, and commits the transaction automatically.

-- First, open a transaction by issuing the BEGIN TRANSACTION command.

BEGIN TRANSACTION;

-- Second, issue SQL statements to select or update data in the database. Note that the change is only visible to the current session (or client).

COMMIT;
-- or 
COMMIT TRANSACTION;

-- If you do not want to save the changes, you can roll back using the ROLLBACK or ROLLBACK TRANSACTION statement:


ROLLBACK;
ROLLBACK TRANSACTION;


/* ============================ < Example > ============================ */

CREATE TABLE accounts ( 
	account_no INTEGER NOT NULL, 
	balance DECIMAL NOT NULL DEFAULT 0,
	PRIMARY KEY(account_no),
        CHECK(balance >= 0)
);

CREATE TABLE account_changes (
	change_no INT NOT NULL PRIMARY KEY,
	account_no INTEGER NOT NULL, 
	flag TEXT NOT NULL, 
	amount DECIMAL NOT NULL, 
	changed_at TEXT NOT NULL 
);

-- Insert
INSERT INTO accounts (account_no,balance)
VALUES (100,20100);

INSERT INTO accounts (account_no,balance)
VALUES (200,10100);


-- Transaction
BEGIN TRANSACTION;

UPDATE accounts
   SET balance = balance - 1000
 WHERE account_no = 100;

UPDATE accounts
   SET balance = balance + 1000
 WHERE account_no = 200;
 
INSERT INTO account_changes(account_no,flag,amount,changed_at) 
VALUES(100,'-',1000,datetime('now'));

INSERT INTO account_changes(account_no,flag,amount,changed_at) 
VALUES(200,'+',1000,datetime('now'));

COMMIT;


-- Rolling back

-- This will fail 
BEGIN TRANSACTION;

UPDATE accounts
   SET balance = balance - 20000
 WHERE account_no = 100;

INSERT INTO account_changes(account_no,flag,amount,changed_at) 
VALUES(100,'-',20000,datetime('now'));
-- err
-- [SQLITE_CONSTRAINT]  Abort due to constraint violation (CHECK constraint failed: accounts)

--rollback
ROLLBACK;

