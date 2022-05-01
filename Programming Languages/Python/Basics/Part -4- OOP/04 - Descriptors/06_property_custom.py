
from numbers import Integral    


class Person:
    @property
    def age(self):
        return getattr(self, '_age', None)
    
    @age.setter
    def age(self, value):
        if not isinstance(value, Integral):
            raise ValueError('age: must be an integer.')
        if value < 0:
            raise ValueError('age: must be a non-negative integer.')
        self._age = value


    
class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable.')
        return self.fget(instance)
            
    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable.')
        self.fset(instance, value)


class Person:
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        self._name = value
        
    name = MakeProperty(fget=get_name, fset=set_name)



class MakeProperty:
    def __init__(self, fget=None, fset=None):
        self.fget = fget
        self.fset = fset
        
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __get__(self, instance, owner_class):
        print('__get__ called...')
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError(f'{self.prop_name} is not readable.')
        return self.fget(instance)
            
    def __set__(self, instance, value):
        print('__set__ called...')
        if self.fset is None:
            raise AttributeError(f'{self.prop_name} is not writable.')
        self.fset(instance, value)
        
    def setter(self, fset):
        self.fset = fset
        return self
    
    class Person:
    def get_first_name(self):
        return getattr(self, '_first_name', None)
    
    def set_first_name(self, value):
        self._first_name = value
        
    def get_last_name(self):
        return getattr(self, '_last_name', None)
    
    def set_last_name(self, value):
        self._last_name = value
        
    first_name = MakeProperty(fget=get_first_name, fset=set_first_name)
    last_name = MakeProperty(fget=get_last_name, fset=set_last_name)


class Person:
    @MakeProperty
    def first_name(self):
        return getattr(self, '_first_name', None)
    
    @first_name.setter
    def first_name(self, value):
        self._first_name = value
        
    @MakeProperty
    def last_name(self):
        return getattr(self, '_last_name', None)
    
    @last_name.setter
    def last_name(self, value):
        self._last_name = value