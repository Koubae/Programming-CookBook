class MyClass:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'MyClass(name={self.name})'

    def __add__(self, other):
        return MyClass(self.name + ' ' + other.name)

    def __iadd__(self, other):
        self.name += ' ' + other.name
        return self

    def __mul__(self, n):
        return MyClass(self.name * n)

    def __imul__(self, n):
        self.name *= n
        return self

    def __rmul__(self, n):
        self.name += n
        return self

    def __contains__(self, value):
        return value in self.name

c1 = MyClass('MontyPython')

print('ty' in c1)
print(c1 * 3)