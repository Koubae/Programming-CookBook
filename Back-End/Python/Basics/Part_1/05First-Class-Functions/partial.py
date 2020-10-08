from functools import partial

def my_func(a, b, c):
    print(a, b, c)

f = partial(my_func, 10)
print(f)
# >>> functools.partial(<function my_func at 0x000002430BC97B80>, 10)
#print(f(20))
# ERROR TypeError: my_func() missing 1 required positional argument: 'c'
f(20, 30 )
# >>> 10 20 30
print(f(20, 30), 'Is None')
# >>> None Is None

def partial_func(b, c):
    return my_func(10, b, c)

print(partial_func(20, 30))

fn = lambda b, c: my_func(10, b, c)
(fn(20, 30))
# >>> 10, 20 , 30


def my_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

f = partial(my_func, 10, k1='a')
f(20, 30, 40, k2='b', k3='c')
# >>> 10 20 (30, 40) a b {'k3': 'c'}

def f(b, *args, k2, **kwargs):
    return my_func(10, b, *args, k1='a', k2=k2, **kwargs)
f(20, 30, 40, k2='b', k3='c')
# >>> 10 20 (30, 40) a b {'k3': 'c'}

def power(base, exponent):
    return base ** exponent

print(power(2, 3))
# >>> 8

square = partial(power, exponent=2)
print(square(4))
cube = partial(power, exponent=3)
print(cube(2))
print(cube(base=2))

# POINTS

origin = (0, 0)
l = [(1,1), (0, 2), (-3, 2), (0,0), (10, 10)]
dist2 = lambda x, y: (x[0]-y[0])**2 + (x[1]-y[1])**2
print(dist2((0,0), (1,1)))
print(dist2((1, 1), origin))


# Sort by the distance and not by element of the tuples
# Sorted key must be a function that takes a single paramenter (each element of the list)
print(sorted(l, key=lambda x: dist2((0,0), x)))
print(sorted(l, key=partial(dist2, (0,0))))

f = partial(dist2, origin)
print(f((1, 1)))
print(sorted(l, key=f))
f = lambda x: dist2(origin, x)
print(sorted(l, key=f))
print(lambda x: dist2(origin, x))