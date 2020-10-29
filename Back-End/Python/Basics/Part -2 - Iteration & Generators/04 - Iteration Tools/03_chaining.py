from itertools import chain


def chain_iterables(*iterables):
    for iterable in iterables:
        yield from iterable

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain_iterables(l1, l2, l3):
    print(item)

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121

### Chain

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

for item in chain(l1, l2, l3):
    print(item)

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100
# 121
################################################

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(lists):
    for i in item:
        print(i)

# Or unpacking

l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4, 8))
l3 = (i**2 for i in range(8, 12))

lists = [l1, l2, l3]
for item in chain(*lists):
    print(item)



def squares():
    print('yielding 1st item')
    yield (i**2 for i in range(4))
    print('yielding 2nd item')
    yield (i**2 for i in range(4, 8))
    print('yielding 3rd item')
    yield (i**2 for i in range(8, 12))

def read_values(*args):
    print('finised reading args')

c = chain.from_iterable(squares())

for item in c:
    print(item)

# yielding 1st item
# 0
# 1
# 4
# 9
# yielding 2nd item
# 16
# 25
# 36
# 49
# yielding 3rd item
# 64
# 81
# 100
# 121


