from datetime import date
from marshmallow import Schema, fields, post_load
from collections import namedtuple


class Person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob

    def __repr__(self):
        return f'Person({self.first_name}, {self.last_name}, {self.dob})'



p1 = Person('John', 'Cleese', date(1939, 10, 27))



class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()


person_schema = PersonSchema()

person_schema.dump(p1)
print(type(person_schema.dump(p1).data)) # dict
print(person_schema.dumps(p1).data)
# '{"first_name": "John", "dob": "1939-10-27", "last_name": "Cleese"}'


PT=namedtuple('PT', 'first_name, last_name, dob')
p2 = PT('Eric', 'Idle', date(1943, 3, 29))
print(person_schema.dumps(p2).data)
# '{"first_name": "Eric", "dob": "1943-03-29", "last_name": "Idle"}'
PT2 = namedtuple('PT2', 'first_name, last_name, age')
p3 = PT2('Michael', 'Palin', 75)
print(person_schema.dumps(p3).data)
# '{"first_name": "Michael", "last_name": "Palin"}'

person_partial = PersonSchema(only=('first_name', 'last_name'))
print(person_partial.dumps(p1).data)
# '{"first_name": "John", "last_name": "Cleese"}'


person_partial = PersonSchema(exclude=['dob'])
print(person_partial.dumps(p1).data)
# '{"first_name": "John", "last_name": "Cleese"}'

p4 = Person(100, None, 200)
print(person_schema.dumps(p4))
# MarshalResult(data='{"first_name": "100", "last_name": null}',
#               errors={'dob': ['"200" cannot be formatted as a date.']})


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)

print(p1, p2)
#
# (Person(John, Cleese, 1939-10-27),
#  PT(first_name='Eric', last_name='Idle', dob=datetime.date(1943, 3, 29)))


parrot = Movie('Parrot Sketch', 1989, [p1,
                                       Person('Michael',
                                              'Palin',
                                              date(1943, 5, 5))
                                      ])


print(MovieSchema().dumps(parrot))

# MarshalResult(data='{"title": "Parrot Sketch", "year": 1989, "actors":
# [{"first_name": "John", "dob": "1939-10-27", "last_name": "Cleese"},
# {"first_name": "Michael", "dob": "1943-05-05", "last_name": "Palin"}]}', errors={})

class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()
    person_schema = PersonSchema()

person_schema.load(dict(first_name='John',
                        last_name='Cleese',
                        dob='1939-10-27'))

# UnmarshalResult(data={'first_name': 'John', 'dob': datetime.date(1939, 10, 27),
# : 'Cleese'}, errors={})

class PersonSchema(Schema):
    first_name = fields.Str()
    last_name = fields.Str()
    dob = fields.Date()

    @post_load
    def make_person(self, data):
        return Person(**data)


person_schema = PersonSchema()


person_schema.load(dict(first_name='John',
                        last_name='Cleese',
                        dob='1939-10-27'))


# UnmarshalResult(data=Person(John, Cleese, 1939-10-27), errors={})

class MovieSchema(Schema):
    title = fields.Str()
    year = fields.Integer()
    actors = fields.Nested(PersonSchema, many=True)

    @post_load
    def make_movie(self, data):
        return Movie(**data)



movie_schema = MovieSchema()

json_data = '''
{"actors": [
    {"first_name": "John", "last_name": "Cleese", "dob": "1939-10-27"}, 
    {"first_name": "Michael", "last_name": "Palin", "dob": "1943-05-05"}], 
"title": "Parrot Sketch", 
"year": 1989}
'''

movie = movie_schema.loads(json_data).data

print(movie.actors)