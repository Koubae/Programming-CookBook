# Flask-Admin - SQLA 
=============================

#### Taken from [Flask-Admin Docs](#https://github.com/flask-admin/flask-admin/tree/master/examples/sqla)


SQLAlchemy model backend integration examples.

### Modules used

- arrow==0.16.0
- Babel==2.8.0
- click==7.1.2
- colour==0.1.5
- Flask==1.1.2
- Flask-Admin==1.5.6
- Flask-BabelEx==0.9.4
- Flask-SQLAlchemy==2.4.4
- SQLAlchemy==1.3.19
- SQLAlchemy-Utils==0.36.8
- tablib==2.0.0

----------------------------------

### Arrow [DOC](#https://arrow.readthedocs.io/en/stable/)

> Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps. It implements and updates the datetime type, plugging gaps in functionality and providing an intelligent module API that supports many common creation scenarios. Simply put, it helps you work with dates and times with fewer imports and a lot less code.


----------------------------------

### SQLAlchemy-Utils [DOC](#https://sqlalchemy-utils.readthedocs.io/en/latest/installation.html)

> Various utility functions and custom data types for SQLAlchemy.

----------------------------------

### Flask-BabelEx [DOC](#https://pythonhosted.org/Flask-BabelEx/)

> Flask-BabelEx is an extension to Flask that adds i18n and l10n support to any Flask application with the help of babel, pytz and speaklater. It has builtin support for date formatting with timezone support as well as a very simple and friendly interface to gettext translations.

----------------------------------

### Tablib [DOC](#https://tablib.readthedocs.io/en/stable/#:~:text=Tablib%20is%20an%20MIT%20Licensed,and%20seamless%20format%20import%20%26%20export.)

> Tablib is an MIT Licensed format-agnostic tabular dataset library, written in Python. It allows you to import, export, and manipulate tabular data sets. Advanced features include segregation, dynamic columns, tags & filtering, and seamless format import & export.

----------------------------------

### Color [DOC](#https://pypi.org/project/colour/)

> Converts and manipulates common color representation (RGB, HSL, web, …)

----------------------------------


## Documentations.

# Python -Lybrary

> ### enum.Enum [DOCS](#https://docs.python.org/3/library/enum.html#enum.Enum)

Base class for creating enumerated constants. See section Functional API for an alternate construction syntax.

> ### Functional API [DOCS](#https://docs.python.org/3/library/enum.html#functional-api)

The Enum class is callable, providing the following functional API:

```

>>> Animal
<enum 'Animal'>
>>> Animal.ANT
<Animal.ANT: 1>
>>> Animal.ANT.value
1
>>> list(Animal)
[<Animal.ANT: 1>, <Animal.BEE: 2>, <Animal.CAT: 3>, <Animal.DOG: 4>]

```


----------------------------------

# Sqlachemy-utils.

>### UUIDType [DOCS](#https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html#module-sqlalchemy_utils.types.uuid) [DOCS2](#https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/uuid.html)

- classsqlalchemy_utils.types.uuid.UUIDType(binary=True, native=True, **kwargs)

Stores a UUID in the database natively when it can and falls back to a BINARY(16) or a CHAR(32) when it can’t.

```

from sqlalchemy_utils import UUIDType
import uuid

class User(Base):
    __tablename__ = 'user'

    # Pass `binary=False` to fallback to CHAR instead of BINARY
    id = sa.Column(UUIDType(binary=False), primary_key=True)

```


----------------------------------

> ### ChoiceType [DOCS](#https://sqlalchemy-utils.readthedocs.io/en/latest/data_types.html?highlight=ChoiceType#module-sqlalchemy_utils.types.choice) [DOCS_2](#https://sqlalchemy-utils.readthedocs.io/en/latest/_modules/sqlalchemy_utils/types/choice.html#ChoiceType)

ChoiceType offers way of having fixed set of choices for given column. It could work with a list of tuple (a collection of key-value pairs), or integrate with enum in the standard library of Python 3.4+ (the enum34 backported package on PyPI is compatible too for < 3.4).

Columns with ChoiceTypes are automatically coerced to Choice objects while a list of tuple been passed to the constructor. If a subclass of enum.Enum is passed, columns will be coerced to enum.Enum objects instead.

----------------------------------