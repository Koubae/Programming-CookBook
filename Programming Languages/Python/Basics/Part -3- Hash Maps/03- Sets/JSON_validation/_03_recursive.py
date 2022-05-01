from tests import template, john, eric, michael
from _02_match_types import match_keys, match_types


persons = ((john, 'John'), (eric, 'Eric'), (michael, 'Michael'))


def recurse_validate(data, template, path):
    # validate keys match
    is_ok, err_msg = match_keys(data, template, path)
    if not is_ok:
        return False, err_msg

    # validate individual data types match
    is_ok, err_msg = match_types(data, template, path)
    if not is_ok:
        return False, err_msg

    # Dicts, only if Value is a SubDict
    dictionary_type_keys = {key for key, value in template.items()
                            if isinstance(value, dict)}
    for key in dictionary_type_keys:
        sub_path = path + '.' + str(key)
        sub_template = template[key]
        sub_data = data[key]
        is_ok, err_msg = recurse_validate(sub_data, sub_template, sub_path)
        if not is_ok:
            return False, err_msg

    return True, None



def validate(data, template):
    return recurse_validate(data, template, '')


for person, name in persons:
    is_ok, err_msg = validate(person, template)

    print(f'{name}: valid={is_ok}: {err_msg}')



# John: valid=True: None
# Eric: valid=False: missing keys:.bio.birthplace.city
# Michael: valid=False: incorrect type: .bio.dob.month -> expected int, found str

class SchemaError(Exception):
    pass

def validate(data, template):
    is_ok, err_msg = recurse_validate(data, template, '')
    if not is_ok:
        raise SchemaError(err_msg)