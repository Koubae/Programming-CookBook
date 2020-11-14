
class Singleton(type):
    instances = {}
    
    def __call__(cls, *args, **kwargs):
        print(f'Request received to create an instance of class: {cls}...')
        existing_instance = Singleton.instances.get(cls, None)
        if existing_instance is None:
            print('Creating instance for the first time...')
            existing_instance = super().__call__(*args, **kwargs)
            Singleton.instances[cls] = existing_instance
        else:
            print('Using existing instance...')
        return existing_instance


class Hundred(metaclass=Singleton):
    value = 100
    
class Thousand(metaclass=Singleton):
    value = 1000
    
class HundredFold(Hundred):
    value = 100 * 100


h1 = Hundred()
h2 = Hundred()
# Request received to create an instance of class: <class '__main__.Hundred'>...
# Creating instance for the first time...
# Request received to create an instance of class: <class '__main__.Hundred'>...
# Using existing instance...


t1 = Thousand()
t2 = Thousand()
# Request received to create an instance of class: <class '__main__.Thousand'>...
# Creating instance for the first time...
# Request received to create an instance of class: <class '__main__.Thousand'>...
# Using existing instance...


hf1 = HundredFold()
hf2 = HundredFold()
# Request received to create an instance of class: <class '__main__.HundredFold'>...
# Creating instance for the first time...
# Request received to create an instance of class: <class '__main__.HundredFold'>...
# Using existing instance...

h1 is h2, t1 is t2, hf1 is hf2
# (True, True, True)

print(h1.value, h2.value, t1.value, t2.value, hf1.value, hf2.value)
# (100, 100, 1000, 1000, 10000, 10000)

h1 is hf1
# False