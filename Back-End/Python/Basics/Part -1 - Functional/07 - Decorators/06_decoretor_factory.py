from time import perf_counter
from functools import wraps
def dec_factory():
    print('Running Dec Factory')

    def dec(fn):
        print('Running Decorator')
        def inner(*args, **kwargs):
            print('Running Wrapper')
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_factory()
def my_func(a, b):
    print(a, b)

my_func(10, 20)

# Running Dec Factory
# Running Decorator
# Running Wrapper
# 10 20

def dec_factory_2():
    def dec(fn):
        def inner(*args, **kwargs):
            print('Running Wrapper')
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_factory()
def my_func(a, b):
    return a + b
my_func(10, 20)

# Decoretor Factory with Argumenrs

def dec_factory(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('running decorator inner')
            print('free vars: ', a, b)  # a and b are free variables!
            return fn(*args, **kwargs)
        return inner
    return dec

@dec_factory(10, 20)
def my_func():
    print('python rocks')

my_func()


def timed(num_reps=1):
    def decorator(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += end - start
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                             num_reps))
            return result
        return inner
    return decorator

def calc_fib_recursive(n):
    return 1 if n < 3 else calc_fib_recursive(n - 1) + calc_fib_recursive(n - 2)

@timed(10)
def fib(n):
    return calc_fib_recursive(n)

fib(10)

