from time import perf_counter
from functools import wraps
from functools import reduce

def timed(fn):

    @wraps(fn)
    def inner(*args, **kwargs):

        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str,
                                                      elapsed))
        return result
    return inner

def timed(num_reps=1):
    def decorator(fn):

        @wraps(fn)
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(num_reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_elapsed = total_elapsed / num_reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_elapsed,
                                                             num_reps))
            return result
        return inner
    return decorator

# Using Recursion
def calc_recursive_fib(n):

    if n <=2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

print(calc_recursive_fib(10))
# 55

@timed
def fib_recursed(n):
    return calc_recursive_fib(n)

print(fib_recursed(10))

# @timed
# def fib_recursive_fib_2(n):
#
#     if n <=2:
#         return 1
#     else:
#         return fib_recursive_fib_2(n-1) + fib_recursive_fib_2(n-2)
#
# print(fib_recursive_fib_2(25))


# Using a Loop
@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1

    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(f'Using Fib Loop --> {fib_loop(10)}')

#Using Reduce
@timed
def fib_reduce(n):

    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]),
                   dummy,
                   initial)
    return fib_n[0]

print(f'With Fib Reduce Func --> {fib_reduce(10)}')

for i in range(10):
    result = fib_loop(10)

for i in range(10):
    result = fib_reduce(10)


# Other

def timer(func):
    """Print the runtime of the decorated function"""
    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])