
print(f'Loading run.py:__name__ = {__name__}')
import module1
import timing


if __name__ == '__main__':
    print('Running run.py...')
    result = timing.timeit('a=1')
    print(result)


# Loading run.py:__name__ = __main__
# Loading Moduel1:__name__ = module1
# Running run.py...
# Timing(repeats=10, elapsed=6.900000000004125e-06, average=6.900000000004125e-07)