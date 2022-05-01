class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __iter__(self):
        print('Calling __iter__')
        return self
    
    def __next__(self):
        print('calling __next__')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(3)

for i in sq:
    print(i)

# Calling __iter__
# calling __next__
# 0
# calling __next__
# 1
# calling __next__
# 4
# calling __next__
print('==='*15)
sq = Squares(5)
x = [item for item in sq if item%2 == 0]
# Calling __iter__
# calling __next__
# calling __next__
# calling __next__
# calling __next__
# calling __next__
# calling __next__
print('==='*15)
sq = Squares(5)
list(enumerate(sq))
print('==='*15)
sq = Squares(5)
sorted(sq, reverse=True)


# Mimic Python Protocol Iteretor

sq = Squares(5)
sq_iteretor = iter(sq)         # Demostrates iter returns itself
print(id(sq), id(sq_iteretor)) #1851376892032 1851376892032 
while True:
    try:
        item = next(sq_iteretor)
        print(item)
    except StopIteration:
        break
# calling __next__
# 0
# calling __next__
# 1
# calling __next__
# 4
# calling __next__
# 9
# calling __next__
# 16
# calling __next__
