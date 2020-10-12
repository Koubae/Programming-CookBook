from functools import wraps
from datetime import datetime, timezone
from time import perf_counter
from operator import mul
from functools import reduce


def logged(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print(f'{fn.__name__}: called {run_dt}')
        return result
    return inner

def logged_2(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now()
        result = fn(*args, **kwargs)
        print(f'{fn.__name__}: called {run_dt:%Y-%m-%d %H:%M}')
        return result
    return inner


@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()
# func_1: called 2020-10-12 03:13:43.274212+00:00
func_2()
# func_2: called 2020-10-12 03:13:43.274212+00:00


# Timed Function
def timed(fn):

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print(f'{fn.__name__} run for {end-start:6f}')
        return result
    return inner

@timed
@logged_2
def factorial(n):

    return reduce(mul, range(1, n+1))

print(factorial(10))


# Debug Decorator
def debug(fn):
    """Print the function signature and return value"""
    @wraps(fn)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f'{k}={v!r}' for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        print(f'Calling {fn.__name__}({signature})')
        value = fn(*args, **kwargs)
        print(f'{fn.__name__!r} returned {value!r}')
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

make_greeting("Richard", age=112)

#  create a wrapper which lets us specify a logfile to output to

from functools import wraps

def logit(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            # Open the logfile and append
            with open(logfile, 'a') as opened_file:
                # Now we log to the specified logfile
                opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()
# Output: myfunc1 was called
# A file called out.log now exists, with the above string

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()
# Output: myfunc2 was called
# A file called func2.log now exists, with the above string


class logit(object):

    _logfile = 'out.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        # Open the logfile and append
        with open(self._logfile, 'a') as opened_file:
            # Now we log to the specified logfile
            opened_file.write(log_string + '\n')
        # Now, send a notification
        self.notify()

        # return base func
        return self.func(*args)



    def notify(self):
        # logit only logs, no more
        pass