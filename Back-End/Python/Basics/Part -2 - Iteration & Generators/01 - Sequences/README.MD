# Sequences
=======================


- []()
----------------------------------------------------------------------------------------------

## Features

### Some methods supported by mutable sequence types such as lists


- l.clear()  *Removes all itesm from l*
- l.append(x) *appends x to the end of s*
- l.insert(i, x) *insert x at index i*
- l.extend(literable) *appends contents of iterable to end of l*
- l.pop(i) *removes **and** returns element of index i*
- l.remove(x) *removes firdst occurence of x in s*
- l.reverse() *does an in-place reversal of elements of s*
- l.copy() *returns a shallow copy*

----------------------------------------------------------------------------------------------

## Sequence Type

**Sequence Type are Iterables**

#### They Should Implement:


- **__len__**
- **__getitem__** => Takes one single Int, + choose to handle slice

*Should return an elemenot for a valid index [0, length-1]*
*Negative indices i < 0 -> i = length > i*
**sclicing**

```
list_[0]
list_.__getitem__(0)
list_[100] => Ok
list_.__getitem__(100) => Error #out of index

```

* concatenation (+)
    - **__add__**
    - **__radd__**

* in-place concatenation (+=)
    - **__iadd__**

* repetition (*)
    - **__mul__**
    - **__rmul__**

* in-place repetition (*=)
    - **__imul__**

* index assignment (seq[i]=val)
    - **__getitem__**

* slice assignment (seq[i:j]=iter and seq[i:j:k]=iter)
    - **__getitem__**

* append, extend, in, del, pop
    - **__contains__** => in
    - **__delitem__** => del

----------------------------------------------------------------------------------------------

## Sequence Type

Transformations [i:j:k], k < 0

[i:j:k] = {x = i + n * k | 0 <= n < (j-i)/k}

----------------------------------------------------------------------------------------------

## Sorted

* Makes a copy of the iterable.
* Returns the sorted elements in a list.
* Uses a sort Alogrithm called [TimSort](https://en.wikipedia.org/wiki/Timsort)
* Stable Sort

## Sort()

* Same TimSort Alogithm.
* Same Keyword-only arg:key.
* Same Keyword-only arg:reverse(default is False).


----------------------------------------------------------------------------------------------


### NOTES

Homogeneous vs Heterogeneous Sequences

- *Strings are **homogeneous** sequences, each element is of the same type (a character).*

- *Lists are **heterogeneous** sequences, each element may be a different type.*

- Introduction to Algorithms, 3rd Edition (Book)


- slice => [itertools.islice()](https://docs.python.org/3.8/library/itertools.html#itertools.islice)


- [Dynamic array](https://en.wikipedia.org/wiki/Dynamic_array)

- [Constant folding](https://en.wikipedia.org/wiki/Constant_folding)

Constant folding and constant propagation are related compiler optimizations used by many modern compilers.[1] An advanced form of constant propagation known as sparse conditional constant propagation can more accurately propagate constants and simultaneously remove dead code.

- [Constant Folding](https://cran.r-project.org/web/packages/rco/vignettes/opt-constant-folding.html)

Constant folding is an optimization technique that eliminates expressions that calculate a value that can already be determined before code execution. These are typically calculations that only reference constant values or expressions that reference variables whose values are constant.

----------------------------------------------------------------------------------------------