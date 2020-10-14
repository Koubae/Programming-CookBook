# helpers

from .calculator import Calc



def say_hello(name):
    return f'Hello {name}'


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)