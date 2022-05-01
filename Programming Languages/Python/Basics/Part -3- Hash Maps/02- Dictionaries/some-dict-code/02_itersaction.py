# Find Intersection between d1 and d2, return Dict, key is tuple
# containing values from d1 and d2 of Intersection
# d = {'b': (2, 20), 'c': (3, 30)}
d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}
x = d1.keys() & d2.keys()
y = d1.items() | d2.items()
print(x) # {'b', 'c'}
intersect_tuple = {k: (d1.get(k), d2.get(k)) for k in (d1.keys() & d2.keys())}
print(intersect_tuple)

# {'b': (2, 20), 'c': (3, 30)}


def intersector(dict1, dict2):
    return {k: (dict1.get(k), dict2.get(k)) for k in (dict1.keys() & dict2.keys())}


my_new_dict = intersector(d1, d2)
print(my_new_dict)

# {'b': (2, 20), 'c': (3, 30)}


def intersect(d1, d2):
    d1_keys = d1.keys()
    d2_keys = d2.keys()
    keys = d1_keys & d2_keys
    d = {k: (d1[k], d2[k]) for k in keys}
    return d


print(intersect(d1, d2))
# {'b': (2, 20), 'c': (3, 30)}
