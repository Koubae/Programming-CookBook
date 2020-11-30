# Itertools
=======================


- [DOCS](https://docs.python.org/3/library/itertools.html)
-----------------------------------------------------------------------------------------------------

## Infinite iterators.


- **Count()**

Infinite count of a Iterator of Float, Given a starting number and steps. Very useful in conjunction with other functions like map, zip and operator module.

The count function is similar to range, except it does not have a stop value. It has both a start and a step

- **cycle**

Make an Iterator that loops repeatedly over and iterator, making a **copy of each element**.

- *repeat*

The repeat function is used to create an iterator that just returns the **same value** again and again. By default it is infinite, but a count can be specified.


## Iterators | Shortest input sequence.


- **accumulate(iterable, [func, *, initial=None])**

The accumulate funcion is very similar to the reduce function, returns a lazy iterator producing all the intermediate results.

**Important** The function passaed as argument should have 2 elements i.e. mul | min | max


- **chain(*iterables)**
- **chain.from_iterable(iterable)**

Analogous to sequence concatenation, generates a iterator that yields concatenated values from the iterables supplied in the arguments, as if it was a unique iterable.

chain.from_iterables, takes one iterable as argument, it iterates through each of its sub
iterable (usefule to use instead of multiple nested for loops).




## Filtering | Selecting

- **compress(data, selector)**

A way of filtering ine iterable using the truthiness ot items in another iterable.

The compress function is essentially a filter that takes two iterables as parameters. The first argument is the iterable (data) that will be filtered, and the second iterable contains elements (selectors), possibly of different length than the iterable being filtered. As always in Python, any object has an associated truth value, and the selectors therefore each have a truth value as well.

The resulting iterator yields elements from the data iterable where the selector at the same "position" is truthy.


- **dropwhile(predicate, iterable)**

Returns an iterator that will start iterating and yielding items once pred(item) is False => iterator exhausted.

- **takewhile(predicate, iterable)**

Returns an iterator that will yield items while pred(item) is Truthy => iterator exhausted.

### 


-----------------------------------------------------------------------------------------------------