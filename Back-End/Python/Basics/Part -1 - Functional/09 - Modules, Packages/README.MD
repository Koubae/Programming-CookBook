# Modules, Packages and Namespaces
=======================


- [The import system](https://docs.python.org/3/reference/import.html)
- [Modules](https://docs.python.org/3/tutorial/modules.html)
-----------------------------------------------------------------------------------------------------



This is how Python imports a module from file:

* checks the sys.modules cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise:

* creates a new module object (types.ModuleType)
* loads the source code from file
* adds an entry to sys.modules with name as key and the newly created
* ompiles and executes the source code

-----------------------------------------------------------------------------------------------------

## Modules

When a module is imported:

**System Cache** is checked first  sys.modules → if in cache, just returns cached reference

Otherwise:

1 Module has to be **located** (found) somewhere  *finders* --> sys.meta_path

2 Module code has to be **retrieve** (loaded)  *loaders* returned by finder ---> Module spec

3 Empty module typed object is created.

4 A **Reference** to the module is added to the system cache *sys.module*

5 Module is compiled.

6 Module is executed --> Set up module's namespace(module.__dict__ is module.globals())

#### Module Finders

- [DOCS](http://docs.python.org/3/glossary.html#term-finder)

A finder is an object that uses its find_module() method to try and find the loader for a module. importlib.abc.Finder is an example of an abstract base class for a finder. Note however that it is deprecated in favor of importlib.abc.MetaPathFinder and importlib.abc.PathEntryFinder.


- *sys.meta_path*

* _frozen_importlib.BuiltinImporter  --> finds built-ins, such as math
* _frozen_importlib.FrozenImporter  --> finds frozen modules
* _frozen_importlib_external.PathFinder --> file-based modules

- *PathFinder*

Finds file-based modules based on sys.path and package __path__
* sys.path
* collections.__path__

#### Module Loader

- [DOCS](http://docs.python.org/3/glossary.html#term-loader)

A loader is an object that is returned by a finder. It uses its load_module() method to load a module into memory. importlib.abc.Loader is an example of an abstract base class for a loader.


#### Module Properties

- module.__spec__
- module.__name__
- module.__package__
- __file__

__file__, __path__ and __package__ Properties

Modules have __file__ and __package__ properties

- *__file__ * --> is the location of module code in the file system
- *__package__ * --> is the package the module code is located in
- *__path__* is the location of the package (directory) in the file system

-----------------------------------------------------------------------------------------------------

## Namespace Packages

Namespace packages are package-likeThese directories are implicitly made into these special types of packages, These directories are implicitly made into these special types of packages.

- [Packaging namespace packages](https://packaging.python.org/guides/packaging-namespace-packages/)

- **Implicit Namespace Packages** [PEP 420](https://www.python.org/dev/peps/pep-0420/)
- [SSO](https://stackoverflow.com/questions/1675734/how-do-i-create-a-namespace-package-in-python)
- [Python Namespace Package Examples](https://github.com/pypa/sample-namespace-packages)
- [Organizing your Project](https://morepath.readthedocs.io/en/latest/organizing_your_project.html)
- [USING CHAINMAP FOR EMBEDDED NAMESPACES (PYTHON RECIPE)](https://code.activestate.com/recipes/578279-using-chainmap-for-embedded-namespaces/)

-----------------------------------------------------------------------------------------------------

## Zip Package

- [SSO](https://stackoverflow.com/questions/32239372/how-to-import-files-in-python-using-sys-path-append)
- [devdungeon](https://www.devdungeon.com/content/python-import-syspath-and-pythonpath-tutorial)


-----------------------------------------------------------------------------------------------------

## Features

- **types** — *Dynamic type creation and names for built-in types*
- [DOCS](https://docs.python.org/3.8/library/types.html)

- **importlib** — *The implementation of import*
- [DOCS](https://docs.python.org/3/library/importlib.html)

- **argparse** — *Parser for command-line options, arguments and sub-commands*
- [DOCS](https://docs.python.org/3.8/library/argparse.html)
- [Tutorial](https://docs.python.org/3.8/howto/argparse.html#id1)

- **New Import Hooks** [PEP 302](https://www.python.org/dev/peps/pep-0302/)

- [Import almost anything in Python](https://blog.quiltdata.com/import-almost-anything-in-python-an-intro-to-module-loaders-and-finders-f5e7b15cda47)

-----------------------------------------------------------------------------------------------------

### NOTES

- sys.modules() --> Check all the modules
- sys.prefix --> Where is Python installed
- sys.exec_prefix --> Where is Python installed
- sys.path ---> Where are the Lookups for the imports
- sys.executable --> A string giving the absolute path of the executable binary for the Python interpreter

-----------------------------------------------------------------------------------------------------