# VAriables & Memory
=======================


- [PYTHON IMPLEMENTATIONS](https://wiki.python.org/moin/PythonImplementations)

• **Jython** – written in Java and can import and use any Java class – in fact it even
compiles to Java bytecode which can then run in a JVM.

• **IronPython** – this one is written in C# and targets .Net (and mono) CLR.

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
- [SOO What does sys.intern() do and when should it be used?](https://stackoverflow.com/questions/1136826/what-does-python-sys-intern-do-and-when-should-it-be-used)
- [SOO Memory Efficient Alternatives to Python Dictionaries](https://stackoverflow.com/questions/327223/memory-efficient-alternatives-to-python-dictionaries)


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

Datamodel
----------


- [Python Data Model DOCS](https://docs.python.org/3/reference/datamodel.html)

**Code objects**

Code objects represent byte-compiled executable Python code, or bytecode. 

The difference between a code object and a function object is that the function object contains an explicit reference to the function’s globals (the module in which it was defined), 
while a code object contains no context; also the default argument values are stored in the function object, not in the code object (because they represent values calculated at run-time). 

Unlike function objects, code objects are immutable and contain no references (directly or indirectly) to mutable objects.


#### Special read-only attributes: 

* **co_name**: gives the function name; co_argcount is the total number of positional arguments (including positional-only arguments and arguments with default values); 

* **co_posonlyargcount**: is the number of positional-only arguments (including arguments with default values); 

* **co_kwonlyargcount**: is the number of keyword-only arguments (including arguments with default values); 

* **co_nlocals**: is the number of local variables used by the function (including arguments); 

* **co_varnames**: is a tuple containing the names of the local variables (starting with the argument names); 

* **co_cellvars**: is a tuple containing the names of local variables that are referenced by nested functions; 

* **co_freevars**: is a tuple containing the names of free variables; co_code is a string representing the sequence of bytecode instructions; 

* **co_consts**: is a tuple containing the literals used by the bytecode; 

* **co_names**: is a tuple containing the names used by the bytecode; 

* **co_filename**: is the filename from which the code was compiled; 

* **co_firstlineno**: is the first line number of the function; 

* **co_lnotab**: is a string encoding the mapping from bytecode offsets to line numbers (for details see the source code of the interpreter); 

* **co_stacksize**: is the required stack size; co_flags is an integer encoding a number of flags for the interpreter.

The following flag bits are defined for co_flags: bit 0x04 is set if the function uses the *arguments syntax to accept an arbitrary number of positional arguments; 
bit 0x08 is set if the function uses the **keywords syntax to accept arbitrary keyword arguments; bit 0x20 is set if the function is a generator.

Future feature declarations (`from __future__ import division`) also use bits in co_flags to indicate whether a code object was 
compiled with a particular feature enabled: bit 0x2000 is set if the function was compiled with future division enabled; bits 0x10 and 0x1000 were used in earlier versions of Python.

Other bits in co_flags are reserved for internal use.

If a code object represents a function, the first item in co_consts is the documentation string of the function, or None if undefined.