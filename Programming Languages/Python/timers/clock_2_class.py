from datetime import datetime


class Clock:
    def __init__(self, hours=0, minutes=0):
        self._hours = hours
        self._minutes = minutes

    def __repr__(self):
        return f'Clock({self._hours},{self._minutes})'

    def __iter__(self):
        return self

    def __next__(self):
        if self._minutes == 59:
            if self._hours == 23:
                self._hours = 0
            else:
                self._hours += 1
            self._minutes = 0
        else:
            self._minutes += 1
        return f'{self._hours:02}:{self._minutes:02}'


time = datetime.utcnow()

clock = Clock(time.hour, time.minute)
for i in range(10):
    print(next(clock))