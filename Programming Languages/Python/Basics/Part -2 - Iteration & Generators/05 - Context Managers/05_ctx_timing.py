from time import perf_counter, sleep


class Timer:
    def __init__(self):
        self.elapsed = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False


with Timer() as timer:
    sleep(1)
print(timer.elapsed)

# 0.9993739623039163

