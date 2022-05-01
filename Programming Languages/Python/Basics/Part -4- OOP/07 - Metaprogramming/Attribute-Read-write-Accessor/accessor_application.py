# Another useful application of __getattr__ and __setattr__ is dealing with objects where we may not know the attributes in advance.

# Consider this scenario where we have a database with various tables and fields. We want to create a class that allows us to retrieve data from these tables.

# We could certainly write a class for each specific table, and hardcode the fields as properties in the class - but that's going to create repetitive code, and anytime there is a new table or the schema of an existing table changes we'll have to revise our code.

# I'm going to simulate a database here by using dictionaries. The outer dictionary will contain tables (as keys), and each table will contain records with a numeric key for each record.

DB = {
    'Person': {
        1: {'first_name': 'Isaac', 'last_name': 'Newton', 'born': 1642, 'country_id': 1},
        2: {'first_name': 'Gottfried', 'last_name': 'von Leibniz', 'born': 1646, 'country_id': 5},
        3: {'first_name': 'Joseph', 'last_name': 'Fourier', 'born': 1768, 'country_id': 3},
        4: {'first_name': 'Bernhard', 'last_name': 'Riemann', 'born': 1826, 'country_id': 5},
        5: {'first_name': 'David', 'last_name': 'Hilbert', 'born': 1862 , 'country_id': 5},
        6: {'first_name': 'Srinivasa', 'last_name': 'Ramanujan', 'born': 1887, 'country_id': 4},
        7: {'first_name': 'John', 'last_name': 'von Neumann', 'born': 1903, 'country_id': 2},
        8: {'first_name': 'Andrew', 'last_name': 'Wiles', 'born': 1928, 'country_id': 6}
    },
    'Country': {
        1: {'name': 'United Kingdom', 'capital': 'London', 'continent': 'Europe'},
        2 :{'name': 'Hungary', 'capital': 'Budapest', 'continent': 'Europe'},
        3: {'name': 'France', 'capital': 'Paris', 'continent': 'Europe'},
        4: {'name': 'India', 'capital': 'New Delhi', 'continent': 'Asia'},
        5: {'name': 'Germany', 'capital': 'Berlin', 'continent': 'Europe'},
        6: {'name': 'USA', 'capital': 'Washington DC', 'continent': 'North America'}
        }
}

class Country:
    def __init__(self, id_):
        if _id in DB['Country']:
            self._db_record = DB['Country'][id_]
        else:
            raise ValueError(f'Record not found (Country.id={id_})')

    @property
    def name(self):
        return self._db_record['name']
    
    @property
    def capital(self):
        return self._db_record['capital']
    
    @property
    def continent(self):
        return self._db_record['continent']



class DBRecord:
    def __init__(self, db_record_dict):
        # again, careful how you set a property on instances of this class
        # because we are overriding __setattr__ we cannot just use 
        # self._record = db_record_dict
        # this will call OUR version of `__setattr__`, which attempts to 
        # see if name is in _record - but _record does not exist yet, so it will
        # call __getattr__, which in turn tries to check if that is contained in _record
        # so, infinite recursion.
        # What we want to here is BYPASS our custom __setattr__ - so we'll use
        # the one in the superclass.
        super().__setattr__('_record', db_record_dict)    
        
    def __getattr__(self, name):
        # here we could write
        #     if name in self._record 
        # since this method should not get called
        # before _record as been created.
        # But just to be on the safe side, I'm still going to use super
        if name in super().__getattribute__('_record'):
            return self._record[name]
        else:
            raise AttributeError(f'Field name {name} does not exist.')

    def __setattr__(self, name, value):
        # and again here, we could write
        # if name in self._record, but I'm still going to use super
        if name in super().__getattribute__('_record'):
            # super().__setattr__(name, value)
            self._record[name] = value
        else:
            raise AttributeError(f'Field name {name} does not exist.')

class DBTable:
    def __init__(self, db, table_name):
        if table_name not in db:
            raise ValueError(f'The table {table_name} does not exist in the database.')
        self._table_name = table_name
        self._table = db[table_name]
        
    @property
    def table_name(self):
        return self._table_name
    
    def __call__(self, record_id):
        if record_id not in self._table:
            raise ValueError(f'Specified id ({record_id}) does not exist '
                             f'in table {self._table_name}')
        return DBRecord(self._table[record_id])



tbl_person = DBTable(DB, 'Person')
tbl_country = DBTable(DB, 'Country')
person_1 = tbl_person(1)
# person_1.first_name, person_1.last_name, person_1.born, person_1.

country_id
# ('Isaac', 'Newton', 1642, 1)
country_1 = tbl_country(person_1.country_id)


country_1.name, country_1.capital
# ('United Kingdom', 'London')


class DBRecord:
    def __init__(self, db_record_dict):
        # again, careful how you set a property on instances of this class
        # because we are overriding __setattr__ we cannot just use 
        # self._record = db_record_dict
        # this will call OUR version of `__setattr__`, which attempts to 
        # see if name is in _record - but _record does not exist yet, so it will
        # call __getattr__, which in turn tries to check if that is contained in _record
        # so, infinite recursion.
        # What we want to here is BYPASS our custom __setattr__ - so we'll use
        # the one in the superclass.
        super().__setattr__('_record', db_record_dict)    
        
    def __getattr__(self, name):
        # here we could write
        #     if name in self._record 
        # since this method should not get called
        # before _record as been created.
        # But just to be on the safe side, I'm still going to use super
        if name in super().__getattribute__('_record'):
            return self._record[name]
        else:
            raise AttributeError(f'Field name {name} does not exist.')

    def __setattr__(self, name, value):
        # and again here, we could write
        # if name in self._record, but I'm still going to use super
        if name in super().__getattribute__('_record'):
            self._record[name] = value
        else:
            raise AttributeError(f'Field name {name} does not exist.')
            
    @property
    def fields(self):
        return tuple(self._record.keys())


tbl_person = DBTable(DB, 'Person')
person_1 = tbl_person(2)


person_1.fields
# ('first_name', 'last_name', 'born', 'country_id')

person_1.last_name
# 'von Leibniz'
person_1.last_name = 'Leibniz'
person_1.last_name
# 'Leibniz'


person_1.__dict__
# {'_record': {'first_name': 'Gottfried',
#   'last_name': 'Leibniz',
#   'born': 1646,
#   'country_id': 5}}