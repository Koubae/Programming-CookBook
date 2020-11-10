class Location:
    __slots__ = 'name', '_longitude', '_latitude'
    
    def __init__(self, name, longitude, latitude):
        self._longitude = longitude
        self._latitude = latitude
        self.name = name
        
    @property
    def longitude(self):
        return self._longitude
    
    @property
    def latitude(self):
        return self._latitude

print(Location.__dict__)
# {'__module__': '__main__', '__slots__': ('name', '_longitude', '_latitude'), '__init__': <function Location.__init__ at 0x00000237D7A39B80>, 'longitude': <property object at 0x00000237D7A36DB0>, 'latitude': <property object at 0x00000237D7A3F590>, 
# '_latitude': <member '_latitude' of 'Location' objects>, '_longitude': <member '_longitude' of 'Location' objects>, 'name': 
# <member 'name' of 'Location' objects>, '__doc__': None}

Location.map_service = 'Google Maps'
l = Location('Mumbai',longitude= 19.0760, latitude=72.8777)
print(l.name, l.longitude, l.latitude)

# ('Mumbai', 19.076, 72.8777)

try:
    l.__dict__
except AttributeError as ex:
    print(ex)
# 'Location' object has no attribute '__dict__'

try:
    l.map_link = 'http://maps.google.com/...'
except AttributeError as ex:
    print(ex)
# 'Location' object has no attribute 'map_link'



del l.name

try:
    print(l.name)
except AttributeError as ex:
    print(f'Attribute Error: {ex}')
# Attribute Error: name
l.name = 'Mumbai'

print(l.name)

# 'Mumbai'

class Person:
    def __init__(self, name):
        self.name = name
        
class Student(Person):
    __slots__ = 'age', 
    
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

s = Student('Python', 30)
print(s.name, s.age, s.__dict__)
# ('Python', 30, {'name': 'Python'})


class Person:
    __slots__ = '_name', 'age'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

p = Person('Eric', 78)
print(p.name, p.age)
#('Eric', 78)
try:
    print(p.__dict__)
except AttributeError as ex:
    print(ex)
# 'Person' object has no attribute '__dict__'
hasattr(Person.name, '__get__'), hasattr(Person.name, '__set__')
#(True, True)
hasattr(Person.age, '__get__'), hasattr(Person.age, '__set__')
#(True, True)


class Person:
    __slots__ = 'name', '__dict__'
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person('Alex', 19)

print(p.name, p.age, p.__dict__)