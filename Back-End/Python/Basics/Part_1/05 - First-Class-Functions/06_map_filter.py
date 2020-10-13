def fact(n):
    return 1 if n < 2 else n * fact(n -1)

print(fact(3))
print(list(map(fact, [1,2,3,4,5])))
# [1, 2, 6, 24, 120]

# Alternative

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x + y
m = map(f, l1, l2)
print(list(m))
# >>> [11, 22, 33, 44, 55]

l = [0, 1, 2, 3, 4, 5, 6]
for e in filter(None, l):
    print(e)

def is_even(n):
    return n % 2 == 0

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(is_even, l)
print(list(result))

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))