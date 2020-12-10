from multiprocessing import Pool, cpu_count
import time
import os
from timeit import default_timer as timer
import functools


# map
def square(n):
    return n * n


def main():

    start = timer()
    print('==='*15 + ' < ' + f'CPU CORES={cpu_count()}' + ' > ' + '==='*15)
    values = (2, 4, 6, 8)

    with Pool() as pool:
        calc_sq = pool.map(square, values)
        print(f'Result= {calc_sq}')

    end = timer()
    print(f'Elapsed Time: {end - start}')


# starmap
def power(x, n):
    time.sleep(1)
    return x ** n


def star_map():

    start = timer()
    print('===' * 15 + ' < ' + f'CPU CORES={cpu_count()}' + ' > ' + '===' * 15)

    values = ((2, 2), (4, 3), (5, 5))

    with Pool() as pool:
        res = pool.starmap(power, values)
        print(res)

    end = timer()
    print(f'elapsed time: {end - start}')


# map and functools.partials
def inc(x):
    return x + 1

def dec(x):
    return x - 1

def add(x, y):
    return x + y

def smap(f):
    return f()


def multi_mapping():

    f_inc = functools.partial(inc, 4)
    f_dec = functools.partial(dec, 2)
    f_add = functools.partial(add, 3, 4)

    with Pool() as pool:
        res = pool.map(smap, [f_inc, f_dec, f_add])

        print(res)

    

if __name__ == '__main__':
    main()
    star_map()
    multi_mapping()