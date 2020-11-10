from functools import partial
from collections import defaultdict
from functools import wraps


def my_func(a, b, c):
    return a, b, c

class Partial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args
        
    def __call__(self, *args):
        return self._func(*self._args, *args)



partial_func = Partial(my_func, 10, 20)
print(partial_func(30))
#(10, 20, 30)
print(callable(partial_func)) # True

miss_counter = 0
def default_value():
    global miss_counter
    miss_counter += 1
    return 'N/A'


d = defaultdict(default_value)

d['a'] = 1
d['a']
d['b']
d['c']
print(miss_counter)
print(d)
# 2
# defaultdict(<function default_value at 0x000001BA82FB10D0>, {'a': 1, 'b': 'N/A', 'c': 'N/A'})


class DefaultValue:
    def __init__(self):
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return 'N/A'

def_1 = DefaultValue()
def_2 = DefaultValue()
cache_1 = defaultdict(def_1)
cache_2 = defaultdict(def_2)
print(cache_1['a'], cache_1['b'])
# ('N/A', 'N/A')
print(def_1.counter) # 2
print(cache_2['a']) # 'N/A'


class DefaultValue:
    def __init__(self, default_value):
        self.default_value = default_value
        self.counter = 0
        
    def __iadd__(self, other):
        if isinstance(other, int):
            self.counter += other
            return self
        raise ValueError('Can only increment with an integer value.')
        
    def __call__(self):
        self.counter += 1
        return self.default_value

cache_def_1 = DefaultValue(None)
cache_def_2 = DefaultValue(0)

cache_1 = defaultdict(cache_def_1)
cache_2 = defaultdict(cache_def_2)
print(cache_1['a'], cache_1['b'], cache_1['a'])
# (None, None, None)

def profiler(fn):
    _counter = 0
    _total_elapsed = 0
    _avg_time = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end - start)
        return result

    def counter():
        return _counter
    
    def avg_time():
        return _total_elapsed / _counter
    
    inner.counter = counter
    inner.avg_time = avg_time
    return inner

@profiler
def func1():
    sleep(random.random())

print(func1(), func1())
# (None, None)
func1.counter()
#2
func1.avg_time()
# 0.3425700559746474


# Class Coounter Decorator

class Profiler:
    def __init__(self, fn):
        self.counter = 0
        self.total_elapsed = 0
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        return result
        
    @property
    def avg_time(self):
        return self.total_elapsed / self.counter

@Profiler
def func_1(a, b):
    sleep(random.random())
    return (a, b)

func_1(1, 2)
# (1, 2)

print(func_1.counter)
#1

print(func_1(2, 3))
#(2, 3)

print(func_1.counter)
#2

print(func_1.avg_time)
#0.46242688701022416



@Profiler
def func_2():
    sleep(random.random())

print(func_2(), func_2(), func_2())

#(None, None, None)

print(func_2.counter, func_2.avg_time)

# (3, 0.5231811150054758)