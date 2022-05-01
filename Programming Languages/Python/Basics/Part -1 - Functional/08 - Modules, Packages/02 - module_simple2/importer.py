import os
import sys
import types

print('Running Importer.py')

def import_(module_name, module_file, module_path):
    if __name__ == '__main__':
        if module_name in sys.modules:
            return sys.modules[module_name]

    module_rel_file_path = os.path.join(module_path, module_file)
    module_abs_file_path = os.path.abspath(module_rel_file_path)

    # Read Source Code from file
    with open(module_rel_file_path, 'r') as code_file:
        source_code = code_file.read()

    # Create Module File
    mod = types.ModuleType(module_name)
    mod.__file__ = module_abs_file_path

    # Insert referenc into sys.modules
    sys.modules[module_name] = mod
    # the third parameter is used to indicate that our source consists of a sequence of statements
    code = compile(source_code, filename=module_abs_file_path, mode='exec')
    exec(code, mod.__dict__)

    return sys.modules[module_name]

