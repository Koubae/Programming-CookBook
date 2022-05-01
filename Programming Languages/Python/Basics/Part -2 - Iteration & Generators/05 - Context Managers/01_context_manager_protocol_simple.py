
class MyContext:
    def __init__(self):
        self.obj = None

    def __enter__(self):
        print('entering context...')
        self.obj = 'the Return Object'
        return self.obj

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exiting context...')
        if exc_type:
            print(f'*** Error occurred: {exc_type}, {exc_value}')
        return True  # suppress exceptions

with MyContext() as obj:
    raise ValueError
print('reached here without an exception...')


with MyContext() as obj:
    print('running inside with block...')
    print(obj)
print(obj)

print('==='*15)
print('---'*15)
print('==='*15)
# entering context...
# exiting context...
# *** Error occurred: <class 'ValueError'>,
# reached here without an exception...
# entering context...
# running inside with block...
# the Return Object
# exiting context...
# the Return Object

class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None


class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None

    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)# Creates instance of Resource
        self.resource.state = 'created' # Crete Instance Attribute of Resource
        return self.resource

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exiting context')
        self.resource.state = 'destroyed' # Change Instance Attribute of Resource
        if exc_type:
            print('error occurred')
        return False

with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')
print(f'{res.name} = {res.state}')

# entering context
# spam = created
# exiting context
# spam = destroyed
print('==='*15)
print('---'*15)
print('==='*15)
