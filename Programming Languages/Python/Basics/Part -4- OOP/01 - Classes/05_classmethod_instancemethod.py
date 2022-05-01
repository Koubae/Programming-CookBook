from datetime import datetime, timezone, timedelta
from time import sleep


class MyClass:
    def hello():
        # this IS an instance method, we just forgot to add a parameter to capture the instance
        # when this is called from an instance - so this will fail
        print('hello...')

    def instance_hello(arg):
        print(f'hello from {arg}')

    @classmethod
    def class_hello(arg):
        print(f'hello from {arg}')


m = MyClass()
MyClass.hello()
# m.hello()
# m.hello()
# TypeError: hello() takes 0 positional arguments but 1 was given
MyClass.class_hello()
MyClass.instance_hello(m)
m.instance_hello()
#hello from <__main__.MyClass object at 0x0000020A89188220>
print('\n', '==='*15)

class MyClass:
    def instance_hello(self):
        print(f'Instance method bound to {self}')

    @classmethod
    def class_hello(cls):
        print(f'Class method bound to {cls}')

    @staticmethod
    def static_hello():
        print('Static method not bound to anything')

m = MyClass()
m.instance_hello()
MyClass.class_hello()
m.class_hello()
MyClass.static_hello()
m.static_hello()
# Instance method bound to <__main__.MyClass object at 0x00000213BD2D87C0>
# Class method bound to <class '__main__.MyClass'>
# Class method bound to <class '__main__.MyClass'>
# Static method not bound to anything
# Static method not bound to anything


class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

Timer.set_tz(-7, 'MST')
print(Timer.tz)

t1 = Timer()
t2 = Timer()
print(t1.tz, t2.tz)
# MST MST
Timer.set_tz(-8, 'PST')
print(t1.tz, t2.tz)
# PST PST


class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

Timer.current_dt_utc()
t = Timer()
print(t.current_dt_utc())
# 2020-11-09 05:27:00.298819+00:00

class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    @staticmethod
    def current_dt_utc():
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

print(Timer.current_dt_utc(), Timer.current_dt())
# 2020-11-09 05:27:39.105782+00:00 2020-11-09 05:27:39.105782+00:00
t1 = Timer()
t2 = Timer()
print(t1.current_dt_utc(), t1.current_dt())
# 2020-11-09 05:27:59.187120+00:00 2020-11-09 05:27:59.187120+00:00


class TimerError(Exception):
    """A custom exception used for Timer class"""
    # (since """...""" is a statement, we don't need to pass)


class Timer:
    tz = timezone.utc  # class variable to store the timezone - default to UTC

    def __init__(self):
        # use these instance variables to keep track of start/end times
        self._time_start = None
        self._time_end = None

    @staticmethod
    def current_dt_utc():
        """Returns non-naive current UTC"""
        return datetime.now(timezone.utc)

    @classmethod
    def set_tz(cls, offset, name):
        cls.tz = timezone(timedelta(hours=offset), name)

    @classmethod
    def current_dt(cls):
        return datetime.now(cls.tz)

    def start(self):
        # internally we always non-naive UTC
        self._time_start = self.current_dt_utc()
        self._time_end = None

    def stop(self):
        if self._time_start is None:
            # cannot stop if timer was not started!
            raise TimerError('Timer must be started before it can be stopped.')
        self._time_end = self.current_dt_utc()

    @property
    def start_time(self):
        if self._time_start is None:
            raise TimerError('Timer has not been started.')
        # since tz is a class variable, we can just as easily access it from self
        return self._time_start.astimezone(self.tz)

    @property
    def end_time(self):
        if self._time_end is None:
            raise TimerError('Timer has not been stopped.')
        return self._time_end.astimezone(self.tz)

    @property
    def elapsed(self):
        if self._time_start is None:
            raise TimerError('Timer must be started before an elapsed time is available')

        if self._time_end is None:
            # timer has not ben stopped, calculate elapsed between start and now
            elapsed_time = self.current_dt_utc() - self._time_start
        else:
            # timer has been stopped, calculate elapsed between start and end
            elapsed_time = self._time_end - self._time_start

        return elapsed_time.total_seconds()

t1 = Timer()
t1.start()
sleep(2)
t1.stop()
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')
# Start time: 2020-11-09 05:31:11.391672+00:00
# End time: 2020-11-09 05:31:13.392697+00:00
# Elapsed: 2.001025 seconds


t2 = Timer()
t2.start()
sleep(3)
t2.stop()
print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')
# Start time: 2020-11-09 05:31:13.392697+00:00
# End time: 2020-11-09 05:31:16.404083+00:00
# Elapsed: 3.011386 seconds

Timer.set_tz(-7, 'MST')
print(f'Start time: {t1.start_time}')
print(f'End time: {t1.end_time}')
print(f'Elapsed: {t1.elapsed} seconds')

# Start time: 2020-11-08 22:32:02.462590-07:00
# End time: 2020-11-08 22:32:04.472562-07:00
# Elapsed: 2.009972 seconds



print(f'Start time: {t2.start_time}')
print(f'End time: {t2.end_time}')
print(f'Elapsed: {t2.elapsed} seconds')
# Start time: 2020-11-08 22:32:04.472562-07:00
# End time: 2020-11-08 22:32:07.485527-07:00
# Elapsed: 3.012965 seconds