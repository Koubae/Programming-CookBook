from itertools import filterfalse



def gen_cubes(n):
    for i in range(n):
        print(f'yielding {i}')
        yield i**3


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 == 1


print(is_odd(4), is_odd(81)) # => False, True

filtered = filter(is_odd, gen_cubes(10))
print(list(filtered))
# yielding 0
# yielding 1
# yielding 2
# yielding 3
# yielding 4
# yielding 5
# yielding 6
# yielding 7
# yielding 8
# yielding 9
# [1, 27, 125, 343, 729]

##################
## FILTERFALSE####
##################

evens = filterfalse(is_even, gen_cubes(10))
odds = filterfalse(is_odd, gen_cubes(10))
print(list(evens))
# yielding 0
# yielding 1
# yielding 2
# yielding 3
# yielding 4
# yielding 5
# yielding 6
# yielding 7
# yielding 8
# yielding 9
# [0, 8, 64, 216, 512]


# print(list(filterfalse(lambda x: x%2, range(10))))
# [0, 2, 4, 6, 8]
