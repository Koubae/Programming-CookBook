def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()


class GenContextManager:
    def __init__(self, gen):
        self.gen = gen

    def __enter__(self):
        return next(self.gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        print('calling next to perform cleanup in generator')
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False



file_gen = open_file('test.txt', 'w')

with GenContextManager(file_gen) as f:
    f.writelines('Sir Spamalot')

file_gen = open_file('test.txt')
with GenContextManager(file_gen) as f:
    print(f.readlines())

# opening file...
# calling next to perform cleanup in generator
# closing file...
# opening file...
# ['Sir Spamalot']
# calling next to perform cleanup in generator
# closing file...
print('==='*15)
print('---'*15)
print('==='*15)

def context_manager_dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContextManager(gen)
        return ctx
    return helper

@context_manager_dec
def open_file(fname, mode='r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()

with open_file('test.txt') as f:
    print(f.readlines())


# opening file...
# ['Sir Spamalot']
# calling next to perform cleanup in generator
# closing file...