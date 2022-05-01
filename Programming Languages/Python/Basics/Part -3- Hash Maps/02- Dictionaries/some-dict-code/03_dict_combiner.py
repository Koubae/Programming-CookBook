from itertools import chain
from functools import reduce

from pprint import pprint
d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}
d4 = d3
all_entries = chain(d1.items(), d2.items(), d3.items())
y = {'d_1': d1, 'd_2': d2, 'd_3d': 3}
# print(list(x))
# [('python', 10), ('java', 3), ('c#', 8), ('javascript', 15),
#  ('java', 10), ('c++', 10), ('c#', 4), ('go', 9), ('python', 6),
#  ('erlang', 5), ('haskell', 2), ('python', 1), ('pascal', 1)]
# print(y)
# {'python': 1, 'java': 10, 'c#': 4, 'javascript':
# 15, 'c++': 10, 'go': 9, 'erlang':
# 5, 'haskell': 2, 'pascal': 1}
z = d1.keys() | d2.keys() | d3.keys()
a = d1.keys() & d2.keys() & d3.keys()
# print('Union |', z)
# print('Intersection & ', a)
# print('Difference -', z - a)
# Union | {'go', 'python', 'java', 'erlang', 'javascript', 'pascal', 'haskell', 'c#', 'c++'}
# Intersection &  {'python'}
# Difference - {'go', 'javascript', 'java', 'pascal', 'haskell', 'erlang', 'c#', 'c++'}

print(list(all_entries))


def get_response(*args):
    result = []
    UNION = reduce(lambda x, y: x | y.keys(), (args))

    def unify_dict():
        for value in UNION:
            d1_ = d1.get(value, 0)
            d2_ = d2.get(value, 0)
            d3_ = d3.get(value, 0)
            result.extend([(value, reduce(lambda x, y: x + y, [d1_, d2_, d3_]))])
        return result
    unification = unify_dict()

    return {k: v for k, v in sorted(unification, key=lambda dict_value: dict_value[1], reverse=True)}

print(get_response(d1, d2, d3, d4))

# {'python': 17, 'javascript': 15, 'java': 13,
# 'c#': 12, 'c++': 10, 'go': 9, 'erlang': 5, 'haskell': 2, 'pascal': 1}


def merge(*dicts):
    unsorted = {}
    for d in dicts:
        for k, v in d.items():
            unsorted[k] = unsorted.get(k, 0) + v

    # create a dictionary sorted by value
    return dict(sorted(unsorted.items(), key=lambda e: e[1], reverse=True))


merged = merge(d1, d2, d3)
for k, v in merged.items():
    print(k, v)



# python 17
# javascript 15
# java 13
# c# 12
# c++ 10
# go 9
# erlang 5
# haskell 2
# pascal 1



# d = {k: v for k, v in sorted(l, key=lambda dict_value: dict_value[1], reverse=True)}
# print(d)








#
# for value in z:
#     d1_ = d1.get(value, 0)
#     d2_ = d2.get(value, 0)
#     d3_ = d3.get(value, 0)
#     result = [(value, reduce(lambda x, y: x+y, [d1_, d2_, d3_ ]))]
#     l.extend(result)



d = {}
for i in all_entries: # Iterater through all items in the dicts
    if i[0] in z: # check if item in intersection of all dicts
        # print(i)
        if i[0] not in d: # Set default to dict
            d.setdefault(i[0], i[1])
        else: # Otherwise adds new value
            x = d.get(i[0])
            f = x + i[1]
            d[i[0]] = f

# print(d)
