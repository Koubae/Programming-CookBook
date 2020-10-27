import math

def my_func():
    print('line 1')
    yield 'Flying'
    print('line 2')
    yield 'Circus'

gen_my_func = my_func()
print(next(gen_my_func))
print(next(gen_my_func))
# print(next(gen_my_func))
# StopIteration
# line 1
# Flying
# line 2
# Circus

def squares(sentinel):
    i = 0
    while True:
        if i < sentinel:
            result = i**2
            i += 1
            yield result
        else:
            return 'all done'
sq = squares(3)
print(next(sq))
print(next(sq))
print(next(sq))
# print(next(sq))
# 0
# 1
# 4
# StopIteration: all done

def squares(sentinel):
    i = 0
    while True:
        if i < sentinel:
            yield i**2
            i += 1 # note how we can incremenet **after** the yield
        else:
            return 'all done!'

for num in squares(5):
    print(num)



def factorials(n):
    for i in range(n):
        yield math.factorial(i)

for num in factorials(5):
    print(num)