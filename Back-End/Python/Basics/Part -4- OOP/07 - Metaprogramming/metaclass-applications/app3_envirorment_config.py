import configparser



with open('prod.ini', 'w') as prod, open('dev.ini', 'w') as dev:
    prod.write('[Database]\n')
    prod.write('db_host=prod.mynetwork.com\n')
    prod.write('db_name=my_database\n')
    prod.write('\n[Server]\n')
    prod.write('port=8080\n')
    
    dev.write('[Database]\n')
    dev.write('db_host=dev.mynetwork.com\n')
    dev.write('db_name=my_database\n')
    dev.write('\n[Server]\n')
    dev.write('port=3000\n')





class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        self.db_host = config['Database']['db_host']
        self.db_name = config['Database']['db_name']
        self.port = config['Server']['port']


config = Config('dev')
# Loading config from dev file...
config.__dict__
# {'db_host': 'dev.mynetwork.com', 'db_name': 'my_database', 'port': '3000'}



class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            for key, value in config[section_name].items():
                setattr(self, key, value)


config = Config('prod')
# Loading config from prod file...

config.__dict__
# {'db_host': 'prod.mynetwork.com', 'db_name': 'my_database', 'port': '8080'}

print(config.port)
# '8080'

class Section:
    def __init__(self, name, item_dict):
        """
        name: str
            name of section
        item_dict : dictionary
            dictionary of named (key) config values (value)
        """
        self.name = name
        for key, value in item_dict.items():
            setattr(self, key, value)

class Config:
    def __init__(self, env='dev'):
        print(f'Loading config from {env} file...')
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            section = Section(section_name, config[section_name])
            setattr(self, section_name.lower(), section)


config = Config()
# Loading config from dev file...
# Now we have sections:

vars(config)
# {'database': <__main__.Section at 0x7f8ce09f6e48>,
#  'server': <__main__.Section at 0x7f8ce09f65f8>}

vars(config.database)
{'name': 'Database', 'db_host': 'dev.mynetwork.com', 'db_name': 'my_database'}

# help(Config)
# Help on class Config in module __main__:

# class Config(builtins.object)
#  |  Config(env='dev')
#  |  
#  |  Methods defined here:
#  |  
#  |  __init__(self, env='dev')
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)


class SectionType(type):
    def __new__(cls, name, bases, cls_dict, section_name, items_dict):
        cls_dict['__doc__'] = f'Configs for {section_name} section'
        cls_dict['section_name'] = section_name
        for key, value in items_dict.items():
            cls_dict[key] = value
        return super().__new__(cls, name, bases, cls_dict)

class DatabaseSection(metaclass=SectionType, section_name='database', items_dict={'db_name': 'my_database', 'host': 'myhost.com'}):
    pass


vars(DatabaseSection)
# mappingproxy({'__module__': '__main__',
#               '__doc__': 'Configs for database section',
#               'section_name': 'database',
#               'db_name': 'my_database',
#               'host': 'myhost.com',
#               '__dict__': <attribute '__dict__' of 'DatabaseSection' objects>,
#               '__weakref__': <attribute '__weakref__' of 'DatabaseSection' objects>})
# As you can see, our items db_name and host are in the class.

DatabaseSection.db_name




class PasswordsSection(metaclass=SectionType, section_name='passwords', items_dict={'db': 'secret', 'site': 'super secret'}):
    pass


vars(PasswordsSection)
# mappingproxy({'__module__': '__main__',
#               '__doc__': 'Configs for passwords section',
#               'section_name': 'passwords',
#               'db': 'secret',
#               'site': 'super secret',
#               '__dict__': <attribute '__dict__' of 'PasswordsSection' objects>,
#               '__weakref__': <attribute '__weakref__' of 'PasswordsSection' objects>})

MyClass = type('MyClass', (object,), {})
print(MyClass)
# __main__.MyClass

MySection = SectionType('DBSection', (object,), {}, section_name='databases', items_dict={'db_name': 'my_db', 'port': 8000})
print(MySection)
# __main__.DBSection


vars(MySection)
# mappingproxy({'__doc__': 'Configs for databases section',
#               'section_name': 'databases',
#               'db_name': 'my_db',
#               'port': 8000,
#               '__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'DBSection' objects>,
#               '__weakref__': <attribute '__weakref__' of 'DBSection' objects>})

class ConfigType(type):
    def __new__(cls, name, bases, cls_dict, env):
        """
        env : str
            The environment we are loading the config for (e.g. dev, prod)
        """
        cls_dict['__doc__'] = f'Configurations for {env}.'
        cls_dict['env'] = env
        config = configparser.ConfigParser()
        file_name = f'{env}.ini'
        config.read(file_name)
        for section_name in config.sections():
            class_name = section_name.capitalize()
            class_attribute_name = section_name.casefold()
            section_items = config[section_name]
            bases = (object, )
            section_cls_dict = {}
            # create a new Section class for this section
            Section = SectionType(
                class_name, bases, section_cls_dict, section_name=section_name, items_dict=section_items
            )
            # And assign it to an attribute in the main config class
            cls_dict[class_attribute_name] = Section
        return super().__new__(cls, name, bases, cls_dict)



class DevConfig(metaclass=ConfigType, env='dev'):
    pass

class ProdConfig(metaclass=ConfigType, env='prod'):
    pass


vars(DevConfig)
# mappingproxy({'__module__': '__main__',
#               '__doc__': 'Configurations for dev.',
#               'env': 'dev',
#               'database': __main__.Database,
#               'server': __main__.Server,
#               '__dict__': <attribute '__dict__' of 'DevConfig' objects>,
#               '__weakref__': <attribute '__weakref__' of 'DevConfig' objects>})

# help(DevConfig)
# Help on class DevConfig in module __main__:

# class DevConfig(builtins.object)
#  |  Configurations for dev.
#  |  
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
#  |  
#  |  ----------------------------------------------------------------------
#  |  Data and other attributes defined here:
#  |  
#  |  database = <class '__main__.Database'>
#  |      Configs for Database section
#  |  
#  |  env = 'dev'
#  |  
#  |  server = <class '__main__.Server'>
#  |      Configs for Server section



vars(DevConfig.database)
# mappingproxy({'__doc__': 'Configs for Database section',
#               'section_name': 'Database',
#               'db_host': 'dev.mynetwork.com',
#               'db_name': 'my_database',
#               '__module__': '__main__',
#               '__dict__': <attribute '__dict__' of 'Database' objects>,
#               '__weakref__': <attribute '__weakref__' of 'Database' objects>})





print(DevConfig.database.db_host, ProdConfig.database.db_host)
# ('dev.mynetwork.com', 'prod.mynetwork.com')