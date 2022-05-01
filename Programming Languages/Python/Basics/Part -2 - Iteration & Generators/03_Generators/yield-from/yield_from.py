def matrix(n):
    gen = ((i * j for j in range(1, n+1))
           for i in range(1, n+1))
    return gen


m = list(matrix(5))
# for i in m:
#     print(i)
# <generator object matrix.<locals>.<genexpr>.<genexpr> at 0x00000262C9AE4A50>


def matrix_iterator(n):
    for row in matrix(n):
        for item in row:
            yield item

for i  in  matrix_iterator(3):
    print(i)

1
2
3
2
4
6
3
6
9


def matrix_iterator(n):
    for row in matrix(n):
        yield from row

# Using yield
def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            for line in f:
                yield line.strip('\n')
files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'
for brand in brands(*files):
    print(brand, end = ', ')

# using Yield From

def brands(*files):
    for f_name in files:
        with open(f_name) as f:
            yield from f
for brand in brands(*files):
    print(brand, end=', ')




def gen_clean_read(file):
    with open(file) as f:
        for line in f:
            yield line.strip('\n')
files = 'car-brands-1.txt', 'car-brands-2.txt', 'car-brands-3.txt'


def brands(*files):
    for file in files:
        yield from gen_clean_read(file)

for brand in brands(*files):
    print(brand, end=', ')



