

def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = (*args, frozenset(kwargs.items()))
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner


@memoizer
def my_func(*, a, b):
    print('calculating a+b...')
    return a + b


print(my_func(a=1, b=2))
# calculating a+b...

my_func(a=1, b=2)
my_func(b=2, a=1)

# --------------#
# Solution 2
# --------------#

def memoizer(fn):
    cache = {}
    def inner(*args, **kwargs):
        key = frozenset(args) | frozenset(kwargs.items())
        if key in cache:
            return cache[key]
        else:
            result = fn(*args, **kwargs)
            cache[key] = result
            return result
    return inner


@memoizer
def adder(*args):
    print('calculating...')
    return sum(args)


adder(1, 2, 3)
adder(3, 2, 1)
adder(2, 1, 3)
adder(1, 2, 3, 4)
# calculating...

adder(4, 2, 1, 3)




