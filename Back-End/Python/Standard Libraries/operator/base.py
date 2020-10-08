import operator
from functools import reduce


dir(operator)


operator.add(1, 2)
# 3

operator.mul(2, 3)
# 6
operator.pow(2, 3)
# 8
operator.mod(13, 2)
# 1
operator.floordiv(13, 2)
# 6
operator.truediv(3, 2)
# 1.5

reduce(lambda x, y: x*y, [1, 2, 3, 4])
# 24

reduce(operator.mul, [1, 2, 3, 4])
# 24

## Comparison and Boolean Operators
operator.lt(10, 100)
#True
operator.le(10, 10)
# True
operator.is_('abc', 'def')
# False
operator.truth([1,2])
# True
operator.truth([])
# False
operator.and_(True, False)
# False
operator.or_(True, False)
# True

# Element and Attribute Getters and Setters

my_list = [1, 2, 3, 4]
my_list[1]

operator.getitem(my_list, 1)
# 2 

my_list = [1, 2, 3, 4]
my_list[1] = 100
del my_list[3]
print(my_list)
# >>> [1, 100, 3]

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
operator.delitem(my_list, 3)
print(my_list)
# >>> [1, 100, 3]

f = operator.itemgetter(2)
f(my_list)
# 3
x = 'python'
f(x)
# 't'


f = operator.itemgetter(2, 3)
my_list = [1, 2, 3, 4]
f(my_list)
# (3, 4)
x = 'pytyhon'
f(x)
# ('t', 'y')
