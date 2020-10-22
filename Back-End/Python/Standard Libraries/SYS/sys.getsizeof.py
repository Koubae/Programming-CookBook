import sys

prev = 0
for i in range(11):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} TUPLE={c} items: {size_c}, delta={delta}')

print('==='*15)
prev = 0
for i in range(11):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} LIST={c} items:{size_c}, delta={delta}')


print('==='*15)
# Size of List when appened

c = []
prev = sys.getsizeof(c)
print(f'0 items: {sys.getsizeof(c)}')
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta={delta}')
