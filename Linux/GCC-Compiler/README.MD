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

- - O (Capital)

Turn on optimization

- Wall

indicates that gcc should warn about many types of suspicious code that are likely to be incorrect.

- -nostartfiles 

Here, -nostartfiles gcc flag prevents the compiler from using standard startup files when linking

- -c 
The-cflag tells the compiler just to produce an object file — extensin myfile.c to --> myfile.o

### Separate Compilation & Object File

```
gcc -Wall -O -c myfile.c
gcc -Wall -O -c myotherfile.c

gcc -o myapp myfile.o myotherfile.c -lm

```

These files are not executables,but just machine-level representations of the code within each source file.
To combine the object files into an executable, you have to “link”them together;


### makefile | make | gmake | makedepend

The program `make` lets you automate much of your build process,and is thus a crucially important tool for any serious program


- make clean

Typing make clean will al-ways result in the command(s) being executed. In this case, thecleantarget is used to remove the object files and executable, quite handy ifyou wish to rebuild the entire program from scratch.

-----------------------------------------------------------------------------------------------------


### Debugging

- g 

generate debugging information for gdb (Warning , don't turn on -O Optimization; though thismay work, it may also lead to confusion during debugging. )

After re-compiling with-g, you are ready to use the debugger. Fireupgdbat the command prompt as follows:

- gdb [filename]

This puts you inside an interactive session with the debugger.Notethat you can also use the debugger to examine “core” files that were pro-duced during bad runs, or to attach to an already-running program; 

The first thing you might want to do is to go ahead and run the pro-gram. To do this, simply typerunat gdb command prompt, type:
```
run 

// BreakPoint

break main
```


-----------------------------------------------------------------------------------------------------