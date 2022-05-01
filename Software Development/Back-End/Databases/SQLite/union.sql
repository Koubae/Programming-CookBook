/* ============================ < Spec  > ============================ */

-- query_1
UNION /*[ALL]*/
-- query_2
UNION /*[ALL]*/
-- query_3
-- ...;

/* ============================ < Example  > ============================ */

CREATE TABLE t1(
    v1 INT
);
 
INSERT INTO t1(v1)
VALUES(1),(2),(3);
 
CREATE TABLE t2(
    v2 INT
);
INSERT INTO t2(v2)
VALUES(2),(3),(4);

-- UNION
SELECT v1
  FROM t1
UNION
SELECT v2
  FROM t2;


-- UNION ALL
SELECT v1
  FROM t1
UNION ALL
SELECT v2
  FROM t2;


SELECT FirstName, LastName, 'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers;

/* ============================ < UNION + ORDER BY  > ============================ */

SELECT FirstName, LastName, 'Employee' AS Type
FROM employees
UNION
SELECT FirstName, LastName, 'Customer'
FROM customers
ORDER BY FirstName, LastName;