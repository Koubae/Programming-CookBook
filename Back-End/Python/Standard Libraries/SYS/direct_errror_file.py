import sys


class Person:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'Person({self.name})'
    
    def __del__(self):
        print(f'__del__ called for {self}...')


class ErrToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stderr = sys.stderr
        
    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stderr = self._file
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        sys.stderr = self._current_stderr
        if self._file:
            self._file.close()
        return False

p = Person('Alex')

with ErrToFile('err.txt'):
    del p

with open('err.txt') as f:
    print(f.readlines())

p = Person('Fede')
