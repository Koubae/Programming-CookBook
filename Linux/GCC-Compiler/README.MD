GCC-Compiler 
=======================


- [GCC online documentation](https://gcc.gnu.org/onlinedocs/)

- [GNU Autotools](https://en.wikipedia.org/wiki/GNU_Autotools)

Commands
--------

You can use the gcc compiler in linux to link two c file in one output. Suppose you have two c files one is 'main.c' and another is 'support.c'. So the command to link these two is

```gcc main.c support.c -o main.out```

- o

indicates that the next parameter is the name of the resulting program (or library). If this option is not specified, the compiled program will, for historic reasons, end up in a file called "a.out" or "a.exe" (for cygwin users).

- Wall

indicates that gcc should warn about many types of suspicious code that are likely to be incorrect.

- g 

generate debugging information for gdb

- -nostartfiles 

Here, -nostartfiles gcc flag prevents the compiler from using standard startup files when linking

-----------------------------------------------------------------------------------------------------