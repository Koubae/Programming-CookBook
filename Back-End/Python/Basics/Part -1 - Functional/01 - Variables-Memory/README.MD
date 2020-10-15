# VAriables & Memory
=======================


- [PYTHON IMPLEMENTATIONS](https://wiki.python.org/moin/PythonImplementations)

• **Jython** – written in Java and can import and use any Java class – in fact it even
compiles to Java bytecode which can then run in a JVM
• **IronPython** – this one is written in C# and targets .Net (and mono) CLR
• **PyPy** – this one is written in RPython (which is itself a statically-typed subset of Python written in C that is specifically designed to write interpreters).

-----------------------------------------------------------------------------------------------------

## Features

- [ctypes](https://docs.python.org/3/library/ctypes.html)

ctypes is a foreign function library for Python. It provides C compatible data types, and allows calling functions in DLLs or shared libraries. It can be used to wrap these libraries in pure Python.

- [sys](https://docs.python.org/3/library/sys.html)

- [gc](https://docs.python.org/3/library/gc.html)

### Notes

**Changing the data inside the object is called modifying the internal state of the object.**


- *An object whose internal state can be changed, is called **Mutable**.*

- *An object whose internal state cannot be changed, is called **Immutable**.*

- *In Python, Strings (str) are **immutable** objects.*


- The term shared reference is the concept of two variables referencing
the same object in memory (i.e. having the same memory address)

- At startup, Python (CPython), pre-loads (caches) a global list of integers in the range [-5, 256].
Any time an integer Python will use the cached version of that object.



> When we write:
```
a = 10
```
Python just has to point to the existing reference for 10 

>But if we write:
```
a = 257
```

Python does not use that global list and a new object is created every time.

> **Interning: reusing objects on-demand**

> [Singletons](https://python-patterns.guide/gang-of-four/singleton/) **Optimization strategy – small integers show up oftenWhen we write**

- [The Singleton](https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html)


- my_func.__code__ [DOCS](https://docs.python.org/3/reference/datamodel.html)

The code object representing the compiled function body.

WRITABLE = True



-----------------------------------------------------------------------------------------------------


## The None Object

- [DOCS](https://docs.python.org/3/c-api/none.html)


The None object can be assigned to variables to indicate that they are not set (in the way we would expect them to be), i.e. an “empty” value (or null pointer).

But the None object is a real object that is managed by the Python memory manager. Furthermore, the memory manager will always use a shared reference when assigning
a variable to None

*So we can test if a variable is “not set” or “empty” by comparing it’s memory
address to the memory address of None using the is operator*


-----------------------------------------------------------------------------------------------------

## Interned

Identifiers are interned:

- must start with _ or a letter
- can only contain _ letters and numbers

```
a = ‘some_long_string’ 
b = ‘some_long_string’
```

Using a == b, we need to compare the two strings character by character
In which case we can use a is b instead – which compares two
integers (memory address)

*This is **much faster** than the character by character comparison*
```
import sys

a = sys.intern(‘the quick brown fox’)
b = sys.intern(‘the quick brown fox’)

```
By using sys.intern you ensure that you never create two string objects that have the same value—when you request the creation of a second string object with the same value as an existing string object, you receive a reference to the pre-existing string object. This way, you are saving memory. Also, string objects comparison is now very efficient because it is carried out by comparing the memory addresses of the two string objects instead of their content.

- [DOCS](https://docs.python.org/3/library/sys.html#sys.intern)
- [SOW](https://stackoverflow.com/questions/1136826/what-does-python-sys-intern-do-and-when-should-it-be-used)
- [SOW](https://stackoverflow.com/questions/327223/memory-efficient-alternatives-to-python-dictionaries)


- Constant expressions
```
24 * 60
```
Python will actually pre-calculate 24 * 60 → 1440

(1, 2) * 5 ===> (1, 2, 1, 2, 1, 2, 1, 2, 1, 2)
'abc' * 3 ===>  abcabcabc
'hello’ + ‘ world’ == > hello world
but not 'the quick brown fox' * 10 ==> more that 20 chars

### **Membership Tests: Mutables are replaced by Immutables**

**if e in [1, 2, 3]:**

are encountered, the [1, 2, 3] constant, is replaced by its immutable counterpart => (1, 2, 3) tuple

> lists ==> tuples
> sets ==> frozensets

**Set membership is much faster than list or tuple membership (sets are basically like dictionaries)**
So, instead of writing:
```
if e in [1, 2, 3]: if e in (1, 2, 3): 
```

Write:
```
if e in {1, 2, 3}:
```

-----------------------------------------------------------------------------------------------------