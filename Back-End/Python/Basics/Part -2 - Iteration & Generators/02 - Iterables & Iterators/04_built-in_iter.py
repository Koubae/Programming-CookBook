l = [1, 2, 3]

iter_1 = iter(l)
print(type(iter_1))

print(next(iter_1)) # 1
print(next(iter_1)) # 2
print(next(iter_1)) # 3
# print(next(iter_1)) # StopIteration
 
print(id(iter_1), id(iter(iter_1)))


print('__next__' in dir(iter_1)) # True
 
print('__iter__' in dir(iter_1)) # True

 

print('__iter__' in dir(l)) # True
print('__next__' in dir(l)) # False

print('__getitem__' in dir(l)) # True

print('__getitem__' in dir(set)) # False

print('__iter__' in dir(set)) # True

d = dict(a=1, b=2, c=3)
iter_d = iter(d)
print(next(iter_d)) # a => Keys

iter_vals = iter(d.values())
print(next(iter_vals)) # 1 Values

iter_items = iter(d.items())
print(next(iter_items)) # ('a', 1) => Iters



