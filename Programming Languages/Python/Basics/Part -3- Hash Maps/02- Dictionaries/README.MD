# Dictionaries
=======================


- **Revamping dict.keys(), .values() and .items()** [PEP 3106](https://www.python.org/dev/peps/pep-3106/)

-----------------------------------------------------------------------------------------------------

## Features

- **Key** Any **hashable object** -> constant
- sys.hash_info.width
- sys.hash_info.modulus
- p.__hash__() & sys.hash_info.modulus -> Truncates the number of bits

Just out of interest:

When we call the hash() function, although it in turn calls the __hash__ method, it does something more.

It will truncate the integer returned by __hash__ to a certain width which is implementation dependent.


### Keys, Values, Items Views


- d.keys() -> Iterable => List ::set()
- d.values() -> Iterable => List
- d.items() -> Iterable => List of Tuples [('k1', 1), ('k2', 2), ('k3', 3)]

Views are **Dynamic** reflecting any changes in the dictionary.
Views are not updatable.

- Keys => set() = union,intersection, difference.

-----------------------------------------------------------------------------------------------------