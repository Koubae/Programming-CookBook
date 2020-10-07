import math


print(math.floor(3.999999999))
# 3

math.floor(-3.0000001)
# -4


a = 33
b = 16
print(a/b)
print(a//b) # same
print(math.floor(a/b)) # Same

# 2.0625
# 2
# 2

a = -33
b = 16
print('{0}/{1} = {2}'.format(a, b, a/b))
print('trunc({0}/{1}) = {2}'.format(a, b, math.trunc(a/b)))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('floor({0}//{1}) = {2}'.format(a, b, math.floor(a/b)))


# -33/16 = -2.0625
# trunc(-33/16) = -2
# -33//16 = -3
# floor(-33//16) = -3

# The Modulo Operator
# The modulo operator and the floor division operator will always satisfy the following equation:
#
# a = b * (a // b) + a % b

a = 13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

# 13/4 = 3.25
# 13//4 = 3
# 13%4 = 1
# True


a = -13
b = 4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)


# -13/4 = -3.25
# -13//4 = -4
# -13%4 = 3
# True


a = 13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)

# 13/-4 = -3.25
# 13//-4 = -4
# 13%-4 = -3
# True

a = -13
b = -4
print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a//b) + a%b)


# -13/-4 = 3.25
# -13//-4 = 3
# -13%-4 = -1
# True