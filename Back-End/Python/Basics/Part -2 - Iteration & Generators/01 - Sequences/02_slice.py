# Converting Slice to Range
import sys

print(slice(1, 5).indices(10))
# (1, 5, 1)
print(list(range(1, 5, 1)))
# [1, 2, 3, 4]
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l[1:5]

print(range(*slice(None, None, -1).indices(10)))
# range(9, -1, -1)
print(list(range(*slice(None, None, -1).indices(10))))
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


