import json
import yaml
import serpy


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


class PersonSerializer(serpy.Serializer):
    name = serpy.StrField()
    age = serpy.IntField()

p1 = Person('Michael Palin', 75)


print(PersonSerializer(p1).data)
# {'name': 'Michael Palin', 'age': 75}


class Movie:
    def __init__(self, title, year, actors):
        self.title = title
        self.year = year
        self.actors = actors


class MovieSerializer(serpy.Serializer):
    title = serpy.StrField()
    year = serpy.IntField()
    actors = PersonSerializer(many=True)


p2 = Person('John Cleese', 79)
movie = Movie('Parrot Sketch', 1989, [p1, p2])


# movie.title, movie.year, movie.actors

('Parrot Sketch',
 1989,
 [Person(name=Michael Palin, age=75), Person(name=John
Cleese, age = 79)])

print(MovieSerializer(movie).data)


# {'title': 'Parrot Sketch',
#  'year': 1989,
#  'actors': [{'name': 'Michael Palin', 'age': 75},
#             {'name': 'John Cleese', 'age': 79}]}

print(json.dumps(MovieSerializer(movie).data))


# '{"title": "Parrot Sketch", "year": 1989, "actors": [{"name": "Michael Palin", "age": 75}, {"name": "John Cleese", "age": 79}]}'

print(yaml.dump(MovieSerializer(movie).data,
                default_flow_style=False))

# actors:
# - age: 75
# name: Michael
# Palin
# - age: 79
# name: John
# Cleese
# title: Parrot
# Sketch
# year: 1989

