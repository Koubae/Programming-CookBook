def fact(n):
    return 1 if n < 2 else n * fact(n-1)

l = [1, 2, 3, 4, 5]

result = [fact(i) for i in l]
print(result)
# >>>> [1, 2, 6, 24, 120]

l1 = 1, 2, 3
l2 = 'a', 'b', 'c'
list(zip(l1, l2))
# [(1, 'a'), (2, 'b'), (3, 'c')]
l1 = 1, 2, 3
l2 = [10, 20, 30]
l3 = ('a', 'b', 'c')
list(zip(l1, l2, l3))
# >>> [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]
l1 = [1, 2, 3]
l2 = (10, 20, 30)
l3 = 'abc'
list(zip(l1, l2, l3))
# >>> [(1, 10, 'a'), (2, 20, 'b'), (3, 30, 'c')]
l1 = range(100)
l2 = 'python'
list(zip(l1, l2))
# [(0, 'p'), (1, 'y'), (2, 't'), (3, 'h'), (4, 'o'), (5, 'n')]
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i, j in zip(l1, l2)]
print(result)
# >>> [11, 22, 33, 44, 55]

# Filtering using a comprehension

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = [i for i in l if i % 2 == 0]
print(result)
# >>> [2, 4, 6, 8]

# Compining map and filter
print(list(map(lambda x: x**2, range(10))))
print(list(filter(lambda y: y < 25, map(lambda x: x**2, range(10)))))
print([x**2 for x in range(10) if x**2 <25])
# >>> [0, 1, 4, 9, 16]