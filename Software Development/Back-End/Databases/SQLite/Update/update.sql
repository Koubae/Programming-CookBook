--sqlite

-- Syntax

UPDATE table

SET /*column_1 = new_value_1,
    column_2 = new_value_2*/

WHERE
    -- search_condition

ORDER /*column_or_expression*/

LIMIT /*row_count*/ OFFSET /*offset*/;



/* ============================ < Update one column > ============================ */

UPDATE employees
SET lastname = 'Smith'
WHERE employeeid = 3;


/* ============================ < Update multiple columns > ============================ */

UPDATE employees
SET city = 'Toronto',
    state = 'ON',
    postalcode = 'M5P 2N7'
WHERE
    employeeid = 4;

/* ============================ < Update with ORDER BY and LIMIT > ============================ */

-- NOTE: The LOWER() function converts the email to lower case.
UPDATE employees
SET email = LOWER(
	firstname || "." || lastname || "@fedeb.com"
)
ORDER BY
	firstname
LIMIT 1;


/* ============================ < Update all rows> ============================ */


UPDATE employees
SET email = LOWER(
	firstname || "." || lastname || "@chinookcorp.com"
);