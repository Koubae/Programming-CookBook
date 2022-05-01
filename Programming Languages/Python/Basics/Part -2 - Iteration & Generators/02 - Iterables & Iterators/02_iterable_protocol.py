class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']

    def __len__(self):
        return len(self._cities)
    
    def __iter__(self) -> iter: # Calling the Iterator Protocol with its instance
        print('Calling Cities instance __iter__' )
        return CityIterator(self)
    

class CityIterator:
    def __init__(self, city_obj):
        print('Calling CityIterator __init__')
        self._city_obj = city_obj
        self._index = 0
    
    def __iter__(self):
        print('Calling CityIterator instance __iter__')
        return self
    
    def __next__(self):
        print('Calling __next__')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item

cities = Cities()
list(enumerate(cities))
# Calling Cities instance __iter__
# Calling CityIterator __init__
# Calling __next__
# Calling __next__
# Calling __next__
# Calling __next__
# Calling __next__
print('==='*15)
iter_1 = iter(cities)
iter_2 = iter(cities)
print(id(iter_1), id(iter_2)) # 1668501808272 1668501808512