def squares_gen(n):
    for i in range(n):
        yield i ** 2

sq = squares_gen(5)
print([num for num in sq])
print([num for num in sq])

# [0, 1, 4, 9, 16]
# []

class Squares:
    def __init__(self, n):
        self.n = n

    @staticmethod
    def squares_gen(n):
        for i in range(n):
            yield i ** 2

    def __iter__(self):
        return Squares.squares_gen(self.n)

sq = Squares(5)

print([num for num in sq])
print([num for num in sq])

# [0, 1, 4, 9, 16]
# [0, 1, 4, 9, 16]