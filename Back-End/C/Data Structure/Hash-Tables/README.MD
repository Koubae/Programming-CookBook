Hash Tables 
========

Also called **Dictionary (Python)** | **Associative Arrays**  | **Maps** | **Lookup Tables.**

They allow for the efficient lookup, insertion, and deletion of any object associated with a given key.

Typical implementation should give **O(1)** time complexity for lookup, insert, update, and delete operations in the average case.

- [Hash table --WIKI--](https://en.wikipedia.org/wiki/Hash_table)

- [Associative array --WIKI--](https://en.wikipedia.org/wiki/Associative_array)


Hashing is an improvement over [Direct Access Table](https://www.geeksforgeeks.org/direct-address-table/).


Documentation
-------------

Is create with a key Value Pair. The key in order to be **hashable** it should.

Resizing is expensive, normally the implementation is done with **over allocate**

- [Hash function --WIKI--](https://en.wikipedia.org/wiki/Hash_function)
- [Hash table --WIKI--](https://en.wikipedia.org/wiki/Hash_table)

---------------------------------------

### Collisions

Since a hash function gets us a small number for a big key, there is possibility that two keys result in same value. The situation where a newly inserted key maps to an already occupied slot in hash table is called collision and must be handled using some collision handling technique. 

---------------------------------------

#### 1. Chaining

The idea is to make each cell of hash table point to a linked list of records that have same hash function value. Chaining is simple, but requires additional memory outside the table.

#### 2. Open Addressing

In open addressing, all elements are stored in the hash table itself. Each table entry contains either a record or NIL. When searching for an element, we one by one examine table slots until the desired element is found or it is clear that the element is not in the table.

#### 3. Probing

- Probing (linear)

---------------------------------------


### Singly Linked List

- [Singly Linked List](https://www.geeksforgeeks.org/)




Linked List
-----------


-----------------------------------------------------------------------------------------------------

Guide & Areas of Study
-----------------------

- [Skip list WIKI](https://en.wikipedia.org/wiki/Skip_list)

- [B-tree](https://en.wikipedia.org/wiki/B-tree)

- [PYTHON DICTIONARY IMPLEMENTATION --GITHUB--](https://github.com/python/cpython/blob/master/Objects/dictobject.c)

- **hash tables or hash maps**

- [Hash table - Wiki](https://en.wikipedia.org/wiki/Hash_table)
- [Basics of Hash Tables ](https://www.hackerearth.com/practice/data-structures/hash-tables/basics-of-hash-tables/tutorial/)
- [Hash Tables](https://www.cs.auckland.ac.nz/software/AlgAnim/hash_tables.html)
- [6.5. Hashing](https://runestone.academy/runestone/books/published/pythonds/SortSearch/Hashing.html)
- [data structures in practice](https://www.data-structures-in-practice.com/hash-tables/)

- **Key-sharing Dictionaries** [PEP 412](https://www.python.org/dev/peps/pep-0412/)

- **Compact Dictionaries** [Python-Dev More compact dictionaries with faster iteration](mail.python.org/pipermail/python-dev/2012-December/123028.html) 


### Associative Arrays (aka maps, or dictionaries)

- Keys unique.

- Adding/removing elements
- modifying an associated value.
- looking up a value via its key.


### Hash Maps (aka hash table)


- **collision** & **hash collision**

- [How do HashTables deal with collisions?](https://stackoverflow.com/questions/4980757/how-do-hashtables-deal-with-collisions)
- [Handling Collisions]()

- **probing (linear)** **probe sequence**

- [Linear probing -Wiki](https://en.wikipedia.org/wiki/Linear_probing)
- [DOCS](http://web.stanford.edu/class/archive/cs/cs166/cs166.1166/lectures/12/Small12.pdf)
- [DOCS](http://www.cs.tau.ac.il/~zwick/Adv-Alg-2015/Linear-Probing.pdf)

- **over allocate**

### Dictionary

- **Split-table Dictionary**

-----------------------------------------------------------------------------------------------------

Terms & Keywords
----------------

**Dictionary (Python)** | **Associative Arrays**  | **Maps** | **Lookup Tables.**

- Probing

- Skip list

- Linked List

- B-tree


-----------------------------------------------------------------------------------------------------

References
----------



-----------------------------------------------------------------------------------------------------

Notes
-----