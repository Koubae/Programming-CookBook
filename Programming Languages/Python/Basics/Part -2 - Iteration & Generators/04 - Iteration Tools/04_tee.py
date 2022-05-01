from itertools import tee


def squares(n):
    for i in range(n):
        yield i**2


gen = squares(10)
print(gen)

iters = tee(squares(10), 3)
print(iters)
# <generator object squares at 0x00000256D4F78C10>
# (<itertools._tee object at 0x00000256D54E1100>,
#  <itertools._tee object at 0x00000256D54E10C0>,
#  <itertools._tee object at 0x00000256D54E1140>)
iter1, iter2, iter3 = iters
print(next(iter1), next(iter1), next(iter1)) # => 0, 1, 4


l = [1, 2, 3, 4]
lists = tee(l, 2) # Not List but iterators
for i in lists:
    print(list(i))

# [1, 2, 3, 4]
# [1, 2, 3, 4]