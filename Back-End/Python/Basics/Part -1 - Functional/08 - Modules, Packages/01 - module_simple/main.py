# main.py
import os
import types
module_name = 'module1'
module_file = 'module1_source.py'
module_path = '.'


module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)
print(module_rel_file_path)
print(module_abs_file_path)


with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()
    print(source_code)

# Create a Module object
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path
print(mod)

# compile the module source code into a code object
# optionally we should tell the code object where the source came from
# the third parameter is used to indicate that our source consists of a sequence of statements
code = compile(source_code, filename=module_abs_file_path, mode='exec')


# execute the module
# we want the global variables to be stored in mod.__dict__
exec(code, mod.__dict__)

mod.hello()

