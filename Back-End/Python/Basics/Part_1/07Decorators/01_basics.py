import inspect

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

def counter(fn):

    count = 0

    def inner(*args, **kwargs):

        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    return inner


def add(a, b=0):
    """
        returns the sum of a and b
    """
    print(a + b)
    return a + b

help(add)
id(add)
# Now we create a closure using the add function as an argument to the counter function:
add = counter(add)
add(1, 2)
add(2, 2)

@counter
def mul(a : float, b: float=1, c: float=1) -> float:
    """
        returns the product of a, b, and c
    """
    print(a * b * c)
    return a * b * c

mul(1, 2, 3)

print(inspect.getsource(add))
print(inspect.getsource(mul))

print(inspect.signature(add))
print(inspect.signature(mul))

print(inspect.signature(add).parameters.get('args'))

######################################################

def counter(fn):

    count = 0

    def inner(*args, **kwargs):

        nonlocal count
        count += 1
        print("{0} was called {1} times".format(fn.__name__, count))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

@counter
def add(a:int, b: int=10) -> int:
    """
       returns sum of two integers
    """
    return a + b

print(add(5, 10))


# Stack Decorators

def dec_1(fn):
    def inner():
        print('Running Dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running Dec_2')
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print('Running my func')

my_func()
# Running Dec_1
# Running Dec_2
# Running my func

@dec_2
@dec_1
def my_func():
    print('Running my func')
my_func()
# Running Dec_2
# Running Dec_1
# Running my func


# PythonDecorators/entry_exit_function.py
def entry_exit(f):
    def new_f():
        print("Entering", f.__name__)
        f()
        print("Exited", f.__name__)
    return new_f

@entry_exit
def func1():
    print("inside func1()")

@entry_exit
def func2():
    print("inside func2()")

func1()
func2()
print(func1.__name__)