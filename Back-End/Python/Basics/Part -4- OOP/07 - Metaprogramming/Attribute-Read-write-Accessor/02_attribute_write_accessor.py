class MyMeta(type):
    def __setattr__(self, name, value):
        print('setting class attribute...')
        return super().__setattr__(name, value)
    
class Person(metaclass=MyMeta):
    def __setattr__(self, name, value):
        print('setting instance attribute...')
        super().__setattr__(name, value)


Person.test = 'test'
# setting class attribute...
p = Person()
p.test = 'test'
# setting instance attribute...


class MyNonDataDesc:
    def __get__(self, instance, owner_class):
        print('__get__ called on non-data descriptor...')
        
class MyDataDesc:
    def __set__(self, instance, value):
        print('__set__ called on data descriptor...')
        
    def __get__(self, instance, owner_class):
        print('__get__ called on data descriptor...')


class MyClass:
    non_data_desc = MyNonDataDesc()
    data_desc = MyDataDesc()
    
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        super().__setattr__(name, value)


m = MyClass()
m.__dict__
# {}
m.data_desc = 100
# __setattr__ called...
# __set__ called on data descriptor...
m.non_data_desc = 200
# __setattr__ called...
m.__dict__
# {'non_data_desc': 200}


class MyClass:
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError('Sorry, this attribute is read-only.')
        super().__setattr__(name, value)


m = MyClass()
In [21]:
# __setattr__ called...
m.__dict__
# {'test': 'test'}



class MyClass:
    def __setattr__(self, name, value):
        print('__setattr__ called...')
        if name.startswith('_') and not name.startswith('__'):
            raise AttributeError('Sorry, this attribute is read-only.')
        setattr(self, name, value)


m = MyClass()

try:
    m._test = 'test'
except AttributeError as ex:
    print(ex)
# __setattr__ called...
# Sorry, this attribute is read-only.

# try:
#     m.test = 'test'
# except RecursionError as ex:
#     print(ex)