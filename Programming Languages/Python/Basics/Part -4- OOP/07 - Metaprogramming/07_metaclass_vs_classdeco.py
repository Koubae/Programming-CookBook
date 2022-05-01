
from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner    

def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls


@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'


Person('Alex', 10).greet()


class ClassLogger(type):
    def __new__(mcls, name, bases, class_dict):
        new_cls = super().__new__(mcls, name, bases, class_dict)
        for key, obj in vars(new_cls).items():
            if callable(obj):
                setattr(new_cls, key, func_logger(obj))
        return new_cls


class Person(metaclass=ClassLogger):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'


p = Person('John', 78).greet()
# log: Person.__init__((<__main__.Person object at 0x7f9be0ce18d0>, 'John', 78), {}) = None
# log: Person.greet((<__main__.Person object at 0x7f9be0ce18d0>,), {}) = Hello, my name is John and I am 78


@class_logger
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'