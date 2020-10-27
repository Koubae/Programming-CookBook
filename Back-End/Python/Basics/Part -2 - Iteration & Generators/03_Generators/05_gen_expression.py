from math import factorial
import tracemalloc



def combo(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))


size = 10  # global variable
pascal = [ [combo(n, k) for k in range(n+1)] for n in range(size+1) ]


# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
# [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

def pascal_list(size):
    l = [[combo(n, k) for k in range(n+1)] for n in range(size+1)]
    for row in l:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')


def pascal_gen(size):
    g = ((combo(n, k) for k in range(n+1)) for n in range(size+1))
    for row in g:
        for item in row:
            pass
    stats = tracemalloc.take_snapshot().statistics('lineno')
    print(stats[0].size, 'bytes')

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_list(300)
# 1998608 bytes

tracemalloc.stop()
tracemalloc.clear_traces()
tracemalloc.start()
pascal_gen(300)
# 1148 bytes