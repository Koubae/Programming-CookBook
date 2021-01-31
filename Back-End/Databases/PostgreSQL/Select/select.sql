
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
    