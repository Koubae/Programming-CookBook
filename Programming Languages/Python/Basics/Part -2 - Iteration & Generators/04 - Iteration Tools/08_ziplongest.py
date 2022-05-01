from itertools import zip_longest



l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 3, 4]
l3 = [1, 2, 3]

print(list(zip_longest(l1, l2, l3, fillvalue='N/A')))
# [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 'N/A'), (5, 'N/A', 'N/A')]



def squares():
    i = 0
    while True:
        yield i ** 2
        i += 1

def cubes():
    i = 0
    while True:
        yield i ** 3
        i += 1


iter1 = squares()
iter2 = cubes()
print(list(zip(range(10), iter1, iter2)))

# [(0, 0, 0),
#  (1, 1, 1),
#  (2, 4, 8),
#  (3, 9, 27),
#  (4, 16, 64),
#  (5, 25, 125),
#  (6, 36, 216),
#  (7, 49, 343),
#  (8, 64, 512),
#  (9, 81, 729)]