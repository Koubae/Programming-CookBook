import operator



a = 2 + 5j
a.real
# 2

l = [10+1j, 8+2j, 5+3j]
sorted(l, key=operator.attrgetter('real'))
# [(5+3j), (8+2j), (10+1j)]

l = ['aaz', 'aad', 'aaa', 'aac']
sorted(l, key=operator.itemgetter(-1))
# ['aaa', 'aac', 'aad', 'aaz']

#  based on the first item of each tuple
l = [(2, 3, 4), (1, 2, 3), (4, ), (3, 4)]
sorted(l, key=operator.itemgetter(0))
# [(1, 2, 3), (2, 3, 4), (3, 4), (4,)]

# Slicing
l = [1, 2, 3, 4]
l[0:2]
l[0:2] = ['a', 'b', 'c']
print(l)
# ['a', 'b', 'c', 3, 4]
del l[3:5]
print(l)
# ['a', 'b', 'c']

# Using operator

l = [1, 2, 3, 4]
operator.getitem(l, slice(0,2))
# [1, 2]
operator.setitem(l, slice(0,2), ['a', 'b', 'c'])
print(l)
# ['a', 'b', 'c', 3, 4]
operator.delitem(l, slice(3, 5))
print(l)
# ['a', 'b', 'c']

# Calling another Callable
x = 'python'
x.upper()
operator.methodcaller('upper')('python')
# 'PYTHON'
operator.attrgetter('upper')(x)()
# 'PYTHON'