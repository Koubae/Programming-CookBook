import math


class Factorial:
    def __init__(self, length):
        self.length = length

    def __iter__(self):
        pass

    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result


class Factorials:
    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result


factorials = Factorials()
fact_iter = iter(factorials)

for _ in range(10):
    print(next(fact_iter))
# 1
# 1
# 2
# 6
# 24
# 120
# 720
# 5040
# 40320
# 362880



