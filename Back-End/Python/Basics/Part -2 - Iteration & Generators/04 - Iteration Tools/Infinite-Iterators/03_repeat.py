from itertools import repeat

g = repeat('Python')
for _ in range(5):
    print(next(g))

g = repeat('Python', 4)
print(list(g))
# Python
# Python
# Python
# Python
# Python
# ['Python', 'Python', 'Python', 'Python']


l = [1, 2, 3]
result = list(repeat(l, 3))
print(result)
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
print(l is result[0], l is result[1], l is result[2])
# True True True



l = [1, 2, 3]
result = [item[:] for item in repeat(l, 3)]


print(l is result[0], l is result[1], l is result[2])
# False False False

