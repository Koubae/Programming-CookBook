from math import pi
from numbers import Real

class Circle:
    def __init__(self, r):
        self._set_radius(r)
        self._area = None
        self._perimeter = None
        
    @property
    def radius(self):
        return self._r

    def _set_radius(self, r):
        if isinstance(r, Real) and r > 0:
            self._r = r
            self._area = None
            self._perimeter = None
        else:
            raise ValueError('Radius must a positive real number.')

    @radius.setter
    def radius(self, r):
        self._set_radius(r)
            
    @property
    def area(self):
        if self._area is None:
            self._area = pi * self.radius ** 2
        return self._area
            
    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = 2 * pi * self.radius
        return self._perimeter


class UnitCircle(Circle):
    def __init__(self):
        super().__init__(1)
        
    @property
    def radius(self):
        return super().radius

u = UnitCircle()
print(u.radius) # 1


class Person:
    def method_1(self):
        print('Person.method_1')
        self.method_2()
        
    def method_2(self):
        print('Person.method_2')
        
class Student(Person):
    def method_1(self):
        print('Student.method_1')
        super().method_1()
        
    def method_2(self):
        print('Student.method_2')

s = Student()


s.method_1()
# Student.method_1
# Person.method_1
# Student.method_2
