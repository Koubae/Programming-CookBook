import random
# Python's sorted function kas a keyword-only argument that allows
# us to modify the values that are used to sort the list.


l = ['a', 'B', 'c', 'D']
print(sorted(l, key=str.upper))
# ['a', 'B', 'c', 'D']

# Same as
print(sorted(l, key = lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi': 100}
print(sorted(d, key=lambda k: d[k]))
# >>> ['ghi', 'abc', 'def']

# Sort complex numbers based on their distance from the origin


def dist(x):
    return x.real**2 + x.imag**2


l = [3+3j, 1+1j, 0]
print(sorted(l, key=lambda x: (x.real)**2 + (x.imag) **2))
# >>> [0, (1+1j), (3+3j)]

#  sort a list of strings based on the last character of the string
l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l, key=lambda s: s[-1]))
# >>> ['Cleese', 'Idle', 'Gilliam', 'Palin', 'Chapman', 'Jones']
print(sorted(l, key=lambda s: s[::-1]))
# >>> ['Idle', 'Cleese', 'Gilliam', 'Chapman', 'Palin', 'Jones']
print(sorted(l))
# >>> ['Chapman', 'Cleese', 'Gilliam', 'Idle', 'Jones', 'Palin']

# Randomizing an Iterable using Sorted

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(l, key=lambda x: random.random()))
# [10, 3, 2, 8, 1, 7, 4, 6, 5, 9]
print(sorted('abcdefg', key=lambda x: random.random()))
# ['c', 'a', 'e', 'f', 'b', 'd', 'g']
print(''.join(sorted('abcdefg', key=lambda x: random.random())))
# fbeagcd