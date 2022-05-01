
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
            
    def __hash__(self):
        return hash(self.name)


p1 = Person('Eric')

d = {p1: 'Eric'}

print(d)
#{<__main__.Person at 0x7fc3d838f0f0>: 'Eric'}
s = {p1}
print(s)