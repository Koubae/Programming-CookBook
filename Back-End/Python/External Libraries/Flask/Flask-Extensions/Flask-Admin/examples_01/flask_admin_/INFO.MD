> __new__


When subclassing immutable built-in types like numbers and strings, and occasionally in other situations, the static method __new__ comes in handy. __new__ is the first step in instance construction, invoked before __init__. The __new__ method is called with the class as its first argument; its responsibility is to return a new instance of that class. Compare this to __init__: __init__ is called with an instance as its first argument, and it doesn't return anything; its responsibility is to initialize the instance. There are situations where a new instance is created without calling __init__ (for example when the instance is loaded from a pickle). There is no way to create a new instance without calling __new__ (although in some cases you can get away with calling a base class's __new__).

Recall that you create class instances by calling the class. When the class is a new-style class, the following happens when it is called. First, the class's __new__ method is called, passing the class itself as first argument, followed by any (positional as well as keyword) arguments received by the original call. This returns a new instance. Then that instance's __init__ method is called to further initialize it. (This is all controlled by the __call__ method of the metaclass, by the way.)

Here is an example of a subclass that overrides __new__ - this is how you would normally use it.


```

    class inch(float):
    ...     "Convert from inch to meter"
    ...     def __new__(cls, arg=0.0):
    ...         return float.__new__(cls, arg*0.0254)
    ...
    >>> print inch(12)
    0.3048
    >>> 


```
-----------------------------


> __class__

```

class abstract1 (object):
  def __init__(self):
    if self.__class__ == abstract1: 
      raise NotImplementedError("Interfaces can't be instantiated")

```

self.__class__ is a reference to the type of the current instance.


** Note that the pythonic way to test for the type of an instance is to use the type() function instead, together with an identity test with the is operator:**

```

class abstract1(object):
    def __init__(self):
        if type(self) is abstract1: 
            raise NotImplementedError("Interfaces can't be instantiated")

```



```



class ClassA(object):
    def display(self):
        print("ClassA")

class ClassB(object):
    __class__ = ClassA

    def display(self):
        print("ClassB")

instance = ClassB()

print(type(instance))
print(instance.__class__)
instance.display()

```

The reason is that ClassB is overriding the __class__ descriptor, however the internal type field in the object is not changed. type(instance) reads directly from that type field, so it returns the correct value, whereas instance.__class__ refers to the new descriptor replacing the original descriptor provided by Python, which reads the internal type field. Instead of reading that internal type field, it returns a hardcoded value.

------------------------------------


- __delattr__
- __dict__   
- __dir__
- __doc__

------------------------------------

- __eq__

Defines behavior for the equality operator, ==.

------------------------------------

- __format__
- __ge__
- __getattribute__
------------------------------------

- __gt__

Defines behavior for the greater-than operator, >.

------------------------------------
- __hash__
------------------------------------

- __init__

The initializer for the class. It gets passed whatever the primary constructor was called with (so, for example, if we called x = SomeClass(10, 'foo'), __init__ would get passed 10 and 'foo' as arguments. __init__ is almost universally used in Python class definitions.

------------------------------------
- __init_subclass__
------------------------------------

- __le__

Defines behavior for the less-than-or-equal-to operator, <=.

------------------------------------

- __lt__

Defines behavior for the less-than operator, <.

------------------------------------
- __module__
- __ne__
------------------------------------
- __new__

__new__ is the first method to get called in an object's instantiation. It takes the class, then any other arguments that it will pass along to __init__. __new__ is used fairly rarely, but it does have its purposes, particularly when subclassing an immutable type like a tuple or a string. I don't want to go in to too much detail on __new__ because it's not too useful, but it is covered in great detail in the [Python docs](#https://www.python.org/download/releases/2.2/descrintro/#__new__).

------------------------------------
- __reduce__
- __reduce_ex__
- __repr__
- __setattr__
- __sizeof__
- __str__
- __subclasshook__
- __weakref__