
print(lambda x : x**2)
# >>> <function <lambda> at 0x00000263AC007B80>
# <class 'function'>
x = lambda: 'Hello world'
print(x())
print(list(x()))
# Hello world
# ['H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

func_1 = lambda x, y=10: (x, y)
print(func_1(1, 2))
# (1, 2)

func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})
func_2(1, 'a', 'b', y=100, a=10, b=20)
# (1, 'a', 'b', 100, {'a': 10, 'b': 20})


def apply_func(x, fn):
    return fn(x)

y = apply_func(3, lambda x: x**3)
print(y)  # --> 27


def apply_func_2(fn, *args, **kwargs):
    return fn(*args, **kwargs)

z = apply_func_2(lambda x, y: x + y, 1, 2)
print(z) # ---> 3

a = apply_func_2(lambda x, *, y: x+y, 1, y=2)
print(a) # --> 3

b = apply_func_2(lambda *args: sum(args), 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(b) # --> 55


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
print(f(1)) # --> 43

# same as
s = lambda x: x + 42
print(s(1))