# 4 Descriptors
=======================

- [Descriptor HowTo Guide --Python DOCS-- ](https://docs.python.org/3/howto/descriptor.html)
- [Real Python](https://realpython.com/python-descriptors/)
- [Python Reference](https://python-reference.readthedocs.io/en/latest/docs/dunderdsc/)
- [Dabeaz](http://dabeaz.com/py3meta/) *Has hot a Metaprogramming PDF Too*

-----------------------------------------------------------------------------------------------------

## Descriptor Protocol

- **__get__**  used to get an attribute value

- **__set__**  used to set an attribute value

- **__delete__** used to delete an attribute
> __delete__(self, obj) -> None

- **__set_name__**

## Non-data Descriptors

**Functions **ARE** Non-data Descriptors**

- **__get__**

##  Data Descriptors

- **__get__**
- **__set__** and or **__delete__**

## Custom Data Descriptors

**Property objects are data descriptors.


## Strong Reference & Weak References and Weak Dictionaries

* weakref: 
 it as a reference to an object that does not affect the reference count as far as the memory manager is concerned

- [weakref — Weak references Python DOCS](https://docs.python.org/3/library/weakref.html)


### *__get__* 

```
__get__((self, instance, owner_class):)

```

> __get__(self, obj, type=None) -> value

### *__set__* 


```
__set__(self, instance, value):

```
> __set__(self, obj, value) -> None

- instance: The instance the __set__ method was called from.
- Value: The value we want to assign to the signature.

### *__set_name__*

* gets called (once) when the descriptor is first instantiated:
    * better error messages
    * include name of attribute that raised the exception
    * useful application in descriptors used for validation
    * **re-usability**

-----------------------------------------------------------------------------------------------------