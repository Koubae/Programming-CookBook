import random


def counter():
    i = 0

    def inc():
        nonlocal i
        i += 1
        return i

    return inc

cnt = counter()


class CounterIterator:
    def __init__(self, counter_callable, sentinel):
        self.counter_callable = counter_callable
        self.sentinel = sentinel
        self.is_consumed = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_consumed:
            raise StopIteration
        else:
            result = self.counter_callable()
            if result == self.sentinel:
                self.is_consumed = True
                raise StopIteration
            else:
                return result



cnt = counter()
cnt_iter = CounterIterator(cnt, 5)
for c in cnt_iter:
    print(c)
# 1
# 2
# 3
# 4
# next(cnt_iter) => StopIteration



cnt = counter()
cnt_iter = iter(cnt, 5) # => Same
for c in cnt_iter:
    print(c)

#random Example

random_iterator = iter(lambda : random.randint(0, 10), 8)
random.seed(0)

for num in random_iterator:
    print(num)

# Countdoun
def countdown(start=10):
    def run():
        nonlocal start
        start -= 1
        return start
    return run

takeoff = countdown(10)
for _ in range(15):
    print(takeoff())

takeoff  = countdown(10)
takeoff_iter = iter(takeoff, -1)

for val in takeoff_iter:
    print(val)