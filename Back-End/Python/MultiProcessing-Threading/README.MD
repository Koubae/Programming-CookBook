Multiprocessing & Threading
=======================



One difference between the threading and multiprocessing examples is the extra protection for **__main__** used in the multiprocessing examples. 
Due to the way the new processes are started, the child process needs to be able to import the script containing the target function. Wrapping the main part of the application in a check for **__main__** ensures that it is not run recursively in each child as the module is imported. 
Another approach is to import the target function from a separate script.

-----------------------------------------------------------------------------------------------------

Pathos
---------


- [pathos --GITHUB--](https://github.com/uqfoundation/pathos)
- [pathos --DOCS--](https://pathos.readthedocs.io/en/latest/pathos.html#pathos-module-documentation)


-----------------------------------------------------------------------------------------------------

Multiprocess - external package
-------------------------------


- [multiprocess --GITHUB--](https://github.com/uqfoundation/multiprocess)


-----------------------------------------------------------------------------------------------------

## Notes

* Lock [Lock (computer science) --WIKI--](https://en.wikipedia.org/wiki/Lock_(computer_science))


