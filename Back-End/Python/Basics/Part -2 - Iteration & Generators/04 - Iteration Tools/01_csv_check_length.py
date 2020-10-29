
# test to make sure that every brand in our file is at least 3 characters long
with open('car-brands.txt') as f:
    result = all(map(lambda row: len(row) >= 3, f))
print(result)
# => True


#  test to see if any line is more than 10 characters
with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 10, f))
print(result)
# => True

# More than 13?
with open('car-brands.txt') as f:
    result = any(map(lambda row: len(row) > 13, f))
print(result)
# => False

# generator expressions instead of map
with open('car-brands.txt') as f:
    result = any(len(row) > 13 for row in f)
print(result)
# => False
