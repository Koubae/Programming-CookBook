class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()


class ZRange: # ITERABLE
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return ZRangeIter(self.n)


class ZRangeIter: # ITERATOR
    def __init__(self, n):
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            StopIteration()

