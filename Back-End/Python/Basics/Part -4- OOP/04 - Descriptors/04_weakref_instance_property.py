class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), 
                                     int(value)
                                    )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1]  # return the associated value, not the weak ref
        
    def _remove_object(self, weak_ref):
        print(f'removing dead entry for {weak_ref}')
        # how do we find that weak reference?

class Point:
    x = IntegerValue()


class IntegerValue:
    def __init__(self):
        self.values = {}
        
    def __set__(self, instance, value):
        self.values[id(instance)] = (weakref.ref(instance, self._remove_object), 
                                     int(value)
                                    )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.values.get(id(instance))
            return value_tuple[1]  # return the associated value, not the weak ref
        
    def _remove_object(self, weak_ref):
        # reverse_lookup = [key for key, value in self.values.items()
        #                  if value[0] is weak_ref]
        # if reverse_lookup:
        #     # key found
        #     key = reverse_lookup[0]
        #     del self.values[key]
        for key, value in self.values.items():
            if value[0] is weak_ref:
                def self.values[key]
                break

class Point:
    x = IntegerValue()

class Person:
    pass

print(hasattr(Person.__weakref__, '__get__'), hasattr(Person.__weakref__, '__set__'))
#(True, True)

class Person:
    __slots__ = 'name',
p = Person()
print(hasattr(p, '__weakref__'))
# False
class Person:
    __slots__ = 'name', '__weakref__'
p = Person()
print(hasattr(p, '__weakref__'))
# True


class ValidString:
    def __init__(self, min_length=0, max_length=255):
        self.data = {}
        self._min_length = min_length
        self._max_length = max_length
        
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError('Value must be a string.')
        if len(value) < self._min_length:
            raise ValueError(
                f'Value should be at least {self._min_length} characters.'
            )
        if len(value) > self._max_length:
            raise ValueError(
                f'Value cannot exceed {self._max_length} characters.'
            )
        self.data[id(instance)] = (weakref.ref(instance, self._finalize_instance), 
                                value
                                )
        
    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        else:
            value_tuple = self.data.get(id(instance))
            return value_tuple[1]  
        
    def _finalize_instance(self, weak_ref):
        reverse_lookup = [key for key, value in self.data.items()
                        if value[0] is weak_ref]
        if reverse_lookup:
            # key found
            key = reverse_lookup[0]
            del self.data[key]


class Person:
    __slots__ = '__weakref__',
    
    first_name = ValidString(1, 100)
    last_name = ValidString(1, 100)
    
    def __eq__(self, other):
        return (
            isinstance(other, Person) and 
            self.first_name == other.first_name and 
            self.last_name == other.last_name
        )
    
class BankAccount:
    __slots__ = '__weakref__',
    
    account_number = ValidString(5, 255)
    
    def __eq__(self, other):
        return (
            isinstance(other, BankAccount) and 
            self.account_number == other.account_number
        )

p1 = Person()

try:
    p1.first_name = ''
except ValueError as ex:
    print(ex)
Value should be at least 1 characters.

p2 = Person()

p1.first_name, p1.last_name = 'Guido', 'van Rossum'
p2.first_name, p2.last_name = 'Raymond', 'Hettinger'

b1, b2 = BankAccount(), BankAccount()

b1.account_number, b2.account_number = 'Savings', 'Checking'

p1.first_name, p1.last_name

# ('Guido', 'van Rossum')

p2.first_name, p2.last_name

# ('Raymond', 'Hettinger')

b1.account_number, b2.account_number

# ('Savings', 'Checking')

Person.first_name.data
# {140356851360776: (<weakref at 0x7fa76043e818; to 'Person' at 0x7fa760446408>,
#   'Guido'),
#  140356851360152: (<weakref at 0x7fa7400752c8; to 'Person' at 0x7fa760446198>,
#   'Raymond')}

Person.last_name.data
# {140356851360776: (<weakref at 0x7fa740075138; to 'Person' at 0x7fa760446408>,
#   'van Rossum'),
#  140356851360152: (<weakref at 0x7fa740075598; to 'Person' at 0x7fa760446198>,
#   'Hettinger')}

BankAccount.account_number.data

# {140356851360536: (<weakref at 0x7fa76043e868; to 'BankAccount' at 0x7fa760446318>,
#   'Savings'),
#  140356851361256: (<weakref at 0x7fa740075868; to 'BankAccount' at 0x7fa7604465e8>,
#   'Checking')}

del p1
del p2
del b1
del b2

Person.first_name.data
# {}

Person.last_name.data
# {}

BankAccount.account_number.data
# {}