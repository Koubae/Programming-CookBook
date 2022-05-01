
my_var = [1, 2, 3, 4]
my_num = 10
print(id(my_num))
print(hex(my_num))

# REFERENCE COUNTING

import ctypes

def ref_count(address):
    return ctypes.c_long.from_address(address).value


print(ref_count(id(my_var)))
# >>> 1

import sys

print((sys.getrefcount(my_var)))
# >>> 2

#The sys.getrefcount() function takes my_var as an argument,
#this means it receives (and stores) a reference to my_var's memory address also - hence the count is off by 1. ' \
#'So use use from_address() instead.