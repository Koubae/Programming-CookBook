Python SQLite API 
=======================


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


-----------------------------------------------------------------------------------------------------