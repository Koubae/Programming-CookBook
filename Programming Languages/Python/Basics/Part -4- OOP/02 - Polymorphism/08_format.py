from datetime import date, datetime

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def __repr__(self):
        print('__repr__ called...')
        return f'Person(name={self.name}, dob={self.dob.isoformat()})'
    
    def __str__(self):
        print('__str__ called...')
        return f'Person({self.name})'
    
    def __format__(self, date_format_spec):
        print(f'__format__ called with {repr(date_format_spec)}...')
        dob = format(self.dob, date_format_spec)
        return f'Person(name={self.name}, dob={dob})'

p = Person('Alex', date(1900, 10, 20))
print(str(p))
# __str__ called...
# Person(Alex)
print(repr(p))
# __repr__ called...
# Person(name=Alex, dob=1900-10-20)
print(format(p, '%B %d, %Y'))
# __format__ called with '%B %d, %Y'...
# Person(name=Alex, dob=October 20, 1900)