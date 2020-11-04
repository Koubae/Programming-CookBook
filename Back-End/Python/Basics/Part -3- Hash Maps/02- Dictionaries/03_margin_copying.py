from copy import deepcopy
from random import randint
from timeit import timeit



d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}



d1.update(d2)
print(d1)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}



d1 = {'a': 1, 'b': 2}


d1.update(b=20, c=30)
print(d1)

# {'a': 1, 'b': 20, 'c': 30}


d1 = {'a': 1, 'b': 2}



d1.update([('c', 2), ('d', 3)])



# {'a': 1, 'b': 2, 'c': 2, 'd': 3}


d = {'a': 1, 'b': 2}
d.update((k, ord(k)) for k in 'python')
print(d)

# {'a': 1, 'b': 2, 'p': 112, 'y': 121, 't': 116, 'h': 104, 'o': 111, 'n': 110}



d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 200, 'd': 4}
d1.update(d2)
print(d1)

# {'a': 1, 'b': 200, 'c': 3, 'd': 4}



l1 = [1, 2, 3]
l2 = 'abc'
l = (*l1, *l2)
print(l)

# (1, 2, 3, 'a', 'b', 'c')



d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = {**d1, **d2}
print(d)

# {'a': 1, 'b': 2, 'c': 3, 'd': 4}



d1 = {'a': 1, 'b': 2}
d2 = {'b': 200, 'c': 3}
d = {**d1, **d2}
print(d)

# {'a': 1, 'b': 200, 'c': 3}



conf_defaults = dict.fromkeys(('host', 'port', 'user', 'pwd', 'database'), None)
print(conf_defaults)

# {'host': None, 'port': None, 'user': None, 'pwd': None, 'database': None}



conf_global = {
    'port': 5432,
    'database': 'deepdive'}


conf_dev = {
    'host': 'localhost',
    'user': 'test',
    'pwd': 'test'
}

conf_prod = {
    'host': 'prodpg.deepdive.com',
    'user': '$prod_user',
    'pwd': '$prod_pwd',
    'database': 'deepdive_prod'
}



config_dev = {**conf_defaults, **conf_global, **conf_dev}



print(config_dev)

# {'host': 'localhost', 'port': 5432, 'user': 'test', 'pwd': 'test', 'database': 'deepdive'}



config_prod = {**conf_defaults, **conf_global, **conf_prod}

:

print(config_prod)

# {'host': 'prodpg.deepdive.com', 'port': 5432, 'user': '$prod_user', 'pwd': '$prod_pwd', 'database': 'deepdive_prod'}


def my_func(*, kw1, kw2, kw3):
    print(kw1, kw2, kw3)


d = {'kw2': 20, 'kw3': 30, 'kw1': 10}

print(my_func(**d))





def my_func(**kwargs):
    for k, v in kwargs.items():
        print(k, v)



my_func(**d)


d = {'a': [1, 2], 'b': [3, 4]}


d1 = d.copy()



print(d)
print(d1)

# {'a': [1, 2], 'b': [3, 4]}
# {'a': [1, 2], 'b': [3, 4]}

del d['a']



print(d)
print(d1)

# {'b': [3, 4]}
# {'a': [1, 2], 'b': [3, 4]}


d['b'] = 100



print(d)
print(d1)

# {'b': 100}
# {'a': [1, 2], 'b': [3, 4]}


d = {'a': [1, 2], 'b': [3, 4]}
d1 = d.copy()
print(d)
print(d1)

# {'a': [1, 2], 'b': [3, 4]}
# {'a': [1, 2], 'b': [3, 4]}


d['a'].append(100)



print(d)

# {'a': [1, 2, 100], 'b': [3, 4]}


print(d1)

# {'a': [1, 2, 100], 'b': [3, 4]}


d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
    'posts': [100, 105, 200]
    }

d1 = d.copy()


d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)



d = {'id': 123445,
    'person': {
        'name': 'John',
        'age': 78},
     'posts': [100, 105, 200]
    }


d1 = deepcopy(d)


d1['person']['name'] = 'John Cleese'
d1['posts'].append(300)




print({'id': 123445, 'person': {'name': 'John', 'age': 78}, 'posts': [100, 105, 200]})



d1 = {'a': [1, 2], 'b':[3, 4]}
d = {**d1}


d1['a'].append(100)




big_d = {k: randint(1, 100) for k in range(1_000_000)}


def copy_unpacking(d):
    d1 = {**d}
    
def copy_copy(d):
    d1 = d.copy()

def copy_create(d):
    d1 = dict(d)
    
def copy_comprehension(d):
    d1 = {k: v for k, v in d.items()}




print(timeit('copy_unpacking(big_d)', globals=globals(), number=100))



# 2.480969894968439



print(timeit('copy_copy(big_d)', globals=globals(), number=100))

# 2.469855136005208


print(timeit('copy_create(big_d)', globals=globals(), number=100))

#2.4125180219998583



print(timeit('copy_comprehension(big_d)', globals=globals(), number=100))

#5.77224236400798