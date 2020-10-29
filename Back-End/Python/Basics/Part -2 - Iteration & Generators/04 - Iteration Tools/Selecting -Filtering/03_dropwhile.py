from itertools import dropwhile
from math import sin, pi

# The dropwhile function on the other hand starts the iteration once the predicate becomes False:

l = [1, 3, 5, 2, 1]

print(list(dropwhile(lambda x: x < 5, l)))
# [5, 2, 1]