class Person:
    def __getattr__(self, name):
        alt_name = '_' + name
        print(f'Could not find {name}, trying {alt_name}...')
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')


p = Person()
try:
    p.age
except AttributeError as ex:
    print(type(ex).__name__, ex)
# Could not find age, trying _age...
# AttributeError Could not find age or _age

class Person:
    def __init__(self, age):
        self._age = age
        
    def __getattr__(self, name):
        print(f'Could not find {name}')
        alt_name = '_' + name
        try:
            return super().__getattribute__(alt_name)
        except AttributeError:
            raise AttributeError(f'Could not find {name} or {alt_name}')


p = Person(100)
p.age
# Could not find age
# 100

# Example 1

class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
        
    def __getattr__(self, name):
        print(f'{name} not found. creating it and setting it to default...')
        setattr(self, name, self._attribute_default)
        return self._attribute_default


d = DefaultClass('NotAvailable')
d.test
# test not found. creating it and setting it to default...
# 'NotAvailable'
d.__dict__
# {'_attribute_default': 'NotAvailable', 'test': 'NotAvailable'}
d.test
# 'NotAvailable'
d.test = 'hello'
d.test
# 'hello'
d.__dict__
# {'_attribute_default': 'NotAvailable', 'test': 'hello'}

class Person(DefaultClass):
    def __init__(self, name):
        super().__init__('Unavailable')
        self.name = name


p = Person('Raymond')
p.name
# 'Raymond'
p.age
# age not found. creating it and setting it to default...

# Example 2

class AttributeNotFoundLogger:
    def __getattr__(self, name):
        err_msg = f"'{type(self).__name__}' object has no attribute '{name}'"
        print(f'Log: {err_msg}')
        raise AttributeError(err_msg)


class Person(AttributeNotFoundLogger):
    def __init__(self, name):
        self.name = name


p = Person('Raymond')
p.name
# 'Raymond'

try:
    p.age
except AttributeError as ex:
    print(f'AttributeError raised: {ex}')
# Log: 'Person' object has no attribute 'age'
# AttributeError raised: 'Person' object has no attribute 'age'

# Example 3: Overriding __getattribute__

class DefaultClass:
    def __init__(self, attribute_default=None):
        self._attribute_default = attribute_default
        
    def __getattr__(self, name):
        print(f'{name} not found. creating it and setting it to default...')
        default_value = super().__getattribute__('_attribute_default')
        setattr(self, name, default_value)
        return default_value


class Person(DefaultClass):
    def __init__(self, name=None, age=None):
        super().__init__('Not Available')
        if name is not None:
            self._name = name
        if age is not None:
            self._age = age
        
    def __getattribute__(self, name):
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError(f'Forbidden access to {name}')
        return super().__getattribute__(name)
    
    @property
    def name(self):
        return super().__getattribute__('_name')
    
    @property
    def age(self):
        return super().__getattribute__('_age')


p = Person('Python', 42)

p.name, p.age
# ('Python', 42)

p.language
# language not found. creating it and setting it to default...
# 'Not Available'

p.__dict__
# {'_attribute_default': 'Not Available',
#  '_name': 'Python',
#  '_age': 42,
#  'language': 'Not Available'}

# Overriding Class Attribute Accessors

class MetaLogger(type):
    def __getattribute__(self, name):
        print('class __getattribute__ called...')
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print('class __getattr__ called...')
        return 'Not Found'


class Account(metaclass=MetaLogger):
    apr = 10


Account.apr
# class __getattribute__ called...
# 10
Account.apy
# class __getattribute__ called...
# class __getattr__ called...
# # 'Not Found'

# Gets called for Method access


class MyClass:
    def __getattribute__(self, name):
        print(f'__getattribute__ called... for {name}')
        return super().__getattribute__(name)
    
    def __getattr__(self, name):
        print(f'__getattr__ called... for {name}')
        raise AttributeError(f'{name} not found')
    
    def say_hello(self):
        return 'hello'


m = MyClass()
m.say_hello()
# __getattribute__ called... for say_hello
# 'hello'