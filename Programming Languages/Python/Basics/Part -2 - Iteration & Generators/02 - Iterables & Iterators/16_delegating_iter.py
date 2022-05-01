from collections import namedtuple


Person = namedtuple('Person', 'first last')


class PersonNames:
    def __init__(self, persons):
        try:
            self._persons = [person.first.capitalize()
                             + ' ' + person.last.capitalize()
                             for person in persons]
        except TypeError:
            self._persons = []

    def __iter__(self):
        return iter(self._persons)

persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]
person_names = PersonNames(persons)
persons = [Person('michaeL', 'paLin'), Person('eric', 'idLe'),
           Person('john', 'cLeese')]


for p in person_names:
    print(p)

print([tuple(person_name.split()) for person_name in sorted(person_names)])
print(sorted(person_names, key=lambda x: x.split()[1]))
# Michael Palin
# Eric Idle
# John Cleese
# [('Eric', 'Idle'), ('John', 'Cleese'), ('Michael', 'Palin')]
# ['John Cleese', 'Eric Idle', 'Michael Palin']
