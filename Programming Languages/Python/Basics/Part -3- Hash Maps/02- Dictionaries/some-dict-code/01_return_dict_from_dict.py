
composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}

item_dict = sorted(composers.items(), key=lambda x: x[1])
new_dict = {k: v for k, v in item_dict}
other_dict = {k: v for k, v in
              sorted(composers.items(), key=lambda x: x[1])}
print(new_dict)
print(other_dict)


def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda el: el[1]))


print(sort_dict_by_value(composers))

# {'Wolfgang': 35, 'Frederic': 39, 'Ludwig': 56, 'Johann': 65}
