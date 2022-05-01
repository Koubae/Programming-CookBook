from timeit import timeit


def fib(n):
    fib_0 = 1
    fib_1 = 1
    for i in range(n-1):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


class Fib:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self.FibIter(self.n)

    class FibIter:
        def __init__(self, n):
            self.n = n
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.n:
                raise StopIteration
            else:
                result = fib(self.i)
                self.i += 1
                return result


def fib_gen(n):
    fib_0 = 1
    yield fib_0
    fib_1 = 1
    yield fib_1
    for i in range(n-2):
        fib_0, fib_1 = fib_1, fib_0 + fib_1
        yield fib_1


result_1 = timeit('[num for num in Fib(5_000)]', globals=globals(), number=1)
result_2 = timeit('[num for num in fib_gen(5_000)]', globals=globals(), number=1)
print(f'Fib Class rub in {result_1}')
print(f'fib_gen run in {result_2}')
# Fib Class rub in 1.0757409
# fib_gen run in 0.0010972000000000204