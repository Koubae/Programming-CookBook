my_list = [0, 1, 2, 3, 4, 5]
print(my_list.__getitem__(0))

print(my_list.__getitem__(slice(0,6,2)))

my_list = [0, 1, 2, 3, 4, 5]

for item in my_list:
    print(item ** 2)

my_list = [0, 1, 2, 3, 4, 5]

index = 0
while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1


