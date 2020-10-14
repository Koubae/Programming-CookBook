from functools import reduce
from functools import lru_cache

# fib_1 = list(lambda n: reduce(lambda prev, n:
#             (prev[0] + prev[1], prev[0],
#             renge(n),
#             (0, 1))[0]))
n = range(10)
fib_1 = reduce(lambda prev, n:
            (prev[0] + prev[1], prev[0]),
            n,
            (0, 1))[0]

print(fib_1)


# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result





# Recursive Type 1
def fib(n):
    print ('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

# Class
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


# Memoization

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
def fib(n):
    print("Calculating fib({0})".format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib(10))