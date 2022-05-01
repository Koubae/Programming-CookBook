# timing.py
"""
Times how long a snippet of code takes to run
over multiple iterations
"""

from time import perf_counter
from collections import namedtuple
import argparse


Timing = namedtuple('Timing', 'repeats elapsed average')


def timeit(code, repeats=10):
    code = compile(code, filename='<string>', mode='exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed / repeats
    return Timing(repeats, elapsed, average) # Create a instance of Timing


if __name__ == '__main__':
    # get code from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code',
                        type=str, help='The Python code snippet')
    parser.add_argument('-r', '--repeats',
                        type=int, default=10,
                        help='Number of times to repeat the test.')
    args = parser.parse_args()
    print(f'Timing. {args.code}...')
    print(timeit(code=str(args.code), repeats=args.repeats))

# python timing.py -r 100  code
# Timing. code...
# Timing(repeats=100, elapsed=4.0400000000002934e-05, average=4.0400000000002935e-07)

# From Terminal python timing.py code
# Timing. code...
# Timing(repeats=10, elapsed=6.699999999998374e-06, average=6.699999999998374e-07)
# usage: timing.py [-h] [-r REPEATS] code
#
# Times how long a snippet of code takes to run over multiple iterations
#
# positional arguments:
#   code                  The Python code snippet
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -r REPEATS, --repeats REPEATS
#                         Number of times to repeat the test.
