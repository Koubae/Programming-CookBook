from contextlib import contextmanager
from time import perf_counter, sleep
import sys
from contextlib import redirect_stdout


@contextmanager
def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()


with open_file('test.txt') as f:
    print(f.readlines())


@contextmanager
def timer():
    stats = dict()
    start = perf_counter()
    stats['start'] = start
    yield stats
    end = perf_counter()
    stats['end'] = end
    stats['elapsed'] = end - start


with timer() as stats:
    sleep(1)



print(stats)




@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout

with out_to_file('test.txt'):
    print('line 1')
    print('line 2')

with open('test.txt') as f:
    print(f.readlines())

with open('test.txt', 'w') as f:
    with redirect_stdout(f):
        print('Look on the bright side of life')

with open('test.txt') as f:
    print(f.readlines())