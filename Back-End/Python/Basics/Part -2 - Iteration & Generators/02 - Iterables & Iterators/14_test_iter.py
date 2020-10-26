class SimpleIter:
    def __init__(self):
        pass

    def __iter__(self):
        return 'Nope'


s = SimpleIter()
print('__iter__' in dir(s) ) # => True


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

obj = 100
if is_iterable(obj):
    for i in obj:
        print(i)
else:
    print('Error: obj is not iterable')

obj = 100
if is_iterable(obj):
    for i in obj:
        print(i)
else:
    print('Error: obj is not iterable')
    print('Taking some action as a consequence of this error')

obj = 100
try:
    for i in obj:
        print(i)
except TypeError:
    print('Error: obj is not iterable')
    print('Taking some action as a consequence of this error')

# True
# Error: obj is not iterable
# Error: obj is not iterable
# Taking some action as a consequence of this error
# Error: obj is not iterable
# Taking some action as a consequence of this error
