# Iterables & Iterators
=======================


An ***iterable*** object is an object that implements *__iter__*, which is expected to **return** an ***iterator*** object.

An ***iterator*** is an object that implements *__next__*, which is expected to return the next element of the iterable object that returned it, and raise a ***StopIteration*** exception when no more elements are available.

In the simplest case the iterable will implement next itself and return self in *__iter__*.

You can use iterables in for loops, and you can use them to construct lists. 

Python will test first if an object is an **Iterable** and implements the **ITERATOR PROTOCOL** calling a **iterator.** 

- **Iterators** [PEP 234](https://www.python.org/dev/peps/pep-0234/)

- [python-patterns](https://github.com/faif/python-patterns)


----------------------------------------------------------------------------------------------------

## Features


- **range(10)** => *iterable* 
- **zip(l1, l2)** => *iterator*
- **enumerate(l1)** => *iterator*
- **open('cars.csv')** => *iterator*
- **dict.keys()** => *iterable*
- **dict.values()** => *iterable*
- **dict.items()** => *iterable*



- [itertools.cycle](https://docs.python.org/3.8/library/itertools.html#itertools.cycle)

Make an iterator returning elements from the iterable and saving a copy of each. When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely.

### Iterables:

An **iterator** is an object that implements:

- **__iter__** => Returns a **ITERATOR**

-----------------------------------------------------------------------------------------------------

### Iterators:

The iterator gets exhausted after we have finished iterating it fully - which means we have to create a new iterator every time we want to use a new iteration over the collection.

- **__next__** method that returns the next element in the container
- **__iter__** method that just returns the object itself (the iterator object)


*Dictionary iterators will iterate over the keys of the dictionary.*

### Lazy Evaluation

The benefits of lazy evaluation include:

* The ability to define control flow (structures) as abstractions instead of primitives.

* The ability to define potentially infinite data structures. This allows for more straightforward implementation of some algorithms.

* Performance increases by avoiding needless calculations, and avoiding error conditions when evaluating compound expressions.

The opposite of lazy evaluation is eager evaluation, sometimes known as strict evaluation.

- [Wiki](https://en.wikipedia.org/wiki/Lazy_evaluation)

Some benefits of using it are that reduces the time complexity of an algorithm by discarding the temporary computations and conditionals, allows the language runtime to discard sub-expressions that are not directly linked to the final result of the expression,
allows the programmer to access components of data structures out-of-order after initialization, as long as they are free from any circuits.

The logical expression operators like and,or, and if-then-else are all lazy,
because they don`t need to evaluate all arguments to determine the resulting value.

### NOTES

- [Python Wiki](https://wiki.python.org/moin/Iterator)

Check:  *Jon Bentley's ***Writing Efficient Programs****


-----------------------------------------------------------------------------------------------------