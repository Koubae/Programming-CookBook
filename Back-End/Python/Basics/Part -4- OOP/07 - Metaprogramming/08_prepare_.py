from collections import OrderedDict


class MyMeta(type):
    @staticmethod
    def __prepare__(name, bases, **kwargs):
        print('MyMeta.__prepare__ called...')
        print('\tname:', name)
        print('\tkwargs:', kwargs)
        return {'a': 100, 'b': 200}
    
    def __new__(mcls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('\tcls: ', mcls, type(mcls))
        print('\tname:', name, type(name))
        print('\tbases: ', bases, type(bases))
        print('\tcls_dict:', cls_dict, type(cls_dict))
        print('\tkwargs:', kwargs)
        return super().__new__(mcls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta, kw1=10, kw2=20):
    pass


class MyMeta(type):
    def __prepare__(name, bases, **kwargs):
        print(f'MyMeta.__prepare__ called... with {kwargs}')
        # we could create a new dictionary and insert everything we need from kwargs
        # or we could just use the kwargs dictionary directly
        kwargs['bonus_attr'] = 'Python rocks!'
        return kwargs
    
    def __new__(cls, name, bases, cls_dict, **kwargs):
        print('MyMeta.__new__ called...')
        print('\tcls: ', cls, type(cls))
        print('\tname:', name, type(name))
        print('\tbases: ', bases, type(bases))
        print('\tcls_dict:', cls_dict, type(cls_dict))
        print('\tkwargs:', kwargs)
        return super().__new__(cls, name, bases, cls_dict)


class MyClass(metaclass=MyMeta, kw1=1, kw2=2):
    pass


class MyMeta(type):
    def __prepare__(name, bases):
        d = OrderedDict()
        d['bonus'] = 'Python rocks!'
        return d

class MyClass(metaclass=MyMeta):
    pass

print(vars(MyClass))
# mappingproxy({'bonus': 'Python rocks!',
#               '__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'MyClass' objects>,
#               '__weakref__': <attribute '__weakref__' of 'MyClass' objects>,
#               '__doc__': None})



class CustomDict(dict):
    def __setitem__(self, key, value):
        print(f'Setting {key} = {value} in custom dictionary')
        super().__setitem__(key, value)
        
    def __getitem__(self, key):
        print(f'Getting {key} from custom dictionary')
        return int(super().__getitem__(key))


class MyMeta(type):
    def __prepare__(name, bases):
        return CustomDict()
    
    def __new__(mcls, name, bases, cls_dict):
        print('metaclass __new__ called...')
        print(f'\ttype(cls_dict) = {type(cls_dict)}')
        print(f'\tcls_dict={cls_dict}')


class MyClass(metaclass=MyMeta):
    pass


# Getting __name__ from custom dictionary
# Setting __module__ = __main__ in custom dictionary
# Setting __qualname__ = MyClass in custom dictionary
# metaclass __new__ called...
# 	type(cls_dict) = <class '__main__.CustomDict'>
# 	cls_dict={'__module__': '__main__', '__qualname__': 'MyClass'}