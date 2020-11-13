
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = object.__new__(Point)
p.__init__(10, 20)
print(p.__dict__)
# {'x': 10, 'y': 20}
print(p)
# <__main__.Point object at 0x000002356DBA7880>


class Point:
    def __new__(cls, x, y):
        print('Creating instance...', x, y)
        instance = object.__new__(cls)  # delegate to object.__new__
        return instance  # don't forget to return the new instance!
    
    def __init__(self, x, y):
        print('Initializing instance...', x, y)
        self.x = x
        self.y = y

p = Point(10, 20)
# Creating instance... 10 20
# Initializing instance... 10 20


class Squared(int):
    def __new__(cls, x):
        return super().__new__(cls, x**2)  # delegate creating an int instance to the int class itself

result = Squared(4)
result
# 16
print(type(result))
# __main__.Squared
isinstance(result, int)
# True


class Person:
    def __new__(cls, name):
        print(f'Person: Instantiating {cls.__name__}...')
        instance = super().__new__(cls)
        return instance
        
    def __init__(self, name):
        print(f'Person: Initializing instance...')
        self.name = name
        

class Student(Person):
    def __new__(cls, name, major):
        print(f'Student: Instantiating {cls.__name__}...')
        instance = super().__new__(cls, name)
        return instance
    
    def __init__(self, name, major):
        print(f'Student: Initializing instance...')
        super().__init__(name)
        self.major = major


s = Student('John', 'Major')
# Student: Instantiating Student...
# Person: Instantiating Student...
# Student: Initializing instance...
# Person: Initializing instance...


class Square:
    def __new__(cls, w, l):
        cls.area = lambda self: self.w * self.l
        # or use setattr(cls, 'area', lambda self: self.w * self.l)
        instance = super().__new__(cls)  
        return instance
    
    def __init__(self, w, l):
        self.w = w
        self.l = l