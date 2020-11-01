
class File:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('closing file...')
        self.file.close()
        return False

with File('test.txt', 'w') as f:
    f.write('This is a late parrot!')

def test():
    with File('test.txt', 'w') as f:
        f.write('This is a late parrot')
        if True:
            return f
        print(f.closed)
    print(f.closed)



f = test()

# opening file...
# closing file...
# opening file...
# closing file...
print('==='*15)
print('---'*15)
print('==='*15)

class File():
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode

    def __enter__(self):
        print('opening file...')
        self.file = open(self.name, self.mode)
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('closing file...')
        self.file.close()
        return False

with File('test.txt', 'r') as file_ctx:
    print(next(file_ctx.file))
    print(file_ctx.name)
    print(file_ctx.mode)

# opening file...
# This is a late parrot
# test.txt
# r
# closing file...