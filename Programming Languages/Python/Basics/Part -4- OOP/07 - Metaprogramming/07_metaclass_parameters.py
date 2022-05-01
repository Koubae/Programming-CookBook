class Metaclass(type):
    def __new__(mcls, name, bases, cls_dict):
        return super().__new__(mcls, name, bases, cls_dict)
    

    
class MyClass(metaclass=Metaclass):
    pass


type(MyClass), type(MyClass())
# (__main__.Metaclass, __main__.MyClass)



class Metaclass(type):
    def __new__(mcls, name, bases, cls_dict, arg1, arg2, arg3=None):
        print(arg1, arg2, arg3)
        return super().__new__(mcls, name, bases, cls_dict)


class MyClass(metaclass=Metaclass, arg1=10, arg2=20, arg3=30):
    pass
# 10 20 30


class MyClass(metaclass=Metaclass, arg1=10, arg2=20):
    pass
# 10 20 None


class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, extra_attrs=None):
        if extra_attrs:
            print('Creating class with some extra attributes: ', extra_attrs)
            # here I'm going to things directly into the cls_dict namespace
            # but could also create the class first, then add using setattr
            for attr_name, attr_value in extra_attrs:
                cls_dict[attr_name] = attr_value
        return super().__new__(cls, name, bases, cls_dict)


class Account(metaclass=AutoClassAttrib, extra_attrs=[('account_type', 'Savings'), ('apr', 0.5)]):
    pass
# Creating class with some extra attributes:  [('account_type', 'Savings'), ('apr', 0.5)]

vars(Account)
# mappingproxy({'__module__': '__main__',
#               'account_type': 'Savings',
#               'apr': 0.5,
#               '__dict__': <attribute '__dict__' of 'Account' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Account' objects>,
#               '__doc__': None})


class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, extra_attrs=None):
        new_cls = super().__new__(cls, name, bases, cls_dict)
        if extra_attrs:
            print('Creating class with some extra attributes: ', extra_attrs)
            for attr_name, attr_value in extra_attrs:
                setattr(new_cls, attr_name, attr_value)
        return new_cls


class Account(metaclass=AutoClassAttrib, extra_attrs=[('account_type', 'Savings'), ('apr', 0.5)]):
    pass
# Creating class with some extra attributes:  [('account_type', 'Savings'), ('apr', 0.5)]


vars(Account)
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'Account' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Account' objects>,
#               '__doc__': None,
#               'account_type': 'Savings',
#               'apr': 0.5})

class AutoClassAttrib(type):
    def __new__(cls, name, bases, cls_dict, **kwargs):
        new_cls = super().__new__(cls, name, bases, cls_dict)
        if kwargs:
            print('Creating class with some extra attributes: ', kwargs)
            for attr_name, attr_value in kwargs.items():
                setattr(new_cls, attr_name, attr_value)
        return new_cls


class Account(metaclass=AutoClassAttrib, account_type='Savings', apr=0.5):
    pass

# Creating class with some extra attributes:  {'account_type': 'Savings', 'apr': 0.5}


print(vars(Account))
# mappingproxy({'__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'Account' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Account' objects>,
#               '__doc__': None,
#               'account_type': 'Savings',
#               'apr': 0.5})