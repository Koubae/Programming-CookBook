import yaml
from datetime import date
from pprint import pprint

data = '''
---
title: Parrot Sketch
year: 1989
actors:
    - first_name: John
      last_name: Cleese
      dob: 1939-10-27
    - first_name: Michael
      last_name: Palin
      dob: 1943-05-05
'''

d = yaml.load(data)
type(d)
#dict

pprint(d)

# {'actors': [{'dob': datetime.date(1939, 10, 27),
#              'first_name': 'John',
#              'last_name': 'Cleese'},
#             {'dob': datetime.date(1943, 5, 5),
#              'first_name': 'Michael',
#              'last_name': 'Palin'}],
#  'title': 'Parrot Sketch',
#  'year': 1989}

d = {'a': 100, 'b': False, 'c': 10.5, 'd': [1, 2, 3]}
print(yaml.dump(d))

# a: 100
# b: false
# c: 10.5
# d: [1, 2, 3]
print(yaml.dump(d, default_flow_style=False))

# a: 100
# b: false
# c: 10.5
# d:
# - 1
# - 2
# - 3


class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob

    def __repr__(self):
        return f'Person(name={self.name}, dob={self.dob})'


p1 = Person('John Cleese', date(1939, 10, 27))
p2 = Person('Michael Palin', date(1934, 5, 5))


print(yaml.dump({'john': p1, 'michael': p2}))


yaml_data = '''
john: !!python/object:__main__.Person 
    dob: 1939-10-27
    name: John Cleese
michael: !!python/object:__main__.Person 
    dob: 1934-05-05
    name: Michael Palin
'''

d = yaml.load(yaml_data)
print(d)

# {'john': Person(name=John Cleese, dob = 1939 - 10 - 27),
# 'michael': Person(name=Michael
# Palin, dob = 1934 - 05 - 05)}





yaml_data = '''
exec_paths: 
    !!python/object/apply:os.get_exec_path []
exec_command:
    !!python/object/apply:subprocess.check_output [['ls', '/']]
'''


print(yaml.load(yaml_data))


{'exec_paths': ['/Users/fbaptiste/anaconda3/envs/deepdive/bin',
                '/Users/fbaptiste/anaconda3/envs/deepdive/bin',
                '/Users/fbaptiste/anaconda3/bin',
                '/usr/local/bin',
                '/usr/bin',
                '/bin',
                '/usr/sbin',
                '/sbin'],
 'exec_command': b'Applications\nLibrary\nNetwork\nSystem\nUsers\nVolumes\nbin\ncores\ndev\netc\nhome\ninstaller.failurerequests\nnet\nprivate\nsbin\ntmp\nusr\nvar\n'}



class Person(YAMLObject):
    yaml_tag = '!Person'
    yaml_loader = SafeLoader

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'


yaml.safe_load(yaml_data)

