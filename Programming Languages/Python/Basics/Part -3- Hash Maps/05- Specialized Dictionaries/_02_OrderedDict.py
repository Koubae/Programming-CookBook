from collections import OrderedDict


d = OrderedDict()


OrderedDict([('z', 'hello'), ('y', 'world'), ('a', 'python')])


for key in d:
    print(key)

for key in reversed(d):
    print(key)

d = {'a': 1, 'b': 2}
for key in reversed(d):
    print(key)



d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40



OrderedDict([('first', 10), ('second', 20), ('third', 30), ('last', 40)])
d.popitem()
OrderedDict([('first', 10), ('second', 20), ('third', 30)])

d.popitem(last=False)
OrderedDict([('second', 20), ('third', 30)])

d = OrderedDict()
d['first'] = 10
d['second'] = 20
d['third'] = 30
d['last'] = 40

d.move_to_end('second')
OrderedDict([('first', 10), ('third', 30), ('last', 40), ('second', 20)])
d.move_to_end('third', last=False)



d1 = {'a': 10, 'b': 20}
d2 = {'b': 20, 'a': 10}


d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = OrderedDict()
d2['a'] = 10
d2['b'] = 20

d3 = OrderedDict()
d3['b'] = 20
d3['a'] = 10


print(d1)
print(d2)
print(d3)

OrderedDict([('a', 10), ('b', 20)])
OrderedDict([('a', 10), ('b', 20)])
OrderedDict([('b', 20), ('a', 10)])


print(isinstance(d1, OrderedDict))


print(isinstance(d1, dict))

d1 = OrderedDict()
d1['a'] = 10
d1['b'] = 20

d2 = {'b': 20, 'a': 10}

print(d1)
print(d2)

print(OrderedDict([('a', 10), ('b', 20)]))
#{'b': 20, 'a': 10}








def create_ordereddict(n=100):
    d = OrderedDict()
    for i in range(n):
        d[str(i)] = i
    return d


def create_deque(n=100):
    return deque(range(n))



def pop_all_ordered_dict(n=1000, last=True):
    d = create_ordereddict(n)
    while True:
        try:
            d.popitem(last=last)
        except KeyError:
            # done popping
            break


def pop_all_deque(n=1000, last=True):
    dq = create_deque(n)
    if last:
        pop = dq.pop
    else:
        pop = dq.popleft

    while True:
        try:
            pop()
        except IndexError:
            break

timeit('create_ordereddict(10_000)',
       globals=globals(),
       number=1_000)

# 2.2906384040252306


print(timeit('create_deque(10_000)',
       globals=globals(),
       number=1_000))



# 0.1509137399843894


n = 10_000
number = 1_000

results = dict()

results['dict_create'] = timeit('create_ordereddict(n)',
                                globals=globals(),
                                number=number)

results['deque_create'] = timeit('create_deque(n)',
                                 globals=globals(),
                                 number=number)

results['dict_create_pop_last'] = timeit(
    'pop_all_ordered_dict(n, last=True)',
    globals=globals(), number=number)

results['dict_create_pop_first'] = timeit(
    'pop_all_ordered_dict(n, last=False)',
    globals=globals(), number=number)

results['deque_create_pop_last'] = timeit(
    'pop_all_deque(n, last=True)',
    globals=globals(), number=number
)

results['deque_create_pop_first'] = timeit(
    'pop_all_deque(n, last=False)',
    globals=globals(), number=number
)

results['dict_pop_last'] = (
    results['dict_create_pop_last'] - results['dict_create'])

results['dict_pop_first'] = (
    results['dict_create_pop_first'] - results['dict_create'])

results['deque_pop_last'] = (
    results['deque_create_pop_last'] - results['deque_create'])

results['deque_pop_first'] = (
    results['deque_create_pop_first'] - results['deque_create'])

for key, result in results.items():
    print(f'{key}: {result}')

# dict_create: 2.3447022930486128
# deque_create: 0.15744277997873724
# dict_create_pop_last: 4.827248840010725
# dict_create_pop_first: 4.72704964800505
# deque_create_pop_last: 0.3677212379989214
# deque_create_pop_first: 0.3731844759895466
# dict_pop_last: 2.482546546962112
# dict_pop_first: 2.382347354956437
# deque_pop_last: 0.2102784580201842
# deque_pop_first: 0.2157416960108094

