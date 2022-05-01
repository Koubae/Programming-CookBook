import itertools
from collections import defaultdict


# with open('cars_2014.csv') as f:
#     for row in itertools.islice(f, 0, 20):
#         print(row, end = '')

makes = defaultdict(int)

with open('cars_2014.csv') as f:
    next(f)  # skip header row
    for row in f:
        make, _ = row.strip('\n').split(',')
        makes[make] += 1

for key, value in makes.items():
    print(f'{key}: {value}')

##----------------------------------------------##
data = (1, 1, 2, 2, 3)
print(list(itertools.groupby(data)))
# [(1, <itertools._grouper at 0x204a6988dd8>),
#  (2, <itertools._grouper at 0x204a69883c8>),
#  (3, <itertools._grouper at 0x204a6988208>)]

it = itertools.groupby(data)
for group in it:
    print(group[0], list(group[1]))
# 1 [1, 1]
# 2 [2, 2]
# 3 [3]
##----------------------------------------------##


data = (
    (1, 'abc'),
    (1, 'bcd'),

    (2, 'pyt'),
    (2, 'yth'),
    (2, 'tho'),

    (3, 'hon')
)

groups = list(itertools.groupby(data, key=lambda x: x[0]))
print(groups)

# [(1, <itertools._grouper object at 0x00000204A6990C50>),
#  (2, <itertools._grouper object at 0x00000204A6990BE0>),
#  (3, <itertools._grouper object at 0x00000204A6990BA8>)]

groups = itertools.groupby(data, key=lambda x: x[0])
for group in groups:
    print(group[0], list(group[1]))

# 1 [(1, 'abc'), (1, 'bcd')]
# 2 [(2, 'pyt'), (2, 'yth'), (2, 'tho')]
# 3 [(3, 'hon')]

##----------------------------------------------##

with open('cars_2014.csv') as f:
    next(f)  # skip header row
    make_groups = itertools.groupby(f, key=lambda x: x.split(',')[0])
    print(list(itertools.islice(make_groups, 5)))

print(list(itertools.islice(make_groups, 5)))



with open('cars_2014.csv') as f:
    next(f)  # skip header row
    make_groups = itertools.groupby(f, key=lambda x: x.split(',')[0])
    make_counts = ((key, sum(1 for model in models))
                    for key, models in make_groups)
    print(list(make_counts))

