# SQLite
=======================

- [SQLite DOCS](https://www.sqlite.org/docs.html)
- [Features Of SQLite](https://www.sqlite.org/features.html)


* SQLite is a transactional database that all changes and queries are atomic, consistent, isolated and durable:  ***ACID***


-----------------------------------------------------------------------------------------------------

Installation
------------

1. Download Binaries in the download page [here](https://www.sqlite.org/download.html) called *sqlite-tools-win32-x86-3340000.zip*

2. Create a Folder and extract the zip file

### SQLite GUI tool

- [SQLiteStudio](https://sqlitestudio.pl/)
- [SQLiteStudio --DOWNLOAD-- ](https://github.com/pawelsalawa/sqlitestudio/releases)
- [SQLiteStudio User_Manual](https://github.com/pawelsalawa/sqlitestudio/wiki/User_Manual)

- [DBeaver](https://dbeaver.io/)

- [DB Browser for SQLite](https://sqlitebrowser.org/)


-----------------------------------------------------------------------------------------------------

Documentation
-------------

## sqlite_stat1

- [The SQLite Query Optimizer Overview ](https://www.sqlite.org/optoverview.html)
- [sqlite_stat1](https://www.sqlite.org/src/artifact/a425d62e8?ln=309-325)

## Select

* INNER JOIN or LEFT JOIN  => query data from multiple tables using joins.

* WHERE => filter rows.

* ORDER BY column => sort the result set.

* LIMIT / OFFSET => constrain number of rows returned

* GROUP BY => get the groups rows into groups + add aggregate function to each group.

* HAVING => filter GROUP BY

#### DISTINCT

**REMOVE DUPLICATES**

The DISTINCT clause is an optional clause of the  SELECT statement. **The DISTINCT clause allows you to remove the duplicate rows in the result set.**

SQLite considers NULL values as duplicates. If you use theDISTINCT clause with a column that has NULL values, SQLite will keep one row of a NULL value.

> In database theory, if a column contains NULL values, it means that we do not have the information about that column of particular records or the information is not applicable.


#### WHERE

Filter rows

When evaluating a SELECT statement with a WHERE clause, SQLite uses the following steps:

1. Check the table in the FROM clause.
2. Evaluate the conditions in the WHERE clause to get the rows that met these conditions.
3. Make the final result set based on the rows in the previous step with columns in the SELECT clause.

```
left_expression COMPARISON_OPERATOR right_expression
```

Besides the SELECT statement, you can use the WHERE clause in the UPDATE and DELETE statements.

#### BETWEEN Operator

The BETWEEN operator is a logical operator that tests whether a value is in range of values. If the value is in the specified range, the BETWEEN operator returns true. 
The BETWEEN operator can be used in the **WHERE** clause of:

- SELECT 
- DELETE
- UPDATE
- REPLACE 

```
test_expression BETWEEN low_expression AND high_expression

test_expression >= low_expression AND test_expression <= high_expression
```

*Note that if any input to the BETWEEN operator is NULL, the result is NULL, or unknown to be precise.*

To negate the result of the BETWEEN operator, you use the NOT BETWEEN operator as follows:

```
test_expression NOT BETWEEN low_expression AND high_expression

test_expression < low_expression OR test_expression > high_expression
```

#### LIKE

Can also use the LIKE operator in the WHERE clause of other statements such as the DELETE and UPDATE.

SQLite provides two wildcards for constructing patterns. They are percent sign % and underscore _ :

1. The percent sign % wildcard matches any sequence of zero or more characters.
2. The underscore _ wildcard matches any single character.

**For Unicode characters that are not in the ASCII ranges, the LIKE operator is case sensitive e.g., "Ä" LIKE "ä" is false.**

In case you want to make LIKE operator works case-sensitively, you need to use the following PRAGMA:
```
PRAGMA case_sensitive_like = true;
```

###### ESCAPE

When you specify the ESCAPE clause, the LIKE operator will evaluate the expression that follows the ESCAPE keyword to a string which consists of a single character, or an escape character.

```
column_1 LIKE '%10\%%' ESCAPE '\';
```

#### GLOB

The GLOB operator is similar to the LIKE operator. The GLOB operator determines whether a string matches a specific pattern.

Unlike the LIKE operator, the GLOB operator is case sensitive and uses the UNIX wildcards. In addition, the GLOB patterns do not have escape characters.

The following shows the wildcards used with the GLOB  operator:

1. The asterisk (*) wildcard matches any number of characters.
2. The question mark (?) wildcard matches exactly one character.

* **[xyz]** match any single x, y, or z character.

* **[a-zA-Z0-9]**  pattern matches any single alphanumeric character, both lowercase, and uppercase.

* **[^0-9]** pattern matches any single character except a numeric character.


### Join | Relationships

*Note that SQLite doesn’t directly support the RIGHT JOIN and FULL OUTER JOIN.*

If you use a LEFT JOIN, INNER JOIN, or CROSS JOIN without the ON or USING clause, SQLite produces the Cartesian product of the involved tables. The number of rows in the Cartesian product is the product of the number of rows in each involved tables.

* INNER JOIN

* LEFT JOIN

* CROSS JOIN

#### INNTER JOIN

![img](img\inner-join.png)

**Selects only the intersection**

To query data from multiple tables, you use INNER JOIN clause. The INNER JOIN clause combines columns from correlated tables.

#### LEFT JOIN

![img](img\left-join.png)


**Select ALL left table + intersaction of other/s table/s**

*Note that LEFT JOIN and LEFT OUTER JOIN are synonyms.*

Generally, this type of query allows you to find rows that are available in the left table but don’t have corresponding rows in the right table.

```

SELECT
	a,
	b
FROM
	A
LEFT JOIN B ON A.f = B.f
WHERE search_condition;

```

1. Rows in table A (left table) that have corresponding rows in table B.
2. Rows in the table A table and the rows in the table B filled with NULL values in case the row from table A does not have any corresponding rows in table B.


#### FULL OUTER JOIN

![img](img\full-outer-join.png)

The result of the FULL OUTER JOIN is a combination of  a LEFT JOIN and a RIGHT JOIN. 

Unfortunately, SQLite does not support the RIGHT JOIN clause and also the FULL OUTER JOIN clause. However, you can easily emulate the FULL OUTER JOIN by using the LEFT JOIN clause.


#### CROSS JOIN

The CROSS JOIN clause creates a [Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of rows from the joined tables.

#### SELF JOIN

### GROUP BY

The GROUP BY clause returns one row for each group. 
For each group, you can apply an aggregate function such as :

- MIN
- MAX 
- SUM 
- COUNT
- AVG

#### HAVING

Group by's filter.

***Note that the HAVING clause is applied after GROUP BY clause, whereas the WHERE clause is applied before the GROUP BY clause.***

You often use the **HAVING** clause with the GROUP BY clause. The GROUP BY clause groups a set of rows into a set of summary rows or groups. Then the HAVING clause filters groups based on a specified condition.

--------------------------------

### UNION | UNION ALL

UNION operator combines result sets of two or more queries into a single result set.

The UNION operator removes eliminate duplicate rows, whereas the UNION ALL operator does not.

*Because the UNION ALL operator does not remove duplicate rows, it runs **faster** than the UNION operator.*

The following are rules to union data:

- The number of columns in all queries must be the same.
- The corresponding columns must have compatible data types.
- The column names of the first query determine the column names of the combined result set.
- The GROUP BY and HAVING clauses are applied to each individual query, not the final result set.
- The ORDER BY clause is applied to the combined result set, not within the individual result set.

*Note that the difference between UNION and JOIN e.g., INNER JOIN or LEFT JOIN is that the JOIN clause combines columns from multiple related tables, while UNION combines rows from multiple similar tables.*


### EXCEPT


SQLite EXCEPT operator compares the result sets of two queries and returns distinct rows from the left query that are not output by the right query.

This query must conform to the following rules:

1. he number of columns in the select lists of both queries must be the same.
2. The order of the columns and their types must be comparable.


### INTERSECT

SQLite INTERSECT operator compares the result sets of two queries and returns distinct rows that are output by both queries.

The basic rules for combining the result sets of two queries are as follows:

1. The number and the order of the columns in all queries must be the same.

2. tTe data types must be comparable.

--------------------------------

### EXISTS | NOT EXISTS


If the subquery returns one or more row, the EXISTS operator return true. Otherwise, the EXISTS operator returns false or NULL.

Note that if the subquery returns one row with NULL, the result of the EXISTS operator is still true because the result set contains one row with NULL.


--------------------------------

### CASE  | simple CASE | searched CASE

The CASE expression is similar to the IF-THEN-ELSE statement in other programming languages.

Can use the CASE in statements:

- SELECT
- UPDATE
- DELETE

Can use the CASE expression in clauses:

- WHERE
- ORDER BY
- HAVING
- SELECT

The simple CASE expression compares the case_expression to the expression appears in the first WHEN clause, when_expression_1, for equality. If you omit the ELSE clause, the CASE expression returns NULL.

The searched CASE expression evaluates the Boolean expressions in the sequence specified and return the corresponding result if the expression evaluates to true.

-----------------------------------------------------------------------------------------------------

## INSERT

When you create a new table using the CREATE TABLE statement, you can specify default values for columns, or a NULL if a default value is not specified.

```

INSERT INTO table (column1,column2 ,..)
VALUES( value1,	value2 ,...);

```

Multiple values

```

INSERT INTO table1 (column1,column2 ,..)
VALUES 
   (value1,value2 ,...),
   (value1,value2 ,...),
    ...
   (value1,value2 ,...);

```

### REPLACE

The idea of the REPLACE statement is that when a UNIQUE or PRIMARY KEY constraint violation occurs, it does the following:

1. Delete the existing row that causes a constraint violation.
2. Insert a new row.

In the second step, if any constraint violation e.g., NOT NULL constraint occurs, the REPLACE statement will **abort** the action and **roll back** the **transaction**.



-----------------------------------------------------------------------------------------------------

## UPDATE

If use a negative value in the LIMIT clause, SQLite assumes that there are no limit and updates all rows that meet the condition in the preceding WHERE clause.

The ORDER BY clause should always goes with the LIMIT clause to specify exactly which rows to be updated. Otherwise, you will never know which row will be actually updated; because without the ORDER BY clause, the order of rows in the table is unspecified.

-----------------------------------------------------------------------------------------------------


## DELETE

1. Specify the name of the table which you want to remove rows after the DELETE FROM keywords.

2. Add a search condition in the WHERE clause to identify the rows to remove. The WHERE clause is an optional part of the DELETE statement. If you omit the WHERE clause, the DELETE statement will delete all rows in the table.

SQLite also provides an extension to the DELETE statement by adding ORDER BY and LIMIT clauses. If you compile SQLite with the [SQLITE_ENABLE_UPDATE_DELETE_LIMIT](https://www.sqlite.org/compile.html#enable_update_delete_limit)


Notice that when you use the **DELETE** statement without a **WHERE** clause on a table that has no triggers!! 

SQLite **will delete all rows** in one shot instead of visiting and deleting each individual row. This feature is known as ***truncate optimization.***

-----------------------------------------------------------------------------------------------------



Command-line
------------

* See the tables
```
.table
.tables

# The quotes are mandatory

.table '[table_name]'

# LIKE Operator
.table '&[patter]'

```

* See the databases

```
.database
.databases
```

* Add an additional database

```
ATTACH DATABASE [DATABASE/DIR] AS  [DATABASE ALIAS]
```

* Show structure of table

```
.schema 

# Show schema to specific tables
.schema [table_name]

# Show Content of sqlite_stat
# Show schema and the content of sqlite_stat tables
.fullschema

```

* Table info

```
PRAGMA table_info([cities]);
```


* Show Indexes

```
.indexes

```


* Save query to File

```
.output [file_name]

#  If you want to save the result of the next single query only to the file 
.once [FILENAME] 
```

* Read from file

```
.mode column
.header on
.read [FILE_NAME or Dir]

```

* Quite the programm

```
.q

.exit
```



-----------------------------------------------------------------------------------------------------