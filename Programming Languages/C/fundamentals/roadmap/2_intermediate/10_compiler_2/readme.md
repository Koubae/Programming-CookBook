C Roadmap - Compiler 2
=======================

- Compiler 2
    - c header files [file].h
    - GNU (just understand what is it, no need to go deep in this)
    - [GCC Command-Line Options](http://tigcc.ticalc.org/doc/comopts.html)
    - gdb : C standard debugger
    - C Projects
        -  Typical C project structures
        - CMAKE
        - Make

- [A Simple Makefile Tutorial](https://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)
- [How to write a Makefile with separate source and header directories?](https://stackoverflow.com/a/30602701/13903942)

- [How to tell VSCode where to find header and source files](https://stackoverflow.com/a/65133723/13903942)


### GCC Command-line

- [3.4 Options Controlling C Dialect](https://gcc.gnu.org/onlinedocs/gcc/C-Dialect-Options.html#C-Dialect-Options)
- [GCC Command-Line Options](http://tigcc.ticalc.org/doc/comopts.html)

```
-Wall 
-Werror 
# include debuggin symbol
-g 

```


Compilation
-----------

Compilation can involve up to four stages: preprocessing, compilation proper, assembly and linking, always in that order. The first three stages apply to an individual source file, and end by producing an object file; linking combines all the object files (those newly compiled, and those specified as input) into an executable file. 

1. preprocessing
2. compilation proper
3. assembly
4. linking


<dl>
<dt><p><b><i>file</i>.c</b></p></dt><dd><p>C source code which must be preprocessed.
</p></dd><dt><p><b><i>file</i>.s</b></p></dt><dd><p>GNU Assembler code.
</p></dd><dt><p><b><i>file</i>.S</b></p></dt><dd><p>GNU Assembler code which must be preprocessed.
</p></dd><dt><p><b><i>file</i>.asm</b></p></dt><dd><p>A68k Assembler code.
</p></dd><dt><p><b><i>file</i>.o</b></p></dt><dd><p>COFF object file to be linked using <code>ld</code>.
</p></dd><dt><p><b><i>file</i>.a</b></p></dt><dd><p>Static library (function archive) to be linked using <code>ld</code>.</p>
</dd></dl>


### gdb

- [GDB: The GNU Project Debugger](https://www.sourceware.org/gdb/)

- [Online debugger - onlinegdb](https://www.onlinegdb.com/)