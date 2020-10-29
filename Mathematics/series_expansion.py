import math
from decorators import debug
# https://en.wikipedia.org/wiki/E_(mathematical_constant)
# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))