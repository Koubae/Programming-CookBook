#------------------------------#
# Example 1
#------------------------------#


def combine(string, target):
    target.update(string.split(' '))


def cleanup(combined):
    words = {'the', 'and', 'a', 'or', 'is', 'of'}
    combined -= words


result = set()
combine('lumberjacks sleep all night', result)
combine('the mistry of silly walks', result)
combine('this parrot is a late parrot', result)
cleanup(result)
print(result)

# {'parrot', 'this', 'walks', 'mistry', 'late', 'lumberjacks', 'night', 'silly', 'sleep', 'all'}

#------------------------------#
# Example 2
#------------------------------#
def gen_read_data():
    yield ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']
    yield ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']
    yield ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']


data = gen_read_data()

next(data)
# ['Paris', 'Beijing', 'New York', 'London', 'Madrid', 'Mumbai']

next(data)
# ['Hyderabad', 'New York', 'Milan', 'Phoenix', 'Berlin', 'Cairo']

next(data)
# ['Stockholm', 'Cairo', 'Paris', 'Barcelona', 'San Francisco']

next(data)
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-25-8ad47eec7ca3> in <module>
# ----> 1 next(data)

# StopIteration: 


def filter_incoming(*cities, data_set):
    data_set.difference_update(cities)


result = set()
data = gen_read_data()
for page in data:
    result.update(page)
    filter_incoming('Paris', 'London', data_set=result)
print(result)

# {'Hyderabad', 'New York', 'Phoenix', 'San Francisco', 'Barcelona', 'Mumbai', 'Stockholm', 'Cairo', 'Madrid', 'Milan', 'Beijing', 'Berlin'}

