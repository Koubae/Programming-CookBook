from itertools import starmap


def add(x, y):
    return x + y

print(list(starmap(add, [(0,0), (1,1), (2,2)])))
# [0, 2, 4]

