from functools import wraps
from functools import lru_cache
from time import perf_counter

class Fib:

    def __init__(self):
        self.cache = {1: 1, 2: 1}

    def fib(self, n):
        if n not in self.cache:
            print(f'Calculating fib --> {n}')
            self.cache[n] = self.fib(n-1) + self.fib(n - 2)
        return self.cache[n]

f = Fib()

print(f.fib(1))

print(f.fib(10))
# Calculating fib --> 10
# Calculating fib --> 9
# Calculating fib --> 8
# Calculating fib --> 7
# Calculating fib --> 6
# Calculating fib --> 5
# Calculating fib --> 4
# Calculating fib --> 3
# 55

# Closure

def fib():

    cache = {1: 1, 2: 2}

    def calc_fib(n):
        if n not in cache:
            print(f'Calculating fib --> {n}')
            cache[n] = calc_fib(n-1) + calc_fib(n -2)
            print(cache)
        return cache[n]
    return calc_fib

f = fib()
print(f(10))

#Using a decorator
def memoize_fib(fn):

    cache = dict()
    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize_fib
def fib(n):
    print(f'Calculating fib --> {n}')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))

def memoize(fn):

    cache = dict()

    @wraps(fn)
    def inner(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return inner

@memoize
def fib(n):
    print(f'Calculating Fib --> {n}')
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))


@lru_cache()
def fact(n):
    print("Calculating fact({0})".format(n))
    return 1 if n < 2 else n * fact(n-1)

print(fact(5))

@lru_cache()
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))


def fib_no_memo(n):
    return 1 if n < 3 else fib_no_memo(n-1) + fib_no_memo(n-2)

start = perf_counter()
result = fib_no_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))

@lru_cache()
def fib_memo(n):
    return 1 if n < 3 else fib_memo(n - 1) + fib_memo(n - 2)

start = perf_counter()
result = fib_memo(35)
print("result={0}, elapsed: {1}s".format(result, perf_counter() - start))

@lru_cache(maxsize=8)
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)


##############
import functools
from decorators import count_calls

def cache(func):
    """Keep a cache of previous function calls"""
    @functools.wraps(func)
    def wrapper_cache(*args, **kwargs):
        cache_key = args + tuple(kwargs.items())
        if cache_key not in wrapper_cache.cache:
            wrapper_cache.cache[cache_key] = func(*args, **kwargs)
        return wrapper_cache.cache[cache_key]
    wrapper_cache.cache = dict()
    return wrapper_cache

@cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)
