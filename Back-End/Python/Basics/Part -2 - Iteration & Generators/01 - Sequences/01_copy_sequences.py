from copy import deepcopy

l1 = [1, 2, 3]
# For Loop
l1_copy = []
for item in l1:
    l1_copy.append(item)

print(l1_copy)

# List Comprehension
l1 = [1, 2, 3]
ly_copy = [item for item in l1]
print(ly_copy)

# copy Metod
l1 = [1, 2, 3]
l1_copy = l1.copy()
print(ly_copy)

# List Function
l1 = [1, 2, 3]
l1_copy = list(l1)


# Sclicing
l1 = [1, 2, 3]
l1_copy = l1[:]
print(l1_copy)
print(l1_copy is l1)


# Deep`Copy 1 level

v1 = [0, 0]
v2 = [0, 0]

line1 = [v1, v2]
line2 = [item[:] for item in line1]
print(id(line1[0]), id(line1[1]))
print(id(line2[0]), id(line2[1]))
# 1994553986816 1994553986560
# 1994553967232 1994553986880

v1 = [0, 0]
v2 = [0, 0]
lin1 = [v1, v2]
line2 = deepcopy(lin1)
print(id(lin1[0]), id(lin1[1]))
print(id(line2[0]), id(line2[1]))