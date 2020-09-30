# FlaskR - Flask Official Tutorial
=========================

**Flask project demostrating basic Flask concepts**

> **[DOCS](https://flask.palletsprojects.com/en/1.1.x/tutorial/)**
> **[GitHub Repo](https://github.com/pallets/flask/tree/master/examples/tutorial)**


Requirements:

- Flask
- Sqlite3
- Good intentions

--------------------------------------------------------------------------------------------

## Features



#### sqlite3.connect [DOCS](https://docs.python.org/2/library/sqlite3.html#sqlite3.connect)
=====================

```

sqlite3.connect(database[, timeout, detect_types, isolation_level, check_same_thread, factory, cached_statements])

```

- [sqlite3.PARSE_DECLTYPES](https://docs.python.org/2/library/sqlite3.html#sqlite3.PARSE_DECLTYPES)

This constant is meant to be used with the detect_types parameter of the connect() function.

Setting it makes the sqlite3 module parse the declared type for each column it returns. It will parse out the first word of the declared type, i. e. for “integer primary key”, it will parse out “integer”, or for “number(10)” it will parse out “number”. Then for that column, it will look into the converters dictionary and use the converter function registered for that type there.

--------------------------------------------------------------------------------------------

#### Executescript [DOCS](https://docs.python.org/2/library/sqlite3.html#sqlite3.Connection.executescript)
===================


This is a nonstandard shortcut that creates an intermediate cursor object by calling the cursor method, then calls the cursor’s executescript method with the parameters given.


--------------------------------------------------------------------------------------------

#### Click.command [DOCS](https://click.palletsprojects.com/en/7.x/api/?highlight=click%20command#click.command)
===================


Creates a new Command and uses the decorated function as callback. This will also automatically attach all decorated option()s and argument()s as parameters to the command.

The name of the command defaults to the name of the function with underscores replaced by dashes. If you want to change that, you can pass the intended name as the first argument.

All keyword arguments are forwarded to the underlying command class.

Once decorated the function turns into a Command instance that can be invoked as a command line utility or be attached to a command Group.

- [add_command](https://click.palletsprojects.com/en/7.x/api/?highlight=click%20command#click.Group.add_command)

Registers another Command with this group. If the name is not provided, the name of the command is used.


--------------------------------------------------------------------------------------------

#### flask.cli.with_appcontext( [DOCS](https://flask.palletsprojects.com/en/1.1.x/api/#flask.cli.with_appcontext)
===================

Wraps a callback so that it’s guaranteed to be executed with the script’s application context. If callbacks are registered directly to the app.cli object then they are wrapped with this function by default unless it’s disabled.

--------------------------------------------------------------------------------------------

##### NOTE TODO

Following up, the Text coverage from the Flask Tutorial ---> [DOCS](https://flask.palletsprojects.com/en/1.1.x/tutorial/tests/)

> ***[SOURCE CODE](https://github.com/pallets/flask/tree/master/examples/tutorial/tests)*

--------------------------------------------------------------------------------------------