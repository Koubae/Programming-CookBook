# Databases 
=======================



-----------------------------------------------------------------------------------------------------

Documentation
-------------


### FAQ ALTER TABLE Workaround for SQLite:

Unlike other database systems e.g., MySQL and PostgreSQL, you cannot use the ALTER TABLE statement to add a primary key to an existing table.

1. Set the foreign key constarint check off.

2. Rename the table to another table name (old_table).

3. Create a new table (table) with exact structure of the table that you have been renamed.

4. Copy data from the old_table to the table.

5. Turn on the foreign key constraint check on

Unlike SQL-standard and other database systems, SQLite supports a very limited functionality of the ALTER TABLE statement.

By using an SQLite ALTER TABLE statement, you can perform two actions:

1. Rename a table.
2. Add a new column to a table.
3. Rename a column (added supported in version 3.20.0)


Relationships & Joins
---------------------

### One-to Many Relationship

- [Entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)

### Many-to-Many Relationships


SQLAlchemy
-----------

- **SQLAlchemy** [DOCS](https://www.sqlalchemy.org/)

- [Object–relational mapping](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping)
- [Object–relational impedance mismatch](https://en.wikipedia.org/wiki/Object%E2%80%93relational_impedance_mismatch)

- [Unit of Work](https://www.martinfowler.com/eaaCatalog/unitOfWork.html)


Topics
-------

- [Relational database](https://en.wikipedia.org/wiki/Relational_database#Relations_or_tables)

- [Entity–relationship model](https://en.wikipedia.org/wiki/Entity%E2%80%93relationship_model)

- [Set Theory](https://www.sqlshack.com/mathematics-sql-server-fast-introduction-set-theory/)

- [Sneakernet](https://en.wikipedia.org/wiki/Sneakernet)


### Learning Links & Other

- [qliteonline](https://sqliteonline.com/)

- [SQL Tutorial - w3resource](https://www.w3resource.com/sql/tutorials.php)

- [chinook SQLite sample database -sqlitetutorial.net-](https://www.sqlitetutorial.net/sqlite-sample-database/)

- [tutlane.com](https://www.tutlane.com/tutorial/sqlite)


-----------------------------------------------------------------------------------------------------