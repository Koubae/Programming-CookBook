def my_gen(): # Generator Function
    try:
        print('creating context and yielding object')
        lst = [1, 2, 3, 4, 5]
        yield lst
    finally:
        print('exiting context and cleaning up')



gen = my_gen()  # create generator

lst = next(gen)  # enter context and get "as" object
print(lst)
# next(gen)  # exit context
#
#
# exiting context and cleaning up
#
# ---------------------------------------------------------------------------
# StopIteration                             Traceback (most recent call last)
# <ipython-input-5-ad32aeec95bc> in <module>()
# ----> 1 next(gen)  # exit context
#
# StopIteration:

# catch the StopIteration exception

gen = my_gen()
lst = next(gen)
print(lst)
try:
    next(gen)
except StopIteration:
    pass


class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)

    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False


def open_file(fname, mode):
    try:
        print('opening file...')
        f = open(fname, mode)
        yield f
    finally:
        print('closing file...')
        f.close()


with GenCtxManager(open_file, 'test.txt', 'w') as f:
    print('writing to file...')
    f.write('testing...')

with open('test.txt') as f:
    print(next(f))