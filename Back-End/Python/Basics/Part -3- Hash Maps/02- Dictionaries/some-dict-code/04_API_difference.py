
n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
n2 = {'employees': 250, 'users': 23, 'user': 230}
n3 = {'employees': 150, 'users': 4, 'login': 1000}


dict_union = n1.keys() | n2.keys() | n3.keys()
dict_intersection = n1.keys() & n2.keys() & n3.keys()
dict_differ = dict_union - dict_intersection
print('Union |', dict_union)
print('Intersection &', dict_intersection)
print('Difference -', dict_differ)
set_differ = (set(n1) | set(n2) | set(n3)) - (set(n1) & set(n2) & set(n3))
print(set_differ)
# Union | {'login', 'user', 'employee', 'users', 'employees'}
# Intersection & {'users', 'employees'}
# Difference - {'login', 'employee', 'user'}


def nodes(node1, node2, node3):
    node_order = (node1, node2, node3)
    def get_node():
        return (set(node1) | set(node2) | set(node3)) - (set(node1) & set(node2) & set(node3))

    node = get_node()
    return {i: (node1.get(i, 0), node2.get(i, 0), node3.get(i, 0)) for i in node}


my_nodes = nodes(n1, n2, n3)
print('my_nodes -->', my_nodes)  # {'login', 'employee', 'user'}

# zip(n1.get(i, 0), n2.get(i, 0), n3.get(i, 0))


def identify(node1, node2, node3):
    union = node1.keys() | node2.keys() | node3.keys()
    intersection = node1.keys() & node2.keys() & node3.keys()
    relevant = union - intersection
    result = {key: (node1.get(key, 0),
                    node2.get(key, 0),
                    node3.get(key, 0))
              for key in relevant}
    return result

result = identify(n1, n2, n3)
for k, v in result.items():
    print(f'{k}: {v}')

#
# login: (0, 0, 1000)
# user: (100, 230, 0)
# employee: (5000, 0, 0)
#