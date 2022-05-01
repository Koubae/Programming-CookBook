class Cities:
    def __init__(self):
        self._cities = ['New York', 'Newark', 'New Delhi', 'Newcastle']
    
    def __len__(self):
        return len(self._cities)
    
    def __getitem__(self, s):
        print('Getting Item')
        return self._cities[s]
    
    def __iter__(self):
        print('Calling Cities instance __iter__')
        return CityIterator(self)


class CityIterator:
    def __init__(self, city_obj):
        print('Calling CityIterator __init__')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('Calling CitiyIterator instance __iter__')
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
cities[0]
# Getting Item

next(iter(cities))
# Clling Cities instance __iter__
# Calling CityIterator __init__
# Calling __next__
print('==='*15)
cities = Cities()
for city in cities: # => Will call the Iterator Protocol
    print(city)

# Calling Cities instance __iter__
# Calling CityIterator __init__
# Calling __next__
# New York
# Calling __next__
# Newark
# Calling __next__
# New Delhi
# Calling __next__
# Newcastle
# Calling __next__