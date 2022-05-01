import numbers


class Int:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError(f'{self.prop_name} must be an integer.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Float:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, float):
            raise ValueError(f'{self.prop_name} must be a float.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, value):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)



class List:
    def __set_name__(self, owner_class, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, list):
            raise ValueError(f'{self.prop_name} must be a list.')
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, value):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Person:
    age = Int()
    height = Float()
    tags = List()
    favorite_foods = List()


p = Person()

try:
    p.age = 12.5
except ValueError as ex:
    print(ex)
# age must be an integer.

try:
    p.height = 'abc'
except ValueError as ex:
    print(ex)
# height must be a float.

try:
    p.tags = 'python'
except ValueError as ex:
    print(ex)
# tags must be a list.


class ValidType:
    def __init__(self, type_):
        self._type = type_
        
    def __set_name__(self, owner_clasds, prop_name):
        self.prop_name = prop_name
        
    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise ValueError(f'{self.prop_name} must be of type '
                            f'{self._type.__name__}'
                            )
        instance.__dict__[self.prop_name] = value
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            return instance.__dict__.get(self.prop_name, None)


class Person:
    age = ValidType(int)
    height = ValidType(float)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

p = Person()

try:
    p.age = 10.5
except ValueError as ex:
    print(ex)
# age must be of type int

try:
    p.height = 10
except ValueError as ex:
    print(ex)
# height must be of type float
isinstance(10.1, numbers.Real)
# True

isinstance(10, numbers.Real)
# True


class Person:
    age = ValidType(int)
    height = ValidType(numbers.Real)
    tags = ValidType(list)
    favorite_foods = ValidType(tuple)
    name = ValidType(str)

p = Person()

p.height = 10
p.height
# 10