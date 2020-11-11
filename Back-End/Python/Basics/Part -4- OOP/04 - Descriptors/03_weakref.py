import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value

class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Person(name={self.name})'

p1 = Person('Guido')
p2 = p1



p1_id = id(p1)
p2_id = id(p2)

p1_id == p2_id, ref_count(p1_id)

# (True, 2)

del p2

ref_count(p1_id)

# 1

del p1

ref_count(p1_id)

# -370994432650002694

import weakref

p1 = Person('Guido')

p1_id = id(p1)

ref_count(p1_id)
# 1
p2 = p1

ref_count(p1_id)

# 2

weak1 = weakref.ref(p1)

ref_count(p1_id)

# 2

print(weak1)
# <weakref at 0x7fbae83667c8; to 'Person' at 0x7fbae8359908>

hex(p1_id)

# '0x7fbae8359908'

weak1 is p1

# False
In [21]:
print(ref_count(p1_id))

# 2

weak1() is p1
# True

print(weak1())
Person(name=Guido)

ref_count(p1_id)
# 2

p3 = weak1()

print(p1 is p3)
# True

print(ref_count(p1_id))

# 3

print(weakref.getweakrefcount(p1), ref_count(p1_id))

# (1, 3)

import sys

print(sys.getrefcount(p1))
# 4
del p3
del p2

print(ref_count(p1_id))

# 1

del p1


print(weak1)
# <weakref at 0x7fbae83667c8; dead>


obj = weak1()

print(obj is None)
# True

In [37]:
l = [1, 2, 3]
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)
# cannot create weak reference to 'list' object

l = {'a': 1}
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)
# cannot create weak reference to 'dict' object

l = 100
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)
# cannot create weak reference to 'int' object

l = 'python'
try:
    w = weakref.ref(l)
except TypeError as ex:
    print(ex)
# cannot create weak reference to 'str' object

p1 = Person('Guido')

d = weakref.WeakKeyDictionary()

print(ref_count(id(p1)))
# 1

print(weakref.getweakrefcount(p1))
# 0

d[p1] = 'Guido'
print(ref_count(id(p1)), weakref.getweakrefcount(p1))
# (1, 1)


hex(id(p1)), list(d.keyrefs())
# ('0x7fbae83635c0',
#  [<weakref at 0x7fbae8381958; to 'Person' at 0x7fbae83635c0>])

del p1

list(d.keyrefs())
# []


try:
    d['python'] = 'test'
except TypeError as ex:
    print(ex)

class Person:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name


p1 = Person('Guido')
p2 = Person('Guido')

p1 == p2
# True


try:
    hash(p1)
except TypeError as ex:
    print(ex)
# unhashable type: 'Person'

try:
    d[p1] = 'Guido'
except TypeError as ex:
    print(ex)
# unhashable type: 'Person'