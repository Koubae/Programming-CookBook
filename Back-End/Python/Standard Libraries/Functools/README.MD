# Functools Module
=======================

Higher-order functions and operations on callable objects

- [DOCS](https://docs.python.org/3/library/functools.html)
-----------------------------------------------------------------------------------------------------

## Functions 

* **functools.cache(user_func)**
- [Memoization --WIKI--](https://en.wikipedia.org/wiki/Memoization)

It calls internally * **functools.lru_cache(user_function)** with maxsize=None
 
- [The Python wiki](https://wiki.python.org/moin/PythonDecoratorLibrary#Cached_Properties)

* **functools.cached_property(func)**

- [cached-property --GITHUB--](https://github.com/pydanny/cached-property)

* **functools.cmp_to_key(func)**


------------------------------------------

* **functools.lru_cache(user_function)**

- [Least recently used (LRU) Wiki](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU))

* **functools.lru_cache(max_size=128, typed=False)**

------------------------------------------


* **functools.total_ordering** => Used as decorator with no args

* **functools.partial(func, /, *args, **kwargs)**
    * **functools.partial.func**
    * **functools.args**
    * **functools.keywords**

* **functools.partialmethod(func, /, *args, **kwargs)**

* **functools.reduce(func, iterable, [itintializer])**

* **functools.singledispatch** => Used as decorator with no args

* **functools.singledispatchmethod(func)** => Used as decorator with no args

* **functools.update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)**

* **functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)**



### 


-----------------------------------------------------------------------------------------------------