# Iteration Tools
=======================



-----------------------------------------------------------------------------------------------------

## itertools 

- [DOCS](https://docs.python.org/3.8/library/itertools.html#module-itertools)

#### itertools.islice => LAZY ITERATOR


*This function can be very useful when dealing with infinite iterators*

islice is an iterator - which means it becomes exhausted, even if you pass an iterable such as a list to it!



---------------------------

#### itertools.filterfalse

- Retains elements where the predicate evaluates to False (opposite than filter)


---------------------------


#### itertools.compress

- A way of **filtering** ine iterable using the truthiness ot items in another iterable.


=> Returns a lazy iterators

The compress function is essentially a filter that takes two iterables as parameters. The first argument is the iterable (data) that will be filtered, and the second iterable contains elements (selectors), possibly of different length than the iterable being filtered. As always in Python, any object has an associated truth value, and the selectors therefore each have a truth value as well.

The resulting iterator yields elements from the data iterable where the selector at the same "position" is truthy.

---------------------------

#### itertools.takewhile

- Returns an iterator that will yield items while pred(item) is Truthy => iterator exhausted.

---------------------------

#### itertools.dropwhile

- Returns an iterator that will start iterating and yielding items once pred(item) is False => iterator exhausted.

---------------------------

-----------------------------------------------------------------------------------------------------


### INFINITE ITERATORS FUNCTIONS

#### itertools.count 

- The count function is an infinite iterator.

The count function is similar to range, except it does not have a stop value. It has both a start and a step

---------------------------

#### itertools.cycle 

- Loops over a **finite** iterable indefinitely.

cycle is used to repeatedly loop over an iterable.

---------------------------

### itertools.repeat

The repeat function is used to create an iterator that just returns the same value again and again. By default it is infinite, but a count can be specified optionally:


-----------------------------------------------------------------------------------------------------

### itertools.chain -> lazy iteratos


*Analogous* to sequence concatenation.

 -> Dealing with **iterables** (including iterators)
 -> Chaining is itself a **lazy iterators**

##### itertoorl.chain.from_iterable(t)

Note that chain expects a variable number of positional arguments, each of which should be an iterable.

-----------------------------------------------------------------------------------------------------

### itertools.tee -> tuple ot iterators

(iter1, iter2, iter3)

-----------------------------------------------------------------------------------------------------

### itertools.starmap 

-----------------------------------------------------------------------------------------------------

### itertools.accumulate -> lazy iterator

The accumulate funcion is very similar to the reduce function,
returns a lazy iterator producing all the intermediate results.

-----------------------------------------------------------------------------------------------------

### itertools.ziploongest  

-----------------------------------------------------------------------------------------------------

### itertools.groupby

Be careful here with the groupby() - if you want to save all the data into a list you cannot first convert the groups into a list - you must step through the groups iterator, and retrieve each individual iterators elements into a list, the way we did it in the first example, or simply using a comprehension.

-----------------------------------------------------------------------------------------------------

### itertools.product -> lazy iterator


-----------------------------------------------------------------------------------------------------

### itertools.permutarions

-----------------------------------------------------------------------------------------------------

### itertools.combinations
### itertools.combinations_with_replacement

-----------------------------------------------------------------------------------------------------
## Aggregator

- Functions that iterate through an iterable and return a single value that
(usually) takes into account every element of the iterable.



```
min(iterable)
max(iterable)
sum(iterable)
```


-----------------------------------------------------------------------------------------------------

### NOTES

- **Predicate** -> Function that takes a single argument and => True or False

- **Filter** => returns a **lazy iterator**

- **Mapping** => Applying a callable to each element of an iterable

- **Accumulation** => Reducing an iterable down to a single value.

- ### COMBINATORICS [WIKI](https://en.wikipedia.org/wiki/Combinatorics)

- **permutations** [WIKI](https://en.wikipedia.org/wiki/Permutation)

- **combinations** [WIKI](https://en.wikipedia.org/wiki/Combination)

- **Cartesian product** [WIKI](Cartesian product)

- [Cross Join in SQL](https://www.w3resource.com/sql/joins/cross-join.php)



-----------------------------------------------------------------------------------------------------