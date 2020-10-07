import sys
import time

print(sys.getsizeof(0))
# 24

# Here we see that to store the number 1
# required 4 bytes (32 bits) on top of the 24 byte overhead:
print(sys.getsizeof(10))
# 28

print(sys.getsizeof(2**1000))
# 160

def calc(a):
    for i in range(10_000_000):
        a * 2


start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)
# 0.3617183

start = time.perf_counter()
calc(2**10_000)
end = time.perf_counter()
print(end - start)
# 5.3573709