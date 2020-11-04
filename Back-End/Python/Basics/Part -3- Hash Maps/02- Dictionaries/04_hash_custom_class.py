

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    __hash__ = None

# print(hash(Person('John', 78)))
# TypeError                                 Traceback (most recent call last)
# <ipython-input-32-31caaf6017f1> in <module>
# ----> 1 hash(Person('John', 78))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    def __hash__(self):
        print('__hash__ called...')
        return hash((self.name, self.age))


p1 = Person('John', 78)
p2 = Person('John', 78)
print(id(p1) is id(p2))
print(p1 == p2)
print(hash(p1) == hash(p2))

# False
# True
# __hash__ called...
# __hash__ called...
# True
p3 = Person('Eric', 75)
print(p1 == p3)
print(hash(p1) == hash(p3))
# False
# __hash__ called...
# __hash__ called...
# False


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def __eq__(self, other):
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        else:
            return False
    
    def __hash__(self):
        return 100



p1 = Person('John', 78)
p2 = Person('Eric', 75)

class Number:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.x == other.x
        else:
            return False
    
    def __hash__(self):
        return hash(self.x)

class SameHash:
    def __init__(self, x):
        self.x = x
        
    def __eq__(self, other):
        if isinstance(other, SameHash):
            return self.x == other.x
        else:
            return False
    
    def __hash__(self):
        return 100


numbers = {Number(i): 'some value' for i in range(1_000)}
same_hashes = {SameHash(i): 'some value' for i in range(1_000)}


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            other = Point(*other)
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __hash__(self):
        return hash((self.x, self.y))