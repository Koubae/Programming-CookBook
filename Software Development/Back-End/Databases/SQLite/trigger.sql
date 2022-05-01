-- sqlite

-- Syntax
CREATE TRIGGER [IF NOT EXISTS] trigger_name 
   [BEFORE|AFTER|INSTEAD OF] [INSERT|UPDATE|DELETE] 
   ON table_name
   [WHEN condition]
BEGIN
 statements;
END;

/* ============================ < Example BEFORE INSERT > ============================ */

CREATE TABLE leads (
	id integer PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	phone text NOT NULL,
	email text NOT NULL,
	source text NOT NULL
);

--validate the email address before inserting a new lead into the leads table
CREATE TRIGGER validate_email_before_insert_leads 
   BEFORE INSERT ON leads
BEGIN
   SELECT
      CASE
	WHEN NEW.email NOT LIKE '%_@__%.__%' THEN
   	  RAISE (ABORT,'Invalid email address')
       END;
END;

--SQLite issued an error: “Invalid email address” and aborted the execution of the insert.
INSERT INTO leads (first_name,last_name,email,phone)
VALUES('John','Doe','jjj','4089009334');


INSERT INTO leads (first_name, last_name, email, phone)
VALUES ('John', 'Doe', 'john.doe@sqlitetutorial.net', '4089009334');

/* ============================ < Example AFTER UPDATE > ============================ */


CREATE TABLE lead_logs (
	id INTEGER PRIMARY KEY,
	old_id int,
	new_id int,
	old_phone text,
	new_phone text,
	old_email text,
	new_email text,
	user_action text,
	created_at text
);


CREATE TRIGGER log_contact_after_update 
   AFTER UPDATE ON leads
   WHEN old.phone <> new.phone
        OR old.email <> new.email
BEGIN
	INSERT INTO lead_logs (
		old_id,
		new_id,
		old_phone,
		new_phone,
		old_email,
		new_email,
		user_action,
		created_at
	)
VALUES
	(
		old.id,
		new.id,
		old.phone,
		new.phone,
		old.email,
		new.email,
		'UPDATE',
		DATETIME('NOW')
	) ;
END;


UPDATE leads
SET 
   phone = '4089998888',
   email = 'john.smith@sqlitetutorial.net'
WHERE
   id = 1;


/* ============================ < Example DROP TRIGGER > ============================ */

-- Syntax
DROP TRIGGER [IF EXISTS] trigger_name;
-- i. e.
DROP TRIGGER validate_email_before_insert_leads;


-- FAQ:
You often use triggers to enable sophisticated auditing. For example, you want to log the changes in the sensitive data such as salary and address whenever it changes.

In addition, you use triggers to enforce complex business rules centrally at the database level and prevent invalid transactions.

-- FAQ:
If you combine the time when the trigger is fired and the event that causes the trigger to be fired, you have a total of 9 possibilities:

    BEFORE INSERT
    AFTER INSERT
    
    BEFORE UPDATE
    AFTER UPDATE
    
    BEFORE DELETE
    AFTER DELETE
    
    INSTEAD OF INSERT
    INSTEAD OF DELETE
    INSTEAD OF UPDATE

