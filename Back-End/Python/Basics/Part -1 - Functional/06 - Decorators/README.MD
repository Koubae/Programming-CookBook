Decorators
=======================


## Memoization

- [Memoization](https://en.wikipedia.org/wiki/Memoization#:~:text=In%20computing%2C%20memoization%20or%20memoisation,the%20same%20inputs%20occur%20again)
- **A powerful caching library for Python** [memoization](https://pypi.org/project/memoization/)


This concept of improving the efficiency of our code by caching pre-calculated values so they do not need to be re-calcualted every time, is called "memoization"

## Monkey patching

- [Monkey patch](https://en.wikipedia.org/wiki/Monkey_patch)

**A monkey patch** (also known as "duck punching")[1] is a way for a program to extend or modify supporting system software locally (affecting only the running instance of the program).

- [Stack Overflow](https://stackoverflow.com/questions/19545982/monkey-patching-a-class-in-another-module-in-python)

#### @functools.lru_cache

**LRU Cache = Least Recently Used caching**: 

- *Since the cache is not unlimited, at some point cached entries need to be discarded, and the least recently used entries are discarded first.*

- [DOCS](https://docs.python.org/3/library/functools.html#functools.lru_cache)

### @functools.total_ordering

The class must define one of __lt__(), __le__(), __gt__(), or __ge__(). In addition, the class should supply an __eq__() method.

- [DOCS](https://docs.python.org/3/library/functools.html#functools.total_ordering)

## Features

- [inspect module](https://docs.python.org/3/library/inspect.html)
- [html](https://docs.python.org/3/library/html.html)
- [Decorators](https://github.com/jaymon/decorators)


### Documentaion referance:

- [PythonDecorators](https://wiki.python.org/moin/PythonDecorators)
- [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)
- [python-cookbook](https://github.com/dabeaz/python-cookbook/blob/master/src/9/defining_a_decorator_that_takes_an_optional_argument/example.py)

### NOTES

- Single Dispatch & Multi dispatch.

[PEP 443](https://www.python.org/dev/peps/pep-0443/)
[Function Overloading with singledispatchhttps](https://www.blog.pythonlibrary.org/2016/02/23/python-3-function-overloading-with-singledispatch/)

- Overloading:

* [Function overloading](https://en.wikipedia.org/wiki/Function_overloading)
* [Computer Programming/Function overloadinghttps](https://en.wikibooks.org/wiki/Computer_Programming/Function_overloading)
* [Operator overloading](https://en.wikipedia.org/wiki/Operator_overloading)


- Singletons

[Singleton pattern](https://en.wikipedia.org/wiki/Singleton_pattern#:~:text=In%20software%20engineering%2C%20the%20singleton,mathematical%20concept%20of%20a%20singleton)

[Purpose of singletons in programming](https://stackoverflow.com/questions/2551112/purpose-of-singletons-in-programming)

A singleton is a class with only one instance. There are several singletons in Python that you use frequently, including None, True, and False.


-----------------------------------------------------------------------------------------------------