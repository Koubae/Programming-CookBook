from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = {**d1, **d2, **d3}
print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

d = {}
d.update(d1)
d.update(d2)
d.update(d3)
print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
print(d)
# ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
print(isinstance(d, dict)) # False
for k, v in d.items():
    print(k, v)

## d 4
# c 3
# f 6
# b 2
# a 1
# e 5

d1 = {'a': 1, 'b': 2}
d2 = {'b': 20, 'c': 3}
d3 = {'c': 30, 'd': 4}
d = ChainMap(d1, d2, d3)



d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
print(d)
# ChainMap({'a': 1, 'b': 2, 'z': 100}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

print(d1)
print(d2)
print(d3)

# {'a': 1, 'b': 2, 'z': 100}
# {'c': 3, 'd': 4}
# {'e': 5, 'f': 6}



d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

d3 = {'d':400, 'e': 5 }
d = ChainMap(d3, d)
print(d)
#ChainMap({'d': 400, 'e': 5},
# ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}))

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)


d3 = {'d':400, 'e': 5 }
d = d.new_child(d3)
print(d)
#ChainMap({'d': 400, 'e': 5}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4})

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
d = ChainMap(d1, d2, d3)
print(d)
#ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})

d = d.parents
print(d)
#ChainMap({'c': 3, 'd': 4}, {'e': 5, 'f': 6})

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d = ChainMap(d1, d2)

type(d.maps), d.maps
# (list, [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}])
d3 = {'e': 5, 'f': 6}
d.maps.append(d3)
print(d.maps)

# [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
d.maps.insert(0, {'a': 100})
print(d.maps)
#
# [{'a': 100}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]

print(list(d.items()))
# [('d', 4), ('c', 3), ('f', 6), ('b', 2), ('a', 100), ('e', 5)]

config = {
    'host': 'prod.deepdive.com',
    'port': 5432,
    'database': 'deepdive',
    'user_id': '$pg_user',
    'user_pwd': '$pg_pwd'
}
local_config = ChainMap({}, config)
print(list(local_config.items()))


# [('user_pwd', '$pg_pwd'),
#  ('database', 'deepdive'),
#  ('port', 5432),
#  ('user_id', '$pg_user'),
#  ('host', 'prod.deepdive.com')]

local_config['user_id'] = 'test'
local_config['user_pwd'] = 'test'
print(list(local_config.items()))
# [('host', 'prod.deepdive.com'),
#  ('database', 'deepdive'),
#  ('port', 5432),
#  ('user_id', 'test'),
#  ('user_pwd', 'test')]
print(list(config.items()))
# [('host', 'prod.deepdive.com'),
#  ('port', 5432),
#  ('database', 'deepdive'),
#  ('user_id', '$pg_user'),
#  ('user_pwd', '$pg_pwd')]

print(local_config.maps)


# [{'user_id': 'test', 'user_pwd': 'test'},
#  {'host': 'prod.deepdive.com',
#   'port': 5432,
#   'database': 'deepdive',
#   'user_id': '$pg_user',
#   'user_pwd': '$pg_pwd'}]

