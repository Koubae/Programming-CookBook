
# Interning strings (making them singleton objects) means that testing
# for string equality can be done faster by comparing the memory address:
a = 'this_is_a_long_string'
b = 'this_is_a_long_string'
print('a==b:', a == b)
print('a is b:', a is b)

# a==b: True
# a is b: True

# Here's where this technique fails:

b = 'hello world'
print('a==b:', a==b)
print('a is b:', a is b)

# a==b: True
# a is b: False

import sys
import time

a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id(a))
print(id(b))
print(id(c))

# 1342722172080
# 1342722172080
# 1342722174896
# Notice how a and b are pointing to the same object, but c is NOT.

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()

print('equality: ', end-start)

# equality:  2.965451618090112


start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()

print('identity: ', end-start)

# identity:  0.28690104431129626
print('==='*30)
print('Python Peephole Optimizations'.upper())


def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 10
    f = [1, 2] * 5

print(my_func.__code__.co_consts)
# 24 * 60 was pre-calculated and cached as a constant (1440)
# (None, 1440, (1, 2, 1, 2, 1, 2, 1, 2, 1, 2), 'abcabcabc', 'ababababababababababab', 'the quick brown foxthe quick brown
# foxthe quick brown foxthe quick brown foxthe quick brown
# foxthe quick brown foxthe quick brown foxthe quick brown foxthe quick brown
# foxthe quick brown fox', 1, 2, 5)

def my_func():
    if e in [1, 2, 3]:
        pass

print(my_func.__code__.co_consts)
# >> (None, 1, 2, 3, (1, 2, 3))
# the mutable list [1, 2, 3] was converted to an immutable tuple.

def my_func():
    if e in {1, 2, 3}:
        pass

print(my_func.__code__.co_consts)
# >>> (None, 1, 2, 3, frozenset({1, 2, 3}))
# set membership will be converted to frozen set membership:


