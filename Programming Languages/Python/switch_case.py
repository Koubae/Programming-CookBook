
# A simple Java example would be something like this:

# switch (dow) {
#     case 1: dowString = 'Monday';
#             break;
#     case 2: dowString = 'Tuesday';
#             break;
#     case 3: dowString = 'Wednesday';
#             break;
#     case 4: dowString = 'Thursday';
#             break;
#     case 5: dowString = 'Friday';
#             break;
#     case 6: dowString = 'Saturday';
#             break;
#     case 7: dowString = 'Sunday';
#             break;
#     default: dowString = 'Invalid day of week';
# }


def dow_switch_fn(dow):
    if dow == 1:
        fn = lambda: print('Monday')
    elif dow == 2:
        fn = lambda: print('Tuesday')
    elif dow == 3:
        fn = lambda: print('Wednesday')
    elif dow == 4:
        fn = lambda: print('Thursday')
    elif dow == 5:
        fn = lambda: print('Friday')
    elif dow == 6:
        fn = lambda: print('Saturday')
    elif dow == 7:
        fn = lambda: print('Sunday')
    else:
        fn = lambda: print('Invalid day of week')
    
    return fn()

dow_switch_fn(1) # Monday


def dow_switch_dict(dow):
    dow_dict = {
        1: lambda: print('Monday'),
        2: lambda: print('Tuesday'),
        3: lambda: print('Wednesday'),
        4: lambda: print('Thursday'),
        5: lambda: print('Friday'),
        6: lambda: print('Saturday'),
        7: lambda: print('Sunday'),
        'default': lambda: print('Invalid day of week')
    }
    
    return dow_dict.get(dow, dow_dict['default'])()

dow_switch_dict(1) # Monday


def switcher(fn):
    registry = dict()
    registry['default'] = fn

    def register(case):
        def inner(fn):
            registry[case] = fn
            return fn # Stack register decorators
        return inner

    def decorator(case):
        fn = registry.get(case, registry['default'])
        return fn()
    
    decorator.register = register
    return decorator


@switcher
def dow():
    print('Invalid day of week')

@dow.register(1)
def dow_1():
    print('Monday')

@dow.register(2)
def dow_2():
    print('Tuesday')

dow_1()
dow_2()

dow.register(1)(lambda: print('Monday'))
dow.register(2)(lambda: print('Tuesday'))
dow.register(3)(lambda: print('Wednesday'))
dow.register(4)(lambda: print('Thursday'))
dow.register(5)(lambda: print('Friday'))
dow.register(6)(lambda: print('Saturday'))
dow.register(7)(lambda: print('Sunday'))

dow(1)
