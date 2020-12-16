Heap queue algorithm 
=======================


- **heapq — Heap queue algorithm** [--Python Docs--](https://docs.python.org/3/library/heapq.html)

Documentation
---------

A heap implements a priority queue as a complete binary tree. In a binary tree, each node will have at most two children. In a complete binary tree, all levels except possibly the deepest one are full at all times. If the deepest level is incomplete, then it will have the nodes as far to the left as possible. 

In a heap tree, **the value in a node is always smaller than both of its children**. This is called the heap property. This is different from a binary search tree, in which only the left node will be smaller than the value of its parent. 


There are three rules that determine the relationship between the element at the index k and its surrounding elements:

1. Its first child is at 2*k + 1.
2. Its second child is at 2*k + 2.
3. Its parent is at (k - 1) // 2.

The heap property means that if h is a heap, then the following will never be False:

-  heapify()

```
h[k] <= h[2*k + 1] and h[k] <= h[2*k + 2] == True

```

 heapify() modifies the list in place but doesn’t sort it. A heap doesn’t have to be sorted to satisfy the heap property. 

 However, since every sorted list **does satisfy** the heap property, running heapify() on a sorted list won’t change the order of elements in the list.

It’s useful to note that an empty list or a list of length one will always be a heap.


1. heapreplace() is equivalent to heappop() followed by heappush().
2. heappushpop() is equivalent to heappush() followed by heappop().

Terms 
-----

* [Logarithm](https://en.wikipedia.org/wiki/Logarithm)



-----------------------------------------------------------------------------------------------------