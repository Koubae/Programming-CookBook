from functools import wraps


def debugger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        print(f'{fn.__qualname__}', args, kwargs)
        return fn(*args, **kwargs)
    return inner


@debugger
def func_1(*args, **kwargs):
    pass


@debugger
def func_2(*args, **kwargs):
    pass


func_1(10, 20, kw='a')
# func_1 (10, 20) {'kw': 'a'}
func_2(10)
# func_2 (10,) {}