Python SQLite API 
=======================


- **Python Database API Specification v2.0**[PEP 249](https://www.python.org/dev/peps/pep-0249/)

My Repo References
------------------

- [query_data.py Fodd-Tracker](https://github.com/Koubae/Programming-CookBook/blob/master/Back-End/Python/External%20Libraries/Flask/Flask_website_examples/02%20Food-Tracker/query_data.py)

- [app_query.py  Full queries Strings](https://github.com/Koubae/Programming-CookBook/blob/master/Back-End/Python/External%20Libraries/Flask/Flask_website_examples/05%20Question%20-%20Answer%20App/app_query.py)

- [Upload File Pic with SQLAlchemy](https://github.com/Koubae/Programming-CookBook/blob/master/Back-End/Python/External%20Libraries/Flask/Flask_website_examples/03%20Uploads/B%20Version/app.py)

- [Flask Flaskr DB](https://github.com/Koubae/Programming-CookBook/blob/master/Back-End/Python/External%20Libraries/Flask/Flask_website_examples/04%20Flaskr/flaskr/db.py)

Documentation
---------


* The default value for the timeout parameter is 5.0 (five seconds)

```
sqlite3.connect('SQLite_Python.db', timeout=20)
```

###  connection.total_changes

The connection.total_changes method returns the total number of database rows that have been affected.

### connection.backup() 

Python sqlite3 module provides a function to take a backup of the SQLite database. Using a connection.backup() method you can take the backup of SQLite database.

```
connection.backup(target, *, pages=0, progress=None, name="main", sleep=0.250)
```

## SQLite Database Exceptions


### sqlite3.Warning

A subclass of Exception. And you can ignore it if you want it doesn’t stop the execution.

### sqlite3.Error

The base class of the other exceptions in the sqlite3 module. It is a subclass of Exception.

### sqlite3.DatabaseError

Exception raised for errors that are related to the database.

Examples: If you try and open a file as a sqlite3 database that is NOT a database file, you will get sqlite3.DatabaseError: file is encrypted or is not a database

### sqlite3.IntegrityError

Subclass of a DatabaseError.  You will get this Exception when the relational integrity of the database is affected, e.g., a foreign key check fails.

### sqlite3.ProgrammingError

It is also a subclass of DatabaseError. This exception raised because of programming errors, e.g., creating a table with the same which already exists, syntax error in the SQL queries.

### sqlite3.OperationalError

It is also a subclass of DatabaseError. This error is not in our control. This exception raised for errors that are related to the database’s operation.

Examples: an accidental disconnect, server down, a timeout occurs, the data source issues. server down

### sqlite3.NotSupportedError

You will get an exception raised when database API was used which is not supported by the database.

Example: calling the rollback() method on a connection that does not support the transaction. Calling commit after creating table command.


-----------------------------------------------------------------------------------------------------