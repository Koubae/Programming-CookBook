from functools import wraps
from types import MethodType

def logger(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        print(f'Log: {fn.__name__} called.')
        return fn(*args, **kwargs)
    return wrapped

@logger
def say_hello():
    pass

print(say_hello())
# Log: say_hello called.


class Logger:
    def __init__(self, fn):
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        print(f'Log: {self.fn.__name__} called.')
        return self.fn(*args, **kwargs)
    
    def __get__(self, instance, owner_class):
        print(f'__get__ called: self={self}, instance={instance}')
        if instance is None:
            print('\treturning self unbound...')
            return self
        else:
            # self is callable, since it implements __call__
            print('\treturning self as a method bound to instance')
            return MethodType(self, instance)


class Person:
    def __init__(self, name):
        self.name = name
        
    @Logger
    def say_hello(self):
        return f'{self.name} says hello!'

p = Person('David')
print(p.say_hello)
# __get__ called: self=<__main__.Logger object at 0x7facc02c8610>, instance=<__main__.Person object at 0x7facc02c8750>
# 	returning self as a method bound to instance
# <bound method ? of <__main__.Person object at 0x7facc02c8750>>

print(p.say_hello())
# __get__ called: self=<__main__.Logger object at 0x7facc02c8610>, instance=<__main__.Person object at 0x7facc02c8750>
# 	returning self as a method bound to instance
# Log: say_hello called.
# 'David says hello!'

@Logger
def say_bye():
    pass

print(say_bye)
# <__main__.Logger at 0x7face0d1e850>

class Person:
    @classmethod
    @Logger
    def cls_method(cls):
        print('class method called...')
        
    @staticmethod
    @Logger
    def static_method():
        print('static method called...')

Person.cls_method()
# Log: cls_method called.
# class method called...

Person.static_method()
# Log: static_method called.
# static method called...