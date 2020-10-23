from functools import lru_cache
import copy


class Fib:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, s):
        if isinstance(s, int):  # Gets single item
            if s < 0:
                s = self._n + s
            if s < 0 or s > self._n -1:
                raise IndexError  # => Raise index error, handles out of range
            return self.fib(s)
        else: # Get by Index
            idx = s.indices(self._n) # slice(*).indices()
            rng = range(idx[0], idx[1], idx[2])
            return [self.fib(n) for n in rng]

    @staticmethod
    @lru_cache(2*32) # =>  maxsize at its default value of 128
    def fib(n):
        if n < 2:
            return 1
        else:
            return Fib.fib(n-1) + Fib.fib(n-2)

f = Fib(10)
print(len(f)) # > 10
print(f[:])
print(f[3])
print(f.fib(20))
print(f.__getitem__(3))
print(f[3])

D = 0; M = 1; Y = -1


class Person(object):
    def __init__(self, name, age, dob):
        self.name = name
        self.age = age
        self.dob = dob

    def __getitem__(self, idx):
        print(f'Calling __getitem__ at index-> {idx}')
        p = copy.copy(self)
        print(p)
        p.name = p.name.split(' ')[idx]
        p.dob = p.dob[idx]
        # p.dob = p.__getitem__(indx)
        return p
p = Person(name = 'Jonab Gutu', age = 20, dob=(1, 1, 1999))
print(p[0])
print(p[Y])
print('---'*15)
print(p[0].name)
print(p[-1].dob)