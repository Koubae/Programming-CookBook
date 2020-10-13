from collections import namedtuple

# We can also choose to let the namedtuple
# function replace invalid field names automatically for us,
# by using the keyword argument rename. When we set that argument
# to True (it is False by default) it will replace
# the invalid name using the position (index) of the field, preceded by an underscore:

                                                    # _age is invalid
Person = namedtuple('Person', ['firstname', 'lastname', '_age', 'ssn'], rename=True)

eric = Person('Eric', 'Idle', 42, 'unknown')

print(eric)
#>>> Person(firstname='Eric', lastname='Idle', _2=42, ssn='unknown')
# _2=42