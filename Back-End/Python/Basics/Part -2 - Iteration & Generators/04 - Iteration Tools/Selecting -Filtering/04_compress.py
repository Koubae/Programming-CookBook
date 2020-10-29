from itertools import compress



data = ['a', 'b', 'c', 'd', 'e']
selectors = [True, False, 1, 0]

print(list(zip(data, selectors)))
# [('a', True), ('b', False), ('c', 1), ('d', 0)]
print([item for item,
      truth_value in zip(data, selectors)
      if truth_value])
# ['a', 'c']

print(list(compress(data, selectors)))

# ['a', 'c']

def filterfalse(predicate, iterable):
    # filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x

