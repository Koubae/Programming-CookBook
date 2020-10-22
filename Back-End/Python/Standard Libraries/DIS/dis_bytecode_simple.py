from dis import Bytecode


def myfunc(x: int) -> str:
    return str(x*2)

print(help(myfunc))
print(myfunc(2))
print('==='*30)

my_byte_code = Bytecode(myfunc)
print(vars(my_byte_code))
print('==='*30)
for byte_code in my_byte_code:
    print(byte_code)
    print('---'*15)
    print(byte_code.opname)

# ==========================================================================================
# {'codeobj': <code object myfunc at 0x0000016EEEFCD450, file "C:/proj/deepdive/03_Section/dis_bytecode_simple.py", line 4>, 'first_line': 4, '_line_offset': 0, '_cell_names': (), '_linestarts': {0: 5}, '_original_object': <function myfunc at 0x0000016EEF017CA0>, 'current_offset': None}
# ==========================================================================================
# Instruction(opname='LOAD_GLOBAL', opcode=116, arg=0, argval='str', argrepr='str', offset=0, starts_line=5, is_jump_target=False)
# ---------------------------------------------
# LOAD_GLOBAL
# Instruction(opname='LOAD_FAST', opcode=124, arg=0, argval='x', argrepr='x', offset=2, starts_line=None, is_jump_target=False)
# ---------------------------------------------
# LOAD_FAST
# Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=2, argrepr='2', offset=4, starts_line=None, is_jump_target=False)
# ---------------------------------------------
# LOAD_CONST
# Instruction(opname='BINARY_MULTIPLY', opcode=20, arg=None, argval=None, argrepr='', offset=6, starts_line=None, is_jump_target=False)
# ---------------------------------------------
# BINARY_MULTIPLY
# Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=8, starts_line=None, is_jump_target=False)
# ---------------------------------------------
# CALL_FUNCTION
# Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=10, starts_line=None, is_jump_target=False)
# ---------------------------------------------
# RETURN_VALUE
#
# Process finished with exit code 0
