# Tuples & Data Structure
=======================


- [collections.namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
-----------------------------------------------------------------------------------------------------


Namedtuple is a function which generates a new class → **class factory**
We have to understand that namedtuple is a class factory
When we use it, we are essentially creating a new class, just as if we had used class ourselves.

```
Point2D = namedtuple('Point2D', ['x', 'y])
```

There are many ways we can provide the list of field names to the namedtuple function:

* List of string
* Tuple of strings
* Single string with the field names separated by whitespace or commas


- _make(iterable)

Class method that makes a new instance from an existing sequence or iterable.

- _asdict()

Return a new dict which maps field names to their corresponding values.

- _replace(**kwargs)

Return a new instance of the named tuple replacing specified fields with new values:

- _fields

Tuple of strings listing the field names. Useful for introspection and for creating new named tuple types from existing named tuples.

- _field_defaults

Dictionary mapping field names to default values.
### The rename keyword-only argument for namedtuple

Namedtuple has a keyword-only argument, **rename** (defaults to False),
that will automatically rename any invalid field name uses convention: 

```
_{position in list of field names}

Person._fields → ('name', 'age', '_2')

Point2D._source # See what the code for that class is, using the class property _source

Point2D = namedtuple('Point2D', 'x y')
pt1 = Point2D(10, 20)

# Creates a dictionary of all the named values in the tuple

pt1._asdict() → {'x': 10, 'y': 20}

```

### The _replace instance method


Named tuples have a very handy instance method, **_replace.**

- It will copy the named tuple into a new one, replacing any values from keyword arguments.
- The keyword arguments are simple the field names in the tuple and the new value.
- The keyword name must match an existing field name.

```
Stock = namedtuple('Stock', 'symbol year month day open high low close')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

djia = djia._replace(day=26, high=26_459, close=26_394)

djia → 'DJIA', 2018, 1, 26, 26_313, 26_459, 26_260, 26_394

```
*Note that the memory address of djia has now changed*


## Features

- [class typing.NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)
- [types.SimpleNamespace](https://docs.python.org/3/library/types.html#types.SimpleNamespace)

### Unpacking:

By convention, we use the underscore to indicate this is a variable we don't care about


```
record = ('DJIA', 2018, 1, 19, 25987.35, 26071.72, 25942.83, 26071.72)

symbol, year, month, day, *_, close = record

city, _, population = ('Beijing', 'China', 21_000_000)
```

### NOTES

- **__defaults__**:

A tuple containing default argument values for those arguments that have defaults, or None if no arguments have a default value. ---> **Writable**

- **Prototype**:

Prototype is a creational design pattern that allows cloning objects, even complex ones, without coupling to their specific classes.

-----------------------------------------------------------------------------------------------------


