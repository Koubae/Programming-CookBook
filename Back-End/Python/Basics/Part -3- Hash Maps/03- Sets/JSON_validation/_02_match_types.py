from tests import template, john, eric, michael


def match_keys(data, valid, path):

    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
    print(extra_keys)
    print(missing_keys)

    if missing_keys or extra_keys:
        is_ok = False
        missing_msg = ('missing keys:' +
                       ','.join({path + '.' + str(key)
                                 for key in missing_keys})
                      ) if missing_keys else ''
        extras_msg = ('extra keys:' +
                     ','.join({path + '.' + str(key)
                               for key in extra_keys})
                     ) if extra_keys else ''
        return False, ' '.join((missing_msg, extras_msg))
    else:
        return True, None


t = {'a': int, 'b': int, 'c': int, 'd': int}
d = {'a': 'wrong type', 'b': 100, 'c': 200, 'd': {'wrong': 'type'}}
is_ok, err_msg = match_keys(d, t, 'some.path')
print(is_ok, err_msg)


def match_types(data, template, path):
    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if not isinstance(data_value, template_type):
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            return False, err_msg
    return True, None


t = {'a': int, 'b': str, 'c': {'d': int}}
d = {'a': 100, 'b': 'test', 'c': {'some': 'dict'}}
print(match_types(d, t, 'some.path')) # (True, None)

d = {'a': 100, 'b': 'test', 'c': 'unexpected'}
print(match_types(d, t, 'some.path'))
# (False, 'incorrect type: some.path.c -> expected dict, found str')
d = {'a': 100, 'b': 200, 'c': {'some': 'dict'}}
print(match_types(d, t, 'some.path'))
# (False, 'incorrect type: some.path.b -> expected str, found int')