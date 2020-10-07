l = [1, 2, 3, 4]
a, b, c, d = l
print(a, b, c, d)

a, b, c = 'XYZ'
print(a, b, c)


# Swapping Two Variables

a = 10
b = 20
print("a={0}, b={1}".format(a, b))
a, b = 10, 20
print("a={0}, b={1}".format(a, b))

a, b = b, a # ----> Swapping
print("a={0}, b={1}".format(a, b))
