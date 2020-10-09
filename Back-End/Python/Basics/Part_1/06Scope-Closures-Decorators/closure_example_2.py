def counter(initial_value):
    # Initial value is a Local Variable
    def inc(increment=1):
        nonlocal initial_value
        # initial_value is a nonlocal (captured) variable here
        initial_value += increment
        return initial_value
    return inc

counter1 = counter(0)

print(counter1(0))
print(counter1(8))
counter2 = counter(1000)
print(counter2(1))
print(counter2())
print(counter2(220))
print(counter2())
# 0
# 8
# 1001
# 1002
# 1222
# 1223

# 2
def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

counted_add = counter(add)
print(counted_add.__code__.co_freevars)
# ('cnt', 'fn')
counted_add(1, 2)
counted_add(2, 3)
# add has been called 1 times
# add has been called 2 times

def mult(a, b, c):
    return a * b * c

counted_mult = counter(mult)
counted_mult(1, 2, 3)
counted_mult(2, 3, 4)
# mult has been called 1 times
# mult has been called 2 times


# 3

counters = dict()


def counter(fn):

    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt # --> is Global
        return fn(*args, **kwargs)
    return inner

counted_add = counter(add)
counted_mult = counter(mult)
counted_add.__code__.co_freevars

counted_add(1, 2)
counted_add(2, 3)
counted_mult(1, 2, 'a')
counted_mult(2, 3, 'b')
counted_mult(1, 1, 'abc')
print(counters)


def counter(fn, counters):
    cnt = 0

    def inner(*args, **kwargs):
        nonlocal cnt
        cnt = cnt + 1
        counters[fn.__name__] = cnt # --> None Local
        return fn(*args, **kwargs)
    return inner

func_counters = dict()
counted_add = counter(add, func_counters)
counted_mult = counter(mult, func_counters)
counted_add.__code__.co_freevars

for i in range(5):
    counted_add(i, i)

for i in range(10):
    counted_mult(i, i, i)
print(func_counters)


def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
        return product

fact = counter(fact, func_counters)
print(fact(0))
print(fact(3))
print(fact(4))