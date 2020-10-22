import dis

def myfunc(alist):
    return len(alist)


print(dis.dis(myfunc))

from dis import dis, code_info


dis(compile('(1,2,3, "a")', 'string', 'eval'))
print('==='*15)
dis(compile('[1,2,3, "a"]', 'string', 'eval'))
print('==='*15)

print(code_info(myfunc))

# Name:              myfunc
# Filename:          C:/proj/deepdive/03_Section/dis_simple.py
# Argument count:    1
# Positional-only arguments: 0
# Kw-only arguments: 0
# Number of locals:  1
# Stack size:        2
# Flags:             OPTIMIZED, NEWLOCALS, NOFREE
# Constants:
#    0: None
# Names:
#    0: len
# Variable names:
#    0: alist
