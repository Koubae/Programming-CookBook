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


# }
#
# template_as_set = set(template)
# john_as_set = set(john)
# print('Equality is =>', template_as_set == john_as_set)
# # Equality is => True
# intersect = template_as_set & john_as_set
# print(intersect)
# # {'name', 'bio', 'user_id'}
# print(template['name'], 'Get', template.get('name'))
# print(john['name'], 'Get', john.get('name'))
# # {'first': <class 'str'>, 'last': <class 'str'>} Get {'first': <class 'str'>, 'last': <class 'str'>}
# # {'first': 'John', 'last': 'Cleese'} Get {'first': 'John', 'last': 'Cleese'}
# # Nest 1
# template_name = template.get('name')
# john_name = john.get('name')
# print(set(template_name),set(john_name))
# # {'last', 'first'} {'last', 'first'}
#
#
# def get_nest():
#     template_as_set = set(template)
#     john_as_set = set(john)
#     if template_as_set == john_as_set:  # Perform intersect only if Receiving Dict has same top-level key of template
#         intersect = template_as_set & john_as_set
# #         return intersect
# #     else:
# #         raise ValueError('JSON response has invalid Keys')
#
#
# for i in get_nest():
#     template_name = template.get(i)
#     john_name = john.get(i)
#     # if not set(template_name) == set(john_name):
#     #     # raise ValueError('Received an invalid JSON response')
#     #     print('yes')
#     #     print()
#     # else:
#     #     print('No')
#     print('template >>>', template_name, 'john >>>', john_name)
#
# # template >>> {'dob': {'year': <class 'int'>, 'month': <class 'int'>,
# # 'day': <class 'int'>}, 'birthplace': {'country': <class 'str'>, 'city': <class 'str'>}}
# # john >>> {'dob': {'year': 1939, 'month': 11, 'day': 27}, 'birthplace': {'country': 'United Kingdom', 'city': 'Weston-super-Mare'}}
# # template >>> {'first': <class 'str'>, 'last': <class 'str'>} john >>> {'first': 'John', 'last': 'Cleese'}
#
#
# print(len(template.items()))
# d = {}
# for i in template.items():
#     if isinstance(i[1], dict):
#         d.update(i[1])
# d1 = {}
# for i in john.items():
#     if isinstance(i[1], dict):
#         d1.update(i[1])
#
# # sub_ = get_nest(d1, d)
# # print(sub_)
# d_ = {}
# for x in d.items():
#     if isinstance(x[1], dict):
#         d_.update(x[1])
#
# d_1 = {}
# for x in d1.items():
#     if isinstance(x[1], dict):
#         d_1.update(x[1])
#
#
# # print(d)
# print(d_)
# print('==='*15)
# print(d1)
# print(d_1)
#
#
# def retrive_nesting(dict_):
#     retriever = {}
#     for key in dict_.items():
#         if isinstance(key[1], dict):
#             retriever.update(key[1])
#     return retriever if retriever else None
#
#
# x = retrive_nesting(template)
# # print(x)
# # print('==='*15)
# # y = retrive_nesting(x)
# print(y)
# print('==='*15)
# z = retrive_nesting(y)
# print(z)

#
# def check_level(template, data):
#
#     t = []
#     d = []
#     i = [(get_nest(template, data))]
#     count = 0
#     def check_template(template, data):
#         nonlocal count
#         x = retrive_nesting(template)
#         y = retrive_nesting(data)
#         if x and (set(x) == set(y)):
#             t.append(x.keys())
#             d.append(y.keys())
#             i.append(get_nest(x, y))
#             count += 1
#             check_template(x, y)
#
#     check_template(template, data)
# #     return t, d, i
# #
# #
# #
# #
# # a = check_level(template, john)
# # print(a[0])
# # print(a[1])
# # print(a[2])
# # print(get_nest(template, john))
# # # [dict_keys(['first', 'last', 'dob', 'birthplace']), dict_keys(['year', 'month', 'day', 'country', 'city'])]
# # # [dict_keys(['first', 'last', 'dob', 'birthplace']), dict_keys(['year', 'month', 'day', 'country', 'city'])]
# # # [{'name', 'user_id', 'bio'}, {'first', 'last', 'dob', 'birthplace'}, {'year', 'day', 'country', 'month', 'city'}]
# # # {'name', 'user_id', 'bio'}
# #
#
# #
# # ##### Hook 3
# #
# # template_name = template.get('name')
# # john_name = john.get('name')
#
#
# def get_nest(data, template):
#     template_as_set = set(template)
#     data_as_set = set(data)
#     if template_as_set == data_as_set: # Perform intersect only if Receiving Dict has same top-level key of template
#         intersect = template_as_set & data_as_set
#         return intersect
#     else:
#         raise ValueError('JSON response has invalid Keys')
#
#
# def retrive_nesting(dict_):
#     retriever = {}
#     for key in dict_.items():
#         if isinstance(key[1], dict):
#             retriever.update(key[1])
#         else:
#             print(key)
#     return retriever if retriever else None
#
#
# # x = retrive_nesting(template)
# # # y = retrive_nesting(john)
# # y = retrive_nesting(x)
# # z = retrive_nesting(y)
# # # print(x)
# # print(y)
# # print(z)
# # print(set(x), set(y))
#
# def check_level(template, data):
#
#     t = []
#     d = []
#     i = [(get_nest(template, data))]
#     count = 0
#     def check_keys(template, data):
#         nonlocal count
#         x = retrive_nesting(template)
#         y = retrive_nesting(data)
#         if x and y:
#             if set(x) == set(y): # Check in sub nesting is the same
#                 t.append(x)
#                 d.append(y)
#                 i.append(get_nest(x, y))
#                 count += 1
#                 check_keys(x, y)
#             else:
#                 raise ValueError('JSON response has invalid Keys')
#
#     check_keys(template, data)
#     return t, d, i
#
#
# a = check_level(template, john)
# a_t = a[0]
# a_d = a[1]
# a_i = a[2]
# # print(len(a_d))
# # print((a_t[0]))
# # print(a_d[0])
# for i in a_i[0]:
#
#     x = template.get(i)
#     y = john.get(i)
#     print(i)
#     # print(x, y)
#     print(x == type(y))
#
# #
# # print(a_t)
#
# x = template.get('user_id')
# y = john.get('user_id')
# print(x, y)
