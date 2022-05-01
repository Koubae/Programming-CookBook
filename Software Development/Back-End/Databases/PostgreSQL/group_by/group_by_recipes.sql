-- CREDIT ---> https://stackoverflow.com/a/41174185/13903942

-- ------------------------------------------------------------------------------------------------------------------------- --

-- GROUP BY with one parameter:
SELECT column_name, AGGREGATE_FUNCTION(column_name)
FROM table_name
WHERE column_name operator value
GROUP BY column_name;

-- ------------------------------------------------------------------------------------------------------------------------- --


-- GROUP BY with two parameters:
SELECT
    column_name1,
    column_name2,
    AGGREGATE_FUNCTION(column_name3)
FROM
    table_name
GROUP BY
    column_name1,
    column_name2;
Remember this order:

-- SELECT (is used to select data from a database)

-- FROM (clause is used to list the tables)

-- WHERE (clause is used to filter records)

-- GROUP BY (clause can be used in a SELECT statement to collect data across multiple records and group the results by one or more columns)

-- HAVING (clause is used in combination with the GROUP BY clause to restrict the groups of returned rows to only those whose the condition is TRUE)

-- ORDER BY (keyword is used to sort the result-set)

-- You can use all of these if you are using aggregate functions, and this is the order that they must be set, otherwise you can get an error.

-- Aggregate Functions are:

-- MIN() returns the smallest value in a given column

-- MAX() returns the maximum value in a given column.

-- SUM() returns the sum of the numeric values in a given column

-- AVG() returns the average value of a given column

-- COUNT() returns the total number of values in a given column

-- COUNT(*) returns the number of rows in a table

-- SQL script examples about using aggregate functions:

-- Let's say we need to find the sale orders whose total sale is greater than $950. We combine the HAVING clause and the GROUP BY clause to accomplish this:

SELECT 
    orderId, SUM(unitPrice * qty) Total
FROM
    OrderDetails
GROUP BY orderId
HAVING Total > 950;

-- ------------------------------------------------------------------------------------------------------------------------- --


-- Counting all orders and grouping them customerID and sorting the result ascendant. We combine the COUNT function and the GROUP BY, ORDER BY clauses and ASC:

SELECT 
    customerId, COUNT(*)
FROM
    Orders
GROUP BY customerId
ORDER BY COUNT(*) ASC;

-- ------------------------------------------------------------------------------------------------------------------------- --


-- Retrieve the category that has an average Unit Price greater than $10, using AVG function combine with GROUP BY and HAVING clauses:

SELECT 
    categoryName, AVG(unitPrice)
FROM
    Products p
INNER JOIN
    Categories c ON c.categoryId = p.categoryId
GROUP BY categoryName
HAVING AVG(unitPrice) > 10;

-- ------------------------------------------------------------------------------------------------------------------------- --


-- Getting the less expensive product by each category, using the MIN function in a subquery:

SELECT categoryId,
       productId,
       productName,
       unitPrice
FROM Products p1
WHERE unitPrice = (
                SELECT MIN(unitPrice)
                FROM Products p2
                WHERE p2.categoryId = p1.categoryId)

-- ------------------------------------------------------------------------------------------------------------------------- --


-- The following will show you how to select the most recent date item "productDate", using MAX function in a subquery:

SELECT categoryId,
       productId,
       productName,
       unitPrice,
       productDate
FROM Products p1
WHERE productDate= (
                  SELECT MAX(productDate) 
                  FROM Products p2
                  WHERE p2.categoryId = p1.categoryId)

-- ------------------------------------------------------------------------------------------------------------------------- --

-- The following statement groups rows with the same values in both categoryId and productId columns:

SELECT 
    categoryId, categoryName, productId, SUM(unitPrice)
FROM
    Products p
INNER JOIN
    Categories c ON c.categoryId = p.categoryId
GROUP BY categoryId, productId