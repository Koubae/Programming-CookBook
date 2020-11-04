# Sets
=======================


A set is an unordered collection of disctinct objects
- **Revamping dict.keys(), .values() and .items()** [PEP 3106](https://www.python.org/dev/peps/pep-3106/)

Elements of a set:

- must be unique(distinct)
- must be hashable
- have no guaranteed order

Elements of a frozenset:

- must be unique(distinct)
- must be hashable
- have no guaranteed order


-----------------------------------------------------------------------------------------------------git 

## Functionality 

* cardinality -> len(s)
* membership testing -> in, not in
* unions -> s1 | s2, si.union(s2)
* intersections -> s1 & s2, s1.intersection(s2)
* differences -> s1 -s2, s1.difference(s2)
* symmetric difference -> s1 ^ s2, s1.symmetric_difference(s2)
* subsets -> s1 <= s2, s1.issubset(s2)
* supersets -> s1 >= s2, s1.issuperset(s2)
* disjointness -> s1.isdisjoint(s2)


#### Common operations

- len(s)
- s.add('python')
- s.remove(30) -> KeyError exception if item not in Set-
- s.discard('a') -> No KeyError exception
- s.pop()
- s.clear()

#### Analogous Set Mutating Updates

* |=  ==> s1 |= s2 or -> s1.update(s2)
* &= ==> s1 &= s2 or -> s1.intersection_update(s2) 
* -= ==> s1 -= s2 or -> s1.difference_update(s2) 
* ^= ==> s1 ^= s2 or -> s1.symmetric_difference_update(s2) 


### 

-----------------------------------------------------------------------------------------------------