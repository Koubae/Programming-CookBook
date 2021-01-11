def sort_priority(values, group):
    def helper(x):
        if x in group:
            return 1, x
        elif x == 200:  # NOTE: 1
            return 0, x
        else:
            return 2, x
    values.sort(key=helper)

numbers = [8, 3, 1, 5, 4, 7, 6, 200]
group = {3, 5, 2, 7}
sort_priority(numbers, group)
print(numbers)  # [200, 3, 5, 7, 1, 4, 6, 8]

# NOTE: 1 Python has specific rules for comparing tuples. It first compares
# items in index zero, then index one, then index two, and so on.
# This is why the return value from the helper closure causes the
# sort order to have two distinct groups.

"""Similar but with A class"""

numbers = [8, 3, 1, 5, 4, 7, 6, 200]
group = {3, 5, 2, 7}


class Sorter(object):

    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)


sorter = Sorter(group)
numbers.sort(key=sorter)

assert sorter.found is True