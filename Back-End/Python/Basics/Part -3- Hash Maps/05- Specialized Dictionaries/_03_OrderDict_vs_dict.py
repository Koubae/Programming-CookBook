from collections import OrderedDict
from timeit import timeit


d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)



print(d1)
print(d2)

OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])
{'a': 1, 'b': 2, 'c': 3, 'd': 4}


for k in reversed(d1):
    print(k)


for k in reversed(list(d2.keys())):
    print(k)

print(d2)
print(first_key)

#{'a': 1, 'b': 2, 'c': 3, 'd': 4}


d1 = OrderedDict(a=1, b=2, c=3, d=4)
d2 = dict(a=1, b=2, c=3, d=4)

print(d2)
print(d2.popitem())
print(d2)
#
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ('d', 4)
# {'a': 1, 'b': 2, 'c': 3}


def popitem(d, last=True):
    if last:
        return d.popitem()
    else:
        first_key = next(iter(d.keys()))
        return first_key, d.pop(first_key)


d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2))
print(d2)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ('d', 4)
# {'a': 1, 'b': 2, 'c': 3}

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
print(popitem(d2, last=False))
print(d2)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# ('a', 1)
# {'b': 2, 'c': 3, 'd': 4}

d2 = dict(a=1, b=2, c=3, d=4)
print(d2)
key = 'b'
d2[key] = d2.pop(key)
print(d2)



d = dict(a=1, b=2, c=3, d=4, e=5, f=6)
key = 'c'

print(d.keys())

# first move desired key to end
d[key] = d.pop(key)
print(d.keys())

keys = list(d.keys())[:-1]
for key in keys:
    d[key] = d.pop(key)
    print(d.keys())

print(d)
#
# dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])
# dict_keys(['a', 'b', 'd', 'e', 'f', 'c'])
# dict_keys(['b', 'd', 'e', 'f', 'c', 'a'])
# dict_keys(['d', 'e', 'f', 'c', 'a', 'b'])
# dict_keys(['e', 'f', 'c', 'a', 'b', 'd'])
# dict_keys(['f', 'c', 'a', 'b', 'd', 'e'])
# dict_keys(['c', 'a', 'b', 'd', 'e', 'f'])
#{'c': 3, 'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6}

def move_to_end(d, key, *, last=True):
    d[key] = d.pop(key)

    if not last:
        for key in list(d.keys())[:-1]:
            d[key] = d.pop(key)


d = dict(a=1, b=2, c=3, d=4, e=5, f=6)

move_to_end(d, 'c')
print(d)

#{'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6, 'c': 3}

move_to_end(d, 'c', last=False)
print(d)

#{'c': 2, 'a': 1, 'b': 2, 'd': 3, 'e': 4, 'f': 5}


d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 20, 'c': 30, 'a': 10}



def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        for k1, k2 in zip(d1.keys(), d2.keys()):
            if k1 != k2:
                return False
        return True
    else:
        return False


def dict_equal_sensitive(d1, d2):
    if d1 == d2:
        return all(map(lambda el: el[0] == el[1],
                       zip(d1.keys(), d2.keys())
                       )
                   )
    else:
        return False



def create_dict(n=100):
    d = dict()
    for i in range(n):
        d[i] = i
    return d

def create_ordered_dict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[i] = i

timeit('create_dict(10_000)', globals=globals(), number=1_000)

#0.46366495298570953

print(timeit('create_ordered_dict(10_000)', globals=globals(), number=1_000))

#0.718640872015385


d1 = create_dict(10_000)
d2 = create_ordered_dict(10_000)

timeit('d1[9_999]', globals=globals(), number=100_000)



timeit('d2[9_999]', globals=globals(), number=100_000)


n = 1_000_000
d1 = create_dict(n)
print(timeit('d1.popitem()', globals=globals(), number=n))



n = 1_000_000
d2 = create_ordered_dict(n)
timeit('d2.popitem(last=True)', globals=globals(), number=n)


#0.26186515000881627


n = 100_000
d1 = create_dict(n)
timeit('popitem(d1, last=False)', globals=globals(), number=n)



#2.9098294480063487


n = 100_000
d2 = create_ordered_dict(n)
print(timeit('d2.popitem(last=False)', globals=globals(), number=n))

