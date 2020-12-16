import datetime
import heapq

def email(frequency, details):
    current = datetime.datetime.now()
    while True:
        current += frequency
        yield current, details

fast_email = email(datetime.timedelta(minutes=15), "fast email")
slow_email = email(datetime.timedelta(minutes=40), "slow email")

unified = heapq.merge(fast_email, slow_email)


for _ in range(10):
    print(next(unified))

# (datetime.datetime(2020, 12, 16, 11, 43, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 11, 58, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 12, 8, 15, 535048), 'slow email')
# (datetime.datetime(2020, 12, 16, 12, 13, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 12, 28, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 12, 43, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 12, 48, 15, 535048), 'slow email')
# (datetime.datetime(2020, 12, 16, 12, 58, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 13, 13, 15, 535048), 'fast email')
# (datetime.datetime(2020, 12, 16, 13, 28, 15, 535048), 'fast email')


# FAQ: The inputs to merge() in this example are infinite generators.
#  The return value assigned to the variable unified is
#  also an infinite iterator. This iterator will
#  yield the emails to be sent in the order of the future timestamps.