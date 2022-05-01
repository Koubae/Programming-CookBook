# ========================= < Simple Timer > ========================= #

import time


def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (((end - start) / rep), (end - start))

# print(time_it(print, 1, 2, 3, 4, sep='-', end=' *** '))

def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return list((n**i for i in range(start, end)))

# compute_powers_1(2, end=5)
# compute_powers_2(2, end=5)
# list(compute_powers_3(2, end=5))


print(time_it(compute_powers_1, n=2, end=20000, rep=4))
print(time_it(compute_powers_2, 2, end=20000, rep=4))
print(time_it(compute_powers_3, 2, end=20000, rep=4))

# (0.42911004999999997, 1.7164401999999999)
# (0.406271425, 1.6250857)
# (0.41299407499999996, 1.6519762999999998)


# ========================= < function's closure > ========================= #

def timer():

    start = perf_counter()

    def elapsed():
        return perf_counter() - start

    return elapsed

# ========================= < function's Decorators > ========================= #
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


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])