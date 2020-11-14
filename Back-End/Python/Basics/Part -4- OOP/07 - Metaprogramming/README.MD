# 7 Metaprogramming
=======================

- [DOCS]()


-----------------------------------------------------------------------------------------------------

## Features

### Metaclasses

Metaclass are a class(type) factory.
Don't always play nicely with multiple inheritance


#### Decorator

Use code to modify the behavior of another piece of code

#### Descriptors

use code to essentially modify the behavior of the dot (.) operator

-----------------------------------------------------------------------------------------------------

### NOTES


* __new__ --> Static Method.

* _prepare__ --> method of the metaclass. -> Static Method => Mapping Type

** Python calls __prepare__ before __new__**
** __prepare_ MUST return an object that is an instance of dict**

* __qualname__

* __doc__

* __getattribute__ --> First call 

if raise a AttributeError then call:

* __getattr__  ---> Re-raise AttributeError

* [types.MethodType](https://docs.python.org/3/library/types.html#types.MethodType)
- [Advantages of Using MethodType in Python
 SSO](https://stackoverflow.com/questions/37455426/advantages-of-using-methodtype-in-python)
-----------------------------------------------------------------------------------------------------