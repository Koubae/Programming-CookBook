# ------------------------------------------------------------------#
# Validate one dictionary structure against a template dictionary.
# ------------------------------------------------------------------#

template = {
    'user_id': int,
    'name': {
        'first': str,
        'last': str
    },
    'bio': {
        'dob': {
            'year': int,
            'month': int,
            'day': int
        },
        'birthplace': {
            'country': str,
            'city': str
        }
    }
}


john = {
    'user_id': 100,
    'name': {
        'first': 'John',
        'last': 'Cleese'
    },
    'bio': {
        'dob': {
            'year': 1939,
            'month': 11,
            'day': 27
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Weston-super-Mare'
        }
    }
}

eric = {
    'user_id': 101,
    'name': {
        'first': 'Eric',
        'last': 'Idle'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 3,
            'day': 29
        },
        'birthplace': {
            'country': 'United Kingdom'
        }
    }
}


michael = {
    'user_id': 102,
    'name': {
        'first': 'Michael',
        'last': 'Palin'
    },
    'bio': {
        'dob': {
            'year': 1943,
            'month': 'May',
            'day': 5
        },
        'birthplace': {
            'country': 'United Kingdom',
            'city': 'Sheffield'
        }
    }
}


template_name = template.get('name')
john_name = john.get('name')


def get_nest(data, template):
    template_as_set = set(template)
    data_as_set = set(data)
    if template_as_set == data_as_set: # Perform intersect only if Receiving Dict has same top-level key of template
        intersect = template_as_set & data_as_set
        return intersect
    else:
        raise ValueError('JSON response has invalid Keys')


# x = retrive_nesting(template)
# # y = retrive_nesting(john)
# y = retrive_nesting(x)
# z = retrive_nesting(y)
# # print(x)
# print(y)
# print(z)
# print(set(x), set(y))

def validate(template, data):

    t = []
    d = []
    i = [(get_nest(template, data))]
    is_validate = True

    def retrive_nesting(dict_):
        retriever = {}
        for key in dict_.items():
            if isinstance(key[1], dict):
                retriever.update(key[1])
        return retriever if retriever else None

    def check_values(trimmed_template, trimmed_data):
        for values in i[-1]:
            a = trimmed_template.get(values)
            b = trimmed_data.get(values)
            if not isinstance(a, dict) or not isinstance(b, dict):
                assert a == type(b)

    def check_keys(template, data):

        x = retrive_nesting(template)
        y = retrive_nesting(data)
        check_values(template, data)
        if x and y:
            if set(x) == set(y): # Check in sub nesting is the same
                t.append(x)
                d.append(y)
                i.append(get_nest(x, y))
                check_keys(x, y)
            else:
                nonlocal is_validate
                is_validate = False
                #raise ValueError('JSON response has invalid Keys')


    check_keys(template, data)
    return is_validate


a = validate(template, john)
print(a)
b = validate(template, eric)
print(b)
c = validate(template, michael)
