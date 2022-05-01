from itertools import count, islice
from decimal import Decimal


g = count(10)
print(list(islice(g, 5)))
# [10, 11, 12, 13, 14]
g = count(10, step=2)
print(list(islice(g, 5)))
# [10, 12, 14, 16, 18]
g = count(10.5, 0.5)
print(list(islice(g, 5)))
# [10.5, 11.0, 11.5, 12.0, 12.5]

g = count(1+1j, 1+2j)

print(list(islice(g, 5)))
g = count(Decimal('0.0'), Decimal('0.1'))
print(islice(g, 5))
print(list(islice(g, 5)))
# <itertools.islice object at 0x000001EB95CBA810>
# [Decimal('0.0'), Decimal('0.1'), Decimal('0.2'), Decimal('0.3'), Decimal('0.4')]