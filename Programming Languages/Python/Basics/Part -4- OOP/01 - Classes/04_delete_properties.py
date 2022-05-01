class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('getting name property value...')
        return self._name
    
    @name.setter
    def name(self, value):
        """Person name"""
        print(f'setting name property to {value}...')
        self._name = value
    
    @name.deleter
    def name(self):
        # delete the underlying data
        print('deleting name property value...')
        del self._name


p = Person('Alex')
print(p.name)
del p.name # Doesn't delete the property from the Class