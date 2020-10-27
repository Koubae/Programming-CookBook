# Generators
=======================


- [Python Wiki](https://wiki.python.org/moin/Generators)
- **Simple Generators** [PEP 255](https://www.python.org/dev/peps/pep-0255/)
- [Python Tips](https://book.pythontips.com/en/latest/generators.html)

- **Iterators** [PEP 234](https://www.python.org/dev/peps/pep-0234/)
- **Coroutines via Enhanced Generators** [PEP 342](https://www.python.org/dev/peps/pep-0342/)

-----------------------------------------------------------------------------------------------------

## yield

- **yield from**
- **.send()**
- **.throw()**
- **.close()**

- Data Pipelines

## Generator Function

Function that contain the yield statement are *generator factories.*
*Generators* **are** *iterators*.


## Generator expressions

- List comprehension are **eager**
    - Faster iteration.
    - if element is really long, and need few elements, is *slower*.

- Generators are **lazy**
    - Slower Iteration.
    - if element is really long, and need few elements, is *faster*.

-----------------------------------------------------------------------------------------------------

### NOTES & ToRead

- [tracemalloc — Trace memory allocations](https://docs.python.org/3/library/tracemalloc.html)
[Python Generator Tricks](https://linuxgazette.net/100/pramode.html)
- [weightless threads](https://www.ibm.com/developerworks/library/l-pythrd/)
- [Generators Are Not Coroutines](http://wiki.c2.com/?GeneratorsAreNotCoroutines)


-----------------------------------------------------------------------------------------------------