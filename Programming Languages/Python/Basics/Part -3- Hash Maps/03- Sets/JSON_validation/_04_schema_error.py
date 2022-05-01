from tests import template, john, eric, michael


class SchemaError(Exception):
    pass


class SchemaKeyMismatch(SchemaError):
    pass


class SchemaTypeMismatch(SchemaError, TypeError):
    pass


def match_keys(data, valid, path):

    data_keys = data.keys()
    valid_keys = valid.keys()

    extra_keys = data_keys - valid_keys
    missing_keys = valid_keys - data_keys
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
        raise SchemaKeyMismatch(' '.join((missing_msg, extras_msg)))


def match_types(data, template, path):

    for key, value in template.items():
        if isinstance(value, dict):
            template_type = dict
        else:
            template_type = value
        data_value = data.get(key, object())
        if isinstance(data_value, template_type):
            continue
        else:
            err_msg = ('incorrect type: ' + path + '.' + key +
                       ' -> expected ' + template_type.__name__ +
                       ', found ' + type(data_value).__name__)
            raise SchemaTypeMismatch(err_msg)


def recurse_validate(data, template, path):
    match_keys(data, template, path)
    match_types(data, template, path)

    dictionary_type_keys = {key for key, value in template.items()
                           if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        recurse_validate(sub_data, sub_template, sub_path)

def validate(data, template):
    recurse_validate(data, template, '')

print(validate(john, template))
# print(validate(eric, template))
# SchemaKeyMismatch: missing keys:.bio.birthplace.city

try:
    validate(eric, template)
except SchemaError as ex:
    print(ex)



try:
    validate(eric, template)
except SchemaKeyMismatch as ex:
    print('mismatched keys, doing some specific handling for that')
    print(ex)
except SchemaTypeMismatch as ex:
    print('mismatched types, doing some specific handling for that')
    print(ex)



try:
    validate(michael, template)
except SchemaKeyMismatch as ex:
    print('mismatched keys, doing some specific handling for that')
    print(ex)
except SchemaTypeMismatch as ex:
    print('mismatched types, doing some specific handling for that')
    print(ex)

# None
# missing keys:.bio.birthplace.city
# mismatched keys, doing some specific handling for that
# missing keys:.bio.birthplace.city
# mismatched types, doing some specific handling for that
# incorrect type: .bio.dob.month -> expected int, found str

