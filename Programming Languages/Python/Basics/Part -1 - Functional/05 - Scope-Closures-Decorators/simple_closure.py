from time import perf_counter

# Implementation with Class
class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count


a = Averager()
a.add(10)
a.add(20)
a.add(30)

# Implementation with a function's closure
def averager():
    numbers = []
    def add(number):
        numbers.apppend(number)
        total = sum(numbers)
        count = len(numbers)
        return total / count
    return add

a = averager()
a(10)
a(20)
a(30)

###############################################
# Implementation with Class
class Timer:
    def __init__(self):
        self._start = perf_counter()

    def __call__(self):
        return (perf_counter() - self._start)

a = Timer()
a()
b = Timer()
print(a())
print(b())

# Implementation with a function's closure
def timer():

    start = perf_counter()

    def elapsed():
        return perf_counter() - start

    return elapsed

x = timer()
x()
y = timer()
print(x())
print(y())