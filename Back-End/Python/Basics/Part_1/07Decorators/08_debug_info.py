from datetime import datetime, timezone

# monkey patching
def debug_info(cls):
    def info(self):
        results = []
        results.append('time: {0}'.format(datetime.now(timezone.utc)))
        results.append('class: {0}'.format(self.__class__.__name__))
        results.append('id: {0}'.format(hex(id(self))))

        if vars(self):
            for k, v in vars(self).items():
                results.append('{0}: {1}'.format(k, v))

        # we have not covered lists, the extend method and generators,
        # but note that a more Pythonic way to do this would be:
        # if vars(self):
        #    results.extend('{0}: {1}'.format(k, v)
        #                   for k, v in vars(self).items())

        return results

    cls.debug = info #

    return cls


@debug_info
class Person:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def say_hi():
        return 'Hello there!'


p1 = Person('John', 1939)
print(p1.debug())


# ['time: 2018-02-09 04:44:02.893951+00:00',
#  'class: Person',
#  'id: 0x2dfe29a4630',
#  'name: John',
#  'birth_year: 1939']


@debug_info
class Automobile:
    def __init__(self, make, model, year, top_speed_mph):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed_mph = top_speed_mph
        self.current_speed = 0

    @property
    def speed(self):
        return self.current_speed

    @speed.setter
    def speed(self, new_speed):
        self.current_speed = new_speed

s = Automobile('Ford', 'Model T', 1908, 45)

s.debug()

s.speed = 20
s.debug()