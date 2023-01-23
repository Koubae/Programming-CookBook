C Roadmap - Compiler 1
======================

include 
-------

- [Include Syntax](https://gcc.gnu.org/onlinedocs/cpp/Include-Syntax.html)
- [#include directive](https://www.techonthenet.com/c_language/directives/include.php)
- [C - Header files](https://www.tutorialspoint.com/cprogramming/c_header_files.htm)
- [#include directive (C/C++)](https://learn.microsoft.com/en-us/cpp/preprocessor/hash-include-directive-c-cpp?view=msvc-170)

For now, just know that `#include` is just a way for `C` to add other `C` files, modules, packages, headers files (special C files), frameworks into the 
current `C` file. What the compiler does during the pre processor is literally **Copy and paste** the included file/header.

The preprocessor stops searching as soon as it finds a file that has the given name. If you enclose a complete, unambiguous path specification for the include file between double quotation marks (" "), the preprocessor searches only that path specification and ignores the standard directories.

**There are 2 variants**

```c
// Is used for system header files
#include <file>
// header files of your own program.
#include "file"

```

Put it simply, the `<file>` variant is for standard library headers, (the one that you won't touch and are already created).
The `"file"` variant, is for header that **You create**.


#### Most used C standard library Header files (but there are many many more)

<table class="std_table">
    <thead>
    <tr>
      <th>Header File</th>
      <th>Type of Functions</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td><a href="/c_language/standard_library_functions/assert_h/index.php">&lt;assert.h&gt;</a></td>
      <td>Diagnostics Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/ctype_h/index.php">&lt;ctype.h&gt;</a></td>
      <td>Character Handling Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/locale_h/index.php">&lt;locale.h&gt;</a></td>
      <td>Localization Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/math_h/index.php">&lt;math.h&gt;</a></td>
      <td>Mathematics Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/setjmp_h/index.php">&lt;setjmp.h&gt;</a></td>
      <td>Nonlocal Jump Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/signal_h/index.php">&lt;signal.h&gt;</a></td>
      <td>Signal Handling Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/stdarg_h/index.php">&lt;stdarg.h&gt;</a></td>
      <td>Variable Argument List Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/stdio_h/index.php">&lt;stdio.h&gt;</a></td>
      <td>Input/Output Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/stdlib_h/index.php">&lt;stdlib.h&gt;</a></td>
      <td>General Utility Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/string_h/index.php">&lt;string.h&gt;</a></td>
      <td>String Functions</td>
    </tr>
    <tr>
      <td><a href="/c_language/standard_library_functions/time_h/index.php">&lt;time.h&gt;</a></td>
      <td>Date and Time Functions</td>
    </tr>
    </tbody>
  </table>


gcc : C standard Compiler
-------------------------

The GNU Compiler Collection, commonly known as GCC, is a set of compilers and development tools available for Linux, Windows, various BSDs, and a wide assortment of other operating systems. It includes support primarily for C and C++ and includes Objective-C, Ada, Go, Fortran, and D. The Free Software Foundation (FSF) wrote GCC and released it as completely free (as in libre) software.

- [GCC, the GNU Compiler Collection](https://gcc.gnu.org/)
- [GCC Releases](https://gcc.gnu.org/releases.html)
- [GNU Compiler Collection - Wikipedia](https://en.wikipedia.org/wiki/GNU_Compiler_Collection)


How compile programm
--------------------


Compiler converts a C program into an executable. There are four phases for a C program to become an executable: 

- Pre-processing
- Compilation
- Assembly
- Linking

```bash 
# generate all intermediate files of the compilation
gcc -Wall -save-temps filename.c –o filename 

```



C versions / standars
---------------------

```
__STDC_VERSION__
```

- C89: 1989
- C90: 1990
- C95: 1995
- C99: 1999
- C11: 2011
- C17: 2018
- C23: 2022


- [GCC Releases](https://gcc.gnu.org/releases.html)
- [The GNU C Library Release Timeline](https://sourceware.org/glibc/wiki/Glibc%20Timeline)
- [The GNU C Library (glibc)](https://www.gnu.org/software/libc/)
- [History of C](https://en.cppreference.com/w/c/language/history)

- [Language Standards](https://sourceforge.net/p/predef/wiki/Standards/)
- [How can I know the version of c?](https://stackoverflow.com/questions/36662063/how-can-i-know-the-version-of-c)
- [C Programming Language Version History](https://developerinsider.co/c-programming-language-version-history/)
- [List of C-family programming languages](https://en.wikipedia.org/wiki/List_of_C-family_programming_languages)
- [C Standard library features - microsoft](https://learn.microsoft.com/en-us/cpp/overview/visual-cpp-language-conformance?view=msvc-170#c-standard-library-features-1)





