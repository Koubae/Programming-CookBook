
def process(s):
    print('Initial s# = {0}'.format(hex(id(s))))
    s = s + 'world'
    print('s after change # = {0}'.format(hex(id(s))))


my_var = 'Hello'
print('my_var # = {}'.format(hex(id(my_var))))
# After we "modify" s, s is pointing to a new memory address:
process(my_var)
#  our own variable my_var is still pointing to the original memory address:
print('my_var # = {0}'.format(hex(id(my_var))))

print('===' * 30)
print('WITH MUTABLE OBJECT\n\n')
# WITH MUTABLE OBJECT
def modify_list(items):
    print('Initial items # = {}'.format(hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2
    items.pop()
    items.append(5)
    print('Final items # = {}'.format(hex(id(items))))


my_list = [2, 3, 4]
print('my_list # = {0}'.format(hex(id(my_list))))
modify_list(my_list)

print('===' * 30)
print('IMMUTABLE CONTAINER WITH MUTABLE OBJECTS\n\n')


def modify_tuple(t):
    print('Initial t # = {}'.format(hex(id(t))))
    t[0].append(100)
    print('Final t # = {}'.format(hex(id(t))))


my_tuple = ([1, 2], 'a')
hex(id(my_tuple))

modify_tuple(my_tuple)


# my_var # = 0x1bee21c8930
# Initial s# = 0x1bee21c8930
# s after change # = 0x1bee21ca670
# my_var # = 0x1bee21c8930
# ==========================================================================================
# WITH MUTABLE OBJECT
#
# 
# my_list # = 0x1bee21700c0
# Initial items # = 0x1bee21700c0
# Final items # = 0x1bee21700c0
# ==========================================================================================
# IMMUTABLE CONTAINER WITH MUTABLE OBJECTS
#
#
# Initial t # = 0x1bee21ca640
# Final t # = 0x1bee21ca640
#
# Process finished with exit code 0
