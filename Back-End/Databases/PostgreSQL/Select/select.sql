
--  ========================= < CONCATENATE > ========================= --

SELECT 
    first_name || ' ' || last_name,
    email
FROM 
    customer;


-- With Alias

SELECT
    first_name || ' ' || last_name "full name"
FROM
    customer;
    



-- Select All There there aren't Numbers
-- Here, the ^ character outside of square brackets means the beginning of the field, the $ character means the end of the field, and we require that all characters in between are non-digits. + indicates that there should be at least one such characters. If we would also allow empty strings, then the regex would look like ^[^0-9]*$.

SELECT COUNT(*) FROM my_table WHERE table_record ~ '^[^0-9]+$';


-- If you want the records which would include digits and lower-case letter, then I would expect a regex like:

DELETE FROM myrecords WHERE record ~ '[0-9a-z]';