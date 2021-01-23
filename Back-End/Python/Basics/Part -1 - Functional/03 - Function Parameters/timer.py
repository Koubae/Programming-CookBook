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