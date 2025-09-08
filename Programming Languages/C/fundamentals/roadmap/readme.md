C RoadMap
---------

*What you need to learn in order become a C programmer/developer.*

### See Also

- [C - Keywords & Terms (Programming-CookBook)](./keywords_and_terms.md)
- [C - Fundamentals (Programming-CookBook)](./fundamentals)

- [C Programming For Beginners – A 20 Day Curriculum!](https://www.geeksforgeeks.org/c-programming-for-beginners-a-20-day-curriculum/)
- [What is the detail roadmap for learning C programming language?](https://www.quora.com/What-is-the-detail-roadmap-for-learning-C-programming-language)
- [How to Learn C Roadmap](https://www.hoppersroppers.org/roadmap/training/c.html)
- [The Complete Roadmap for C Programming, Everything you need to know.](https://www.linkedin.com/pulse/complete-roadmap-c-programming-everything-you-need-know-muntashir/)
- [Developer Roadmaps](https://roadmap.sh/)
- [https://github.com/kamranahmedse/developer-roadmap](https://github.com/kamranahmedse/developer-roadmap)


Here, a list of the main C components and feature, listed more or less by difficul level (first easier , last more advanced).
Keep in mind that this list if not just by 'topic' but some point are just specified to take your attention of a particula feature
of the language that is controversial, different, unexpected or simply requires more attention (hence, need to be studied!).

Also, is not **EVERYTHING** specific to the *C* language, some stuff are just some generic *Software Developer* stuff but are required to 
move forward with the language, or, especially if you have experience with other programing languages, to see how is done in C rather. 


Basic
-----

- Install C
- Compiler 1
    - #include 
    - gcc : C standard Compiler
    - how compile programm
    - C versions / standars 
- Data Types 1
    - int
        - short
        - long 
        - long long
        - uint8_t
        - uint16_t
        - uint32_t
        - uint64_t
    - char
    - bool
    - Typecasting
    - String interpolation
- Variables 1
    - const
- Operators
    - arithmetic operators
    - relational operators
    - logic operators
    - assignment operators
    - bitwise operators
    - sizeof
- Control flow
    - Conditionals 
        - if , else if, else
        - switch
        - ternary opertor
    - Loops
        - while
        - do while
        - for loop`
    - continue, break 
    - go to 
- Functions 1
    - functions
    - parameters and how they work with C
    - function invocation
    - exit

Intermediate
------------

- [Keywords in C](https://www.programiz.com/c-programming/list-all-keywords-c-language)
- Functions 2
    - Functions prototypes
    - recursions
    - 
- Scopes
- Data Structures
    - Strings
    - Arrays
        - multidimensional arrays
        - matrix array
        - array subscript operator.
        - array | subscript.
    - Linked List
    - Stack
    - Queue
- I/O Stream
    - FILE
    - stdin
    - stderr
    - print on console
    - input/output and closing file
    - printf
    - perror
    - FIles
    - directories
    - streams
    - buffers
- Variable 2
    - storage classes
        - auto
        - extern
        - static 
        - register
    - Symbolic constants
        - __LINE__ | __FILE__ | __DATE__ | __TIME__ | __STDC__
- Data Types 2
    - pointers
        - double pointer
        - function pointer
    - struct (structure)
        - Access operator '.'  [struct].[proprerty]
        - Access operator pointer '->'  [struct]->[proprerty]
    - union 
    - enum 
    - size_t [What is size_t in C?](https://stackoverflow.com/questions/2550774/what-is-size-t-in-c)
    - typedef
- C Standard Library [C++ Standard Library headers](https://en.cppreference.com/w/cpp/header)
    - First to learn
        - <stdio.h>
        - <stdlib.h>
        - <string.h>
        - <ctype.h>
        - <time.h>
        - <stddef.h>
        - <stdint.h>
        - <stdarg.h>
        - <stdbool.h>
        - <errno.h>
    - Main by topic
        - Concepts library
        - Coroutines library
        - Utilities library
        - Dynamic memory management 
        - Numeric limits 
        - Error handling
        - Strings library
        - Containers library
        - Iterators library
        - Ranges library
        - Algorithms library
        - Numerics library
        - Localization library
        - Input/output library
        - Filesystem library
        - Regular Expressions library
        - Atomic Operations library
        - Thread support library
        - C compatibility headers
- Error Handling
    - perror
    - error log
- Memory
    - Dynamic Memory Allocation
        - malloc
        - calloc
        - realloc
        - free
        - bfree
- Compiler 2
    - c header files [file].h
    - GNU (just understand what is it, no need to go deep in this)
    - [GCC Command-Line Options](http://tigcc.ticalc.org/doc/comopts.html)
    - gdb : C standard debugger
    - CMAKE
    - Make
- Preprocessor    
    - #define
    - #undef
    - #if
    - #else
    - #endif
    - #ifdef
    - #ifndev 
    - #iddef
    - macros
        -  EXIT_SUCCESS
        - EXIT_FAILURE
        - [Variadic macro in the C preprocessor](https://en.wikipedia.org/wiki/Variadic_macro_in_the_C_preprocessor)
        - [ellipsis operator](https://stackoverflow.com/questions/3792761/what-is-ellipsis-operator-in-c)
    - #pragma
    - __attribute__
    - Preprocessor Predefined symbolic constants
    - [Directive (programming)](https://en.wikipedia.org/wiki/Directive_(programming))

- Command line arguments
- Generics
    - _Generic
    - [Syntax and Sample Usage of _Generic in C11](https://stackoverflow.com/questions/9804371/syntax-and-sample-usage-of-generic-in-c11)


Advanced
--------

- Debugging
- Testing    
- Buffers
    - Circular Buffer
- UNIX System interface : https://clc-wiki.net/wiki/K%26R2_solutions:Chapter_8
- Compiler 3
    - How Compiler works
    - Heap
    - Stack



Others not C specific
---------------------

*Next, also you could learn the following, is not a C specific thing but rather, a general Software engineer/developer related.*


- Software development method(SDM)
    - Specification needs
    - Problem Analysis
    - Design and Algorithms representation
    - Implementation
    - Testing and verification
    - Documentation
- Testing
    - unittest
    - integration tests
    - e2e testing
    - TDD (Test-driven development)

