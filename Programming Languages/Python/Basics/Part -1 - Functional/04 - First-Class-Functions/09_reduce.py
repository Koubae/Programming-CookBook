from functools import reduce

l = [5, 8, 6, 10, 9]
reduce(lambda a, b: a if a > b else b, l)
reduce(lambda a, b: a if a < b else b, l)
reduce(lambda a, b: a + b, l)

print(max(l), min(l), sum(l))

l = [0, 1, 2]
any(l)

l = [0, 0, 0]
any(l)

l = [0, 1, 2]
all(l)

l = [1, 2, 3]
all(l)

# any
l = [0, 1, 2]
print(reduce(lambda a, b: bool(a or b), l))

l = [0, 0, 0]
print(reduce(lambda a, b: bool(a or b), l))

# all
l = [0, 1, 2]
print(reduce(lambda a, b: bool(a and b), l))
l = [1, 2, 3]
print(reduce(lambda a, b: bool(a and b), l))

# Products
def mul(a, b):
    return a * b

l = [2, 3, 4]
print(reduce(mul, l))

print(reduce(lambda a, b: a * b, l))

# Factorials
# n! = 1 * 2 * 3 * ... * n
def fact(n):
    if n <=1:
        return 1
    else:
        result = 1
        for i in range(2, n+1):
            result *= i
        return result


print(fact(1), fact(2), fact(3), fact(4), fact(5))
# >>> 1 2 6 24 120

# RECURSIVE
def fact(n):
    if n <=1:
        return 1
    else:
        return n * fact(n-1)

print(fact(1), fact(2), fact(3), fact(4), fact(5))
# >>> (1, 2, 6, 24, 120)


n = 5
reduce(lambda a, b: a * b, range(1, n+1))
# >>> 120

# reduce initializer
l = [1, 2, 3]
print(reduce(lambda x, y: x*y, l))

l = []
print(reduce(lambda x, y: x*y, l, 1))
