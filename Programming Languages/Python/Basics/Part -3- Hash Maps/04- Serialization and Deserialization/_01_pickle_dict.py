import pickle

from pprint import pprint

ser = pickle.dumps('Python Pickled Peppers')
print(ser)
deser = pickle.loads(ser)
print(deser)
# b'\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x16Python Pickled Peppers\x94.'
# Python Pickled Peppers

# Numbers
ser = pickle.dumps(3.14)
print(ser)
deser = pickle.loads(ser)
print(deser)
# b'\x80\x04\x95\n\x00\x00\x00\x00\x00\x00\x00G@\t\x1e\xb8Q\xeb\x85\x1f.'
# 3.14


d = [10, 20, ('a', 'b', 30)]
ser = pickle.dumps(d)
print(ser)
deser = pickle.loads(ser)
print(deser)
# b'\x80\x04\x95\x15\x00\x00\x00\x00\x00\x00\x00]\x94(K\nK\x14\x8c\x01a\x94\x8c\x01b\x94K\x1e\x87\x94e.'
# [10, 20, ('a', 'b', 30)]

print('==='*15, '\n')

s = {'a', 'b', 'x', 10}
print(s)
ser = pickle.dumps(s)
print(ser)
# {'a', 'b', 10, 'x'}
# b'\x80\x04\x95\x13\x00\x00\x00\x00\x00\x00\x00\x8f\x94(\x8c\x01a\x94\x8c\x01b\x94K\n\x8c\x01x\x94\x90.'


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


john = Person('John Cleese', 79)
eric = Person('Eric Idle', 75)
michael = Person('Michael Palin', 75)



parrot_sketch = {
    "title": "Parrot Sketch",
    "actors": [john, michael]
}

ministry_sketch = {
    "title": "Ministry of Silly Walks",
    "actors": [john, michael]
}

joke_sketch = {
    "title": "Funniest Joke in the World",
    "actors": [eric, michael]
}



fan_favorites = {
    "user_1": [parrot_sketch, joke_sketch],
    "user_2": [parrot_sketch, ministry_sketch]
}

pprint(fan_favorites)
fan_favorites['user_1'][0] is fan_favorites['user_2'][0] # True

parrot_id_original = id(parrot_sketch)
ser = pickle.dumps(fan_favorites)
new_fan_favorites = pickle.loads(ser)
print(fan_favorites == new_fan_favorites) # True