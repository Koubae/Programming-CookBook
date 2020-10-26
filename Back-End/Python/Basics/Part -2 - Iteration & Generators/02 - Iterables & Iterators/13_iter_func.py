class Squares:
    def __init__(self, n):
        self._n = n

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if i >= self._n:
            raise IndexError
        else:
            return i*2

class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._i >= len(self._squares):
            raise StopIteration
        else:
            result = self._squares[self._i]
            self._i += 1
            return result

sq = Squares(5)
sq_iterator = SquaresIterator(sq)
print(type(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
print(next(sq_iterator))
# <class '__main__.SquaresIterator'>
# 0
# 2
# 4
# 6
# 8


# leverage the fact that the sequence will raise an IndexError if the index is out of bounds:
class SquaresIterator:
    def __init__(self, squares):
        self._squares = squares
        self._i = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = self._squares[self._i]
            self._i += 1
            return result
        except IndexError:
            raise StopIteration()


sq_iterator = SquaresIterator(sq)
for i in sq_iterator:
    print(i)
