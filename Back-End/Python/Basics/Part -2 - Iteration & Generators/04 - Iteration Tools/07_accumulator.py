import operator
from itertools import accumulate

def sum_(iterable):
    it = iter(iterable)
    acc = next(it)
    yield acc
    yield acc

    for item in it:
        acc += item
        yield acc



for item in sum_([10, 20, 30]):
    print(item)
# 10
# 10
# 30
# 60


def running_reduce(fn, iterable, start=None):
    it = iter(iterable)
    if start is None:
        accumulator = next(it)
    else:
        accumulator = start

    yield accumulator

    for item in it:
        accumulator = fn(accumulator, item)
        yield accumulator

print(list(running_reduce(operator.add, [10, 20, 30])))
#[10, 30, 60]
print(list(running_reduce(operator.mul, [1, 2, 3, 4])))
# [1, 2, 6, 24]
print(list(running_reduce(operator.mul, [1, 2, 3, 4], 10)))
# [10, 10, 20, 60, 240]

# ACCUMULATE

print(list(accumulate([10, 20, 30])))
# [10, 30, 60]
print(list(accumulate([1, 2, 3, 4], operator.mul)))

# [1, 2, 6, 24]