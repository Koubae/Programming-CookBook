def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n

    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n - 1)

fact.short_description = 'factorial function'
print(fact.short_description)
# >>> factorial function
print(dir(fact))
#['__annotations__', '__call__', '__class__',
# '__closure__', '__code__', '__defaults__',
# '__delattr__', '__dict__', '__dir__',
# '__doc__', '__eq__', '__format__',
# '__ge__', '__get__', '__getattribute__',
# '__globals__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__kwdefaults__',
# '__le__', '__lt__', '__module__',
# '__name__', '__ne__', '__new__',
# '__qualname__', '__reduce__', '__reduce_ex__',
# '__repr__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__', 'short_description'] --> short_description, customized attribute


def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func
print(f.__doc__)
print(f.__annotations__)
print(f.__name__)
print(f.__defaults__)
print(f.__kwdefaults__)

def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

print(my_func.__code__)
print(my_func.__code__)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)


