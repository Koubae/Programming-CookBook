import math
from itertools import islice


def factorials(n):
    for i in range(n+1):
        yield math.factorial(i)


facts = factorials(100)
# print(facts[0:2]) => TypeError: 'generator' object is not subscriptable


def slice_(iter, start, stop):
    for _ in range(0, start): # Iterator to a Fix starting point
        next(iter)

    for _ in range(start, stop):
        yield next(iter)

my_slice = slice_(factorials(10), 4, 10)
my_slice2 = slice_(factorials(10), 6, 10)
print(my_slice)
print(list(my_slice))
print(list(my_slice2))
# [24, 120, 720, 5040, 40320, 362880]
# [720, 5040, 40320, 362880]ç

## itertools.islice
# It does not support negative indices,
# or step values, but it does support None for all the arguments
print('==='*15)
print(list(islice(factorials(10), 4, 10, 1)))
print(list(islice(factorials(10), None, None, 2)))
# [24, 120, 720, 5040, 40320, 362880]
# [1, 2, 24, 720, 40320, 3628800]

#Infinite Iterators

def factorial():
    index = 0
    while True:
        print(f'Yielding Factorial ({index})...')
        yield math.factorial(index)
        index += 1

list(islice(factorial(), 9))

# Yielding Factorial (0)...
# Yielding Factorial (1)...
# Yielding Factorial (2)...
# Yielding Factorial (3)...
# Yielding Factorial (4)...
# Yielding Factorial (5)...
# Yielding Factorial (6)...
# Yielding Factorial (7)...
# Yielding Factorial (8)...


