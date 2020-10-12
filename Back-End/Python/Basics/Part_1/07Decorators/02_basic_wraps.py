from functools import wraps
import inspect

def counter(fn):

    count = 0

    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)

    return inner

@counter
def add(a: int, b: int=10) -> int:
    """
    returns sum of two integers
    """
    return a + b


print(inspect.getsource(add))
print(inspect.signature(add))
print(inspect.signature(add).parameters)
