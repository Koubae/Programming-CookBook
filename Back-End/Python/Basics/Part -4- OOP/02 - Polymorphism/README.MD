# 2Polymorphism and Special Methods 
=======================

- [DOCS]()


-----------------------------------------------------------------------------------------------------

##### New Class

* __new__

* __init__


##### Itedentity

* __class__

* __name__

* __dict__ -> Memory Overhead, Instance Dictionary


##### Str() & repr()

* __str__

* __repr__

If _str__ is not implemented, Python lookups for __repr__

##### Methods

* __self__ -> the instance the method is bound to

* __func__ -> he original function (defined in the class)

##### Context Manager **Protocol**

* __enter__

* __exit__

##### Sequence Types **Protocol**

* __getitem__

* __setitem__

* __delitem__

##### Iterables and Iterators **Protocol**

* __iter__

* __next__


###### Instance Methods

* __self__

* __init__


##### Hashing and Equality **Protocol**

An object ot be usable in a mapping type:

- > Key in a Dictionary.
- > Element of a Set.

**It mush be Hashable**

* __hash__  => Uses id() of object
* __eq__ => uses identify comparison (is)

If **only** __eq__ is implemented, __hash__ is implicity set to None unless __hash__ *is* implemented.


##### Boolean **Protocol**

* __bool__ -> Must return True or False

**If __bool__ is not defined** it will look for:

* __len__ -> 0 = False, any is True

**If __bool__ && __len__ are not implemented** object = True


##### Callable **Protocol**

* __call__ 

##### Class Finelizer **Protocol**  (or Destructor, but not accurate GC is.)

* __del__

- **-- Safe object finalization** [PEP 442](https://www.python.org/dev/peps/pep-0442/)

- [Finalizer --WIKI--](https://en.wikipedia.org/wiki/Finalizer)

**we do not control whenit will get called!**

A Class Finalizer The garbage collector destroys objects that are no longer referenced anywhere
The __del__method will get called *right beforethe* object is destroyed by the **GC**.
so the GCdetermines whenthis method is called.
User **context manager** to clean up

##### Format 

* __format__


##### Pre-Determined Attributes

* __slots__

##### Others

* __len__ -> Implements len()

* __contains__ -> Implements in()



#### Arithmetic Operations

* __add__ +     __radd__
* __sub__ -     __rsub__
* __mul__ *     __rmul__
* __truediv__ /     __rtruediv__
* __floordiv__ //     __rfloordiv__
* __mod__ %     __rmod__
* __pow__ **     __rpow__
* __matmul__ @ *numpy* support

##### In-Place operators

* __isub__ -=     
* __imul__ *=     
* __itruediv__ /=     
* __ifloordiv__ //=     
* __imod__ %=     
* __ipow__ **=     

##### Unary Operators, Functions
 
* ___neg__ -a
* __pos__ +a
* __abs__ abs(a)



##### Rich Comparison

**Python Automatically uses Reflactions

* __lt__ < if *NotImplemented* > __gt__
* __le__ <= if *NotImplemented* >= __ge__
* __eq__ == if *NotImplemented* > != __ne__
* __ne__ != if *NotImplemented* == __eq__
* __gt__ > if *NotImplemented* < __lt__
* __ge__ >= if *NotImplemented* <= __le__

For example, if == and < is defined, then:

- a <= b is a == b or a < b
- a > b is b < a
- a >= b is a == b or b < a
- a != b is not(a == b)
- On the other hand if we define == and <=, then:

- a < b is a <= b and not(a == b)
- a >= b is b <= a
- a > b is b <= a and not(b == a)
- a != b is not(a == b)


-----------------------------------------------------------------------------------------------------