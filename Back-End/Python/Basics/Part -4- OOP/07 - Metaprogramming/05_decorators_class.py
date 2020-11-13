def savings(cls):
    cls.account_type = 'savings'
    return cls
    
def checking(cls):
    cls.account_type = 'checking'
    return cls

class Account:
    pass

@savings
class Bank1Savings(Account):
    pass

@savings
class Bank2Savings(Account):
    pass

@checking
class Bank1Checking(Account):
    pass

@checking
class Bank2Checking(Account):
    pass



def account_type(type_):
    def decorator(cls):
        cls.account_type = type_
        return cls
    return decorator


@account_type('Savings')
class Bank1Savings:
    pass

@account_type('Checking')
class Bank1Checking:
    pass



from functools import wraps

def func_logger(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        result = fn(*args, **kwargs)
        print(f'log: {fn.__qualname__}({args}, {kwargs}) = {result}')
        return result
    return inner


class Person:
    @func_logger
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @func_logger
    def greet(self):
        return f'Hello, my name is {self.name} and I am {self.age}'



p = Person('John', 78)



def class_logger(cls):
    for name, obj in vars(cls).items():
        if callable(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
        elif isinstance(obj, staticmethod):
            original_func = obj.__func__
            print('decorating static method', original_func)
            decorated_func = func_logger(original_func)
            method = staticmethod(decorated_func)
            print(method, type(method))
            setattr(cls, name, method)
        elif isinstance(obj, classmethod):
            original_func = obj.__func__
            print('decorating class method', original_func)
            decorated_func = func_logger(original_func)
            method = classmethod(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            if obj.fget:
                obj = obj.getter(func_logger(obj.fget))
            if obj.fset:
                obj = obj.setter(func_logger(obj.fset))
            if obj.fdel:
                obj = obj.deleter(func_logger(obj.fdel))
            setattr(cls, name, obj)
    return cls



import inspect

class MyClass:
    @staticmethod
    def static_method():
        pass
    
    @classmethod
    def cls_method(cls):
        pass
    
    def inst_method(self):
        pass
    
    @property
    def name(self):
        pass
    
    def __add__(self, other):
        pass
    
    class Other:
        def __call__(self):
            pass
        
    other = Other()


keys = ('static_method', 'cls_method', 'inst_method', 'name', '__add__', 'Other', 'other')
# inspect_funcs = ('isroutine', 'ismethod', 'isfunction', 'isbuiltin', 'ismethoddescriptor')

print(keys)
# ('static_method', 'cls_method', 'inst_method', 'name', '__add__', 'Other', 'other')

max_header_length = max(len(key) for key in keys)
max_fname_length = max(len(func) for func in inspect_funcs)

print(format('', f'{max_fname_length}s'), '\t'.join(format(key, f'{max_header_length}s') for key in keys))

for inspect_func in inspect_funcs:
    fn = getattr(inspect, inspect_func)
    inspect_results = (format(str(fn(MyClass.__dict__[key])), f'{max_header_length}s') for key in keys)
    print(format(inspect_func, f'{max_fname_length}s'), '\t'.join(inspect_results))


#                    static_method	cls_method   	inst_method  	name         	__add__      	Other        	other        
# isroutine          True         	True         	True         	False        	True         	False        	False        
# ismethod           False        	False        	False        	False        	False        	False        	False        
# isfunction         False        	False        	True         	False        	True         	False        	False        
# isbuiltin          False        	False        	False        	False        	False        	False        	False        
# ismethoddescriptor True         	True         	False        	False        	False        	False        	False        



import inspect

def class_logger(cls):
    for name, obj in vars(cls).items():
        if isinstance(obj, staticmethod) or isinstance(obj, classmethod):
            type_ = type(obj)
            original_func = obj.__func__
            print(f'decorating {type_.__name__} method', original_func)
            decorated_func = func_logger(original_func)
            method = type_(decorated_func)
            setattr(cls, name, method)
        elif isinstance(obj, property):
            print('decorating property', obj)
            methods = (('fget', 'getter'), ('fset', 'setter'), ('fdel', 'deleter'))
            for prop, method in methods:
                if getattr(obj, prop):
                    obj = getattr(obj, method)(func_logger(getattr(obj, prop)))
            setattr(cls, name, obj)
        elif inspect.isroutine(obj):
            print('decorating:', cls, name)
            setattr(cls, name, func_logger(obj))
    return cls


@class_logger
class MyClass:
    @staticmethod
    def static_method():
        print('static_method called...')
    
    @classmethod
    def cls_method(cls):
        print('class method called...')
    
    def inst_method(self):
        print('instance method called...')
    
    @property
    def name(self):
        print('name getter called...')
        
    @name.setter
    def name(self, value):
        print('name setter called...')
        
    @name.deleter
    def name(self):
        print('name deleter called...')
    
    def __add__(self, other):
        print('__add__ called...')
    
    @class_logger
    class Other:
        def __call__(self):
            print(f'{self}.__call__ called...')
        
    other = Other()


# decorating: <class '__main__.MyClass.Other'> __call__
# decorating staticmethod method <function MyClass.static_method at 0x7fad8914a170>
# decorating classmethod method <function MyClass.cls_method at 0x7fad8914a3b0>
# decorating: <class '__main__.MyClass'> inst_method
# decorating property <property object at 0x7fad682be950>
# decorating: <class '__main__.MyClass'> __add__
MyClass().name
# name getter called...
# log: MyClass.name((<__main__.MyClass object at 0x7fad98076fd0>,), {}) = None


MyClass().name = 'David'
# name setter called...
# log: MyClass.name((<__main__.MyClass object at 0x7fad980764d0>, 'David'), {}) = None
del MyClass().name
# name deleter called...
# log: MyClass.name((<__main__.MyClass object at 0x7fad98076410>,), {}) = None