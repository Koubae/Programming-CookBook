class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        
    def __repr__(self):
        return f'Person(name={self._name}, age={self._age})'
    
    @property
    def name(self):
        return self._name
        
    @property
    def age(self):
        return self._age
    
    def key(self):
        return frozenset({self.name, self.age})


p1 = Person('John', 78)
p2 = Person('Eric', 75)

d = {p1.key(): p1, p2.key(): p2
print(d)
# {frozenset({78, 'John'}): Person(name=John, age=78),
#  frozenset({75, 'Eric'}): Person(name=Eric, age=75)}

# Lookup
print(d[frozenset({'John', 78})])
# Person(name=John, age=78)
print(d[frozenset({78, 'John'})])
# Person(name=John, age=78)