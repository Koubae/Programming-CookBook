PostgreSQL
========



Installation
------------

```
pip install psycopg2-binary

```

- [Psycopg Installation](https://www.psycopg.org/docs/install.html)


Documentation
-------------

### Transactions

PostgreSQL actually treats every SQL statement as being executed within a transaction. If you do not issue a BEGIN command, then each individual statement has an implicit BEGIN and (if successful) COMMIT wrapped around it. A group of statements surrounded by BEGIN and COMMIT is sometimes called a transaction block.

Some client libraries issue BEGIN and COMMIT commands automatically, so that you might get the effect of transaction blocks without asking. 


It's possible to control the statements in a transaction in a more granular fashion through the use of **savepoints**. 

- **Savepoints** allow you to selectively discard parts of the transaction, while committing the rest. After defining a savepoint with `SAVEPOINT`, you can if needed roll back to the savepoint with `ROLLBACK TO`.


### Command Line


- [psql](https://www.postgresql.org/docs/13/app-psql.html)

- [createdb](https://www.postgresql.org/docs/13/app-createdb.html)
- [dropdb](https://www.postgresql.org/docs/13/app-dropdb.html)

- [pg_restore](https://www.postgresql.org/docs/7.3/app-pgrestore.html)


### Agregate Functions

It is important to understand the interaction between aggregates and SQL's WHERE and HAVING clauses. The fundamental difference between WHERE and HAVING is this: WHERE selects input rows before groups and aggregates are computed (thus, it controls which rows go into the aggregate computation), whereas HAVING selects group rows after groups and aggregates are computed. Thus, the WHERE clause must not con
tain aggregate functions; it makes no sense to try to use an aggregate to determine which rows will be inputs to the aggregates. On the other hand, the HAVING clause always contains aggregate functions. (Strictly speaking, you are allowed to write a HAVING clause that doesn't use aggregates, but it's seldom useful. The same condition could be used more efficiently at the WHERE stage.)

- max()
- min()
- sum()
- rank()


### Window Function

```

SELECT depname, empno, salary, avg(salary) OVER (PARTITION BY depname) FROM empsalary;

```

A window function call always contains an OVER clause directly following the window function's name and argument(s). This is what syntactically distinguishes it from a normal function or non-window aggregate. 

There is another important concept associated with window functions: for each row, there is a set of rows within its partition called its ***window frame.***

Some window functions act only on the rows of the window frame, rather than of the whole partition. 

Window functions are permitted only in the SELECT list and the ORDER BY clause of the query. They are forbidden elsewhere, such as in GROUP BY, HAVING and WHERE clauses. This is because they logically execute after the processing of those clauses. Also, window functions execute after non-window aggregate functions. This means it is valid to include an aggregate function call in the arguments of a window function, but not vice versa.

### Pattern Matching

- [Pattern Matching](https://www.postgresql.org/docs/13/functions-matching.html)

-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------

- [Psycopg – PostgreSQL DOCS](https://www.psycopg.org/docs/)
- [GITHUB](https://github.com/psycopg/psycopg2)
- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)

-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------

- transactional database
- Transactions
- Atomic
- atomic updates
- transaction block
- Savepoints 

-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----