C | Fundamentals
----------------

*Fundamental stuff about the C language*

#### Based on **[Roadmap](../roadmap.md)**

- [Features](#features)
- [Data Types](#data-types)
- [Operators](#operators)
- [Variables](#variables)
    - [variable scope](#variable-scope)
- [Conditionals](#conditionals)
- [Loops](#loops)
- [Functions | Subroutines](#functions--subroutines)
- [Type definitions | Enums](#type-definitions--enum)
- [Structures | struct](#structures--struct)
- [The Preprocessor CPP](#the-preprocessor-cpp)
- [typedef](#typedef)
- [I/O | Input & Output](#io--input--output)
- [Headers files](#headers-files)
- [Command Line Parameters](#command-line-parameters)


Features
---------

- char
- int
- short
- long
- Pointer
- subroutines 
- declarations
- Structures struct
- enum 
- typedef
- Macros
- #ifndev #iddef
- Preprocessor 
- Preprocessor Predefined symbolic constants
- [Directive (programming)](https://en.wikipedia.org/wiki/Directive_(programming))
- Struct
- [Bit Fields --WIKI--](https://en.wikipedia.org/wiki/Bit_field)
- [Bit Fields tutorialspoint.com](https://www.tutorialspoint.com/cprogramming/c_bit_fields.htm)
- EOF (End of File)
- [Type Casting](https://www.tutorialspoint.com/cprogramming/c_type_casting.htm)  | type-conversion
- array subscript operator.
- array | subscript.


Data Types
---------

*C standard Data Types*

- [tutorialspoint.com](https://www.tutorialspoint.com/cprogramming/c_data_types.htm)
- [Member access operators](https://en.cppreference.com/w/c/language/operator_member_access)
- [Implicit conversions](https://en.cppreference.com/w/cpp/language/implicit_conversion)
- [Explicit type conversion](https://en.cppreference.com/w/cpp/language/explicit_cast)

The char type is commonly used to store letters of the ASCII chart, but it can be used to hold small integers from -128 to 127. It takes at least 1 byte.

- int takes at least 2 bytes. short takes at least 2 bytes. long takes at least 4 bytes.

*Guaranteed that short is not longer than int. And we're guaranteed long is not shorter than int.*

- unsigned **char** will range from 0 to at least 255
- unsigned **int** will range from 0 to at least 65,535
- unsigned **short** will range from 0 to at least 65,535
- unsigned **long** will range from 0 to at least 4,294,967,295

#### Integers


#### Floating Points

- float
- double
- long double

The minimum requirements for any C implementation is that float can represent a range between 10^-37 and 10^+37, and is typically implemented using 32 bits. double can represent a bigger set of numbers. long double can hold even more numbers.

A double number is represented in 64 bits, with a precision of 53 significant bits. 11 bits are used to encode the exponent.

The type long double is represented in 80 bits, has a precision of 64 significant bits. 15 bits are used to encode the exponent.

#### Strings


```


char name[7] = "Federi";
printf("%s", name);

```

"Federi" is 6 chars long, but I defined an array of length 7, This is because the last character in a string must be a  0 value, the string terminator, and we must make space for it.

##### #include <string.h>, have access to:

- **strcpy(**) to copy a string over another string
- **strcat()** to append a string to another string
- **strcmp()** to compare two strings for equality
- **strncmp()** to compare the first n characters of two strings
- **strlen()** to calculate the length of a string

##### String Interpolation

- [cppreference](https://en.cppreference.com/w/c/io/fprintf)

- %c for a `char`
- %s for a `char`

- %hd short `int`
- %d for a `int`
- %u `unsigned int`
- %li `long int`
- %lii `long long int`
- %lu `unisigned long int`
- %llu `unisigned long long int`

- %f for `float`
- %lf `double`
- %LF `long double`

- %G --> converts **floating-point** number to **decimal or decimal exponent** notation depending on the value and the precision. converts floating-point number to decimal or decimal exponent notation depending on the value and the precision. 

- %p pointers `&var` 

##### Integers Interpolation


- **x** prints an unsigned number in hexadecimal.
- **o** prints an unsigned number in octal.
- **u** prints an unsigned number in decimal.
- **d** prints a signed number in decimal.
- **i** prints a signed number in decimal.



#### Pointers

A pointer is the address of a block of memory that contains a variable.

- [Concept & Description ](https://www.tutorialspoint.com/cprogramming/c_pointers.htm)

* is called the **dereference operator** (when working with pointers). It operates on a pointer and gives the value stored in that pointer.

> This is equivalent to

```
int *p = &c;

```
> THIS

```
int *p:
p = &c;
// or
int* p = &c;
```

```

//Syntax
int* var;

int *var;

int * var;

int* var1, var2;  /var2 is NOT a pointer but a normal var 

int age = 37;
printf("%p", &age); /* 0x7ffeef7dcb9c */

//  assign the address to a variable:
int *address = &age;


// use the pointer operator * to get the value of the variable an address is pointing to

int* pc, c;
c = 5;
pc = &c;
printf("%d", *pc);   // Output: 5



// use a pointer to initialize the value

int age;
int *address = &age;
*address = 37;
printf("%u", *address);


// The prices variable is actually a pointer to the first item of the array. 
int prices[3] = { 5, 4, 3 };
printf("%u", *prices); /* 5 */

//  we can get the second item by adding 1 to the prices pointer 
printf("%u", *(prices + 1)); /* 4 */


```

#### OTHER C TYPES

- uint8_t
- uint16_t
- uint32_t
- uint64_t

- [C - Type - What are uint8_t, uint16_t, uint32_t and uint64_t? ](https://www.badprog.com/c-type-what-are-uint8-t-uint16-t-uint32-t-and-uint64-t)

- size_t
- [What is size_t in C?](https://stackoverflow.com/a/2550799/13903942)


Operators
---------

- arithmetic operators
- comparison operators
- logical operators
- compound assignment operators
- bitwise operators
- pointer operators
- structure operators
- miscellaneous operators

**Increment and Decrement on place operator!**

```

int a = 2;
int b;
b = a++ /* b is 2, a is 3 */
b = ++a /* b is 4, a is 4 */

```


#### Unary expressions

```

Operator     Meaning
========     =======
   &         Address-of; value is the location of the operand
   *         Contents-of; value is what is stored at the location
   -         Negation
   +         Value-of operator
   !         Logical negation ( (!E) is equivalent to (0==E) )
   ~         Bit-wise complement
   
```

#### The ternary operator


```

// Syntax
<condition> ? <expression> : <expression>

a ? b : c

```

#### Operator precedence


In order from less precedence to more precedence, we have:

- the = assignment operator
- the + and - **binary** operators
- the * and / operators
- the + and - **unary** operators
- Parentheses  => ()

Operators also have an associativity rule, which is always left to right except for the unary operators and the assignment.



Variables
---------

#### Constants 

Constants Variables are written Upper Case for convention.

```
const int AGE = 37;

//Another way to define a constant

#define AGE 37

```

#### Storage Classes

- auto
- register
- static
- extern

##### **auto**

The auto storage class is the default storage class for all local variables.

##### **register**


The register should only be used for variables that require quick access such as counters. It should also be noted that defining 'register' does not mean that the variable will be stored in a register. It means that it MIGHT be stored in a register depending on hardware and implementation restrictions.

##### **static**

In C programming, when static is used on a global variable, it causes only one copy of that member to be shared by all the objects of its class.

##### **extern**

The extern storage class is used to give a reference of a global variable that is visible to ALL the program files


###### register keyword


The register keyword is used to declare register variables. Register variables were supposed to be faster than local variables.

However, modern compilers are very good at code optimization, and there is a rare chance that using register variables will make your program faster.

Unless you are working on embedded systems where you know how to optimize code for the given application, there is no use of register variables.

Register is a storage class, and C doesn’t allow multiple storage class specifiers for a variable. So, register can not be used with static . Try below program.

Register can only be used within a block (local), it can not be used in the global scope (outside main).

```

#include<stdio.h> 
  
int main() 
{ 
    int i = 10; 
    register int* a = &i; 
    printf("%d", *a); 
    getchar(); 
    return 0; 
} 

```

###### static variable

- [What are the default values of static variables in C?](https://www.geeksforgeeks.org/g-fact-53/)

The value of a static variable persists until the end of the program.
Static variables (like global variables) are initialized as 0 if not initialized explicitly. 

```
Syntax
static [data_type] [var_name] = [var_value]; 

static int i;
```



#### Variable scope

- global variables
- local variables

Global variables are accessible from any function of the program, and they are available for the whole execution of the program, until it ends.

Local variables are declared on the stack, by default, unless you explicitly allocate them on the heap using pointers. But then you have to manage the memory yourself.


- Static variables

Inside a function, you can initialize a static variable using the static keyword.
**"inside a function"** because global variables are static by default, so there's no need to add the keyword.

A static variable is initialized to 0 if no initial value is specified, and it retains the value across function calls.

```

// Will get always 1, because the variable is  re-initialized to 0 on every single function call.
int incrementAge() {
  int age = 0;
  age++;
  return age;
}


int incrementAge() {
  static int age = 0;
  age++;
  return age;
}
printf("%d\n", incrementAge());
printf("%d\n", incrementAge());
printf("%d\n", incrementAge());
1
2
3


// This is also valid
int incrementAge() {
  static int ages[3];
  ages[0]++;
  return ages[0];
}


```


Conditionals
------------

- If | else if | else Syntax

```

int a = 1;

if (a == 2) {
  /* do something */
} else if (a == 1) {
  /* do something else */
} else {
  /* do something else again */
}

```

- Switch Syntax

```

int a = 1;

switch (a) {
  case 0:
    /* do something */
    break;
  case 1:
    /* do something else */
    break;
  case 2:
    /* do something else */
    break;
  default:
    /* handle all the other cases */
    break;
}


```


Loops
-----

- For loops

```

for (int i = 0; i <= 10; i++) {
  /* instructions to be repeated */
}

// Start reducing rather than increasing

for (int i = 10; i > 0; i--) {
  /* instructions to be repeated */
}


// Increment by 2 or more value

for (int i = 0; i < 1000; i = i + 30) {
  /* instructions to be repeated */
}

// Break Statement

for (int i = 0; i <= 10; i++) {
  if (i == 4 && someVariable == 10) {
    break;
  }
}


```

- While loops

```

int i = 0;

while (i < 10) {
  /* do something */

  i++;
}

// Break Statement

int i = 0;
while (1) {
  /* do something */

  i++;
  if (i == 10) break;
}

```

- do while loops.

```

int i = 0;

do {
  /* do something */

  i++;
} while (i < 10);


```


- goto statement

The goto statement allows us to transfer control of the program to the specified label.

```
goto label;
... .. ...
... .. ...
label: 
statement;

```

#### Arrays

Every value in the array, in C, must have the same type. This means you will have arrays of int values, arrays of double values, and more.

You must always specify the size of the array. C does not provide dynamic arrays out of the box.

```

// Define an Array
int prices[5];

const int SIZE = 5;
int prices[SIZE];


// Assign Value after definition
int prices[5];

prices[0] = 1;
prices[1] = 2;
prices[2] = 3;
prices[3] = 4;
prices[4] = 5;

// Using a Loop

int prices[5];

for (int i = 0; i < 5; i++) {
  prices[i] = i + 1;
}


```


Functions | Subroutines
----------------------------

If the function has no return value, you can use the keyword void before the function name. Otherwise you specify the function return value type (int for an integer, float for a floating point value, const char * for a string, etc).

**You cannot return more than one value from a function.**

**You can't define a default value for a parameter. C++ can do that (and so Arduino Language programs can), but C can't.**

A variable is created at the point of invocation of the function and is destroyed when the function ends. It's not visible from the outside.

Inside a function, you can call the function itself hence you can have recursions in C.


```
void doSomething(int value) {
   /* ... */
}
doSomething(3);

int doSomething(int value1, int value2) {
  printf("%d %d\n", value1, value2);
  return 1;
}

```

##### Function prototype


```
// Syntax 
returnType functionName(type1 argument1, type2 argument2, ...);

#include <stdio.h>
int addNumbers(int a, int b);         // function prototype

int main()
{
    int n1,n2,sum;

    printf("Enters two numbers: ");
    scanf("%d %d",&n1,&n2);

    sum = addNumbers(n1, n2);        // function call
    printf("sum = %d",sum);

    return 0;
}

int addNumbers(int a, int b)         // function definition   
{
    int result;
    result = a+b;
    return result;                  // return statement
}
```


Type definitions | enum 
-----------------------

Starting from the built-in C types, we can create our own types, using this syntax:
**The new type we create is usually, by convention, uppercase**

```
enum typedef
typedef existingtype NEWTYPE
typedef int NUMBER

NUMBER one = 1;
```

- Enumerated types

Using the typedef and enum keywords we can define a type that can have either one value or another.

```

typedef enum {
  //...values
} TYPENA

typedef enum {
  true,
  false
} BOOLEAN;

//  define weekdays


typedef enum {
  monday,  
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday
} WEEKDAY;


```

simple program that uses this enumerated type


```

#include <stdio.h>

typedef enum {
  monday,  
  tuesday,
  wednesday,
  thursday,
  friday,
  saturday,
  sunday
} WEEKDAY;

int main(void) {
  WEEKDAY day = monday;

  if (day == monday) {
    printf("It's monday!"); 
  } else {
    printf("It's not monday"); 
  }
}

```


Structures  | struct
--------------------


Using the struct keyword we can create complex data structures using basic C types.
A structure is a collection of values of different types. Arrays in C are limited to a type, so structures can prove to be very interesting in a lot of use cases.


It's important to note that structures are **passed by copy**, unless of course you pass a pointer to a struct, in which case it's passed by reference.

- [Opaque C structs: various ways to declare them](https://stackoverflow.com/questions/3965279/opaque-c-structs-various-ways-to-declare-them)

**Designated Initializers**
- [Designated Initializers GNU.org](https://gcc.gnu.org/onlinedocs/gcc/Designated-Inits.html)
- [How to initialize a struct in accordance with C programming language standards SOO](https://stackoverflow.com/questions/330793/how-to-initialize-a-struct-in-accordance-with-c-programming-language-standards)
- []()
- []()


There are two types of operators used for accessing members of a structure.

1. `.` - Member operator
2. `->` - Structure pointer operator (will be discussed in the next tutorial)


syntax 
```
struct <structname> {
  //...variables
};

struct person {
  int age;
  char *name;
};


// You can declare variables that have as type that structure by adding them after the closing curly bracket
struct person {
  int age;
  char *name;
} mystruct;


// multiple ones
struct person {
  int age;
  char *name;
} mystruct, manystructs[20];


//  declare variables later on
struct person {
  int age;
  char *name;
};

struct person mystruct;


//  initialize a structure at declaration time
struct person {
  int age;
  char *name;
};

struct person fede = { 37, "Federico" };

//  access the values in it using a dot
struct person {
  int age;
  char *name;
};

struct person fede = { 37, "Federico" };
printf("%s, age %u", fede.name, fede.age);

// change the values using the dot syntax
struct person {
  int age;
  char *name;
};

struct person fede = { 37, "Federico" };

fede.age = 38;

```

- Using typedef we can simplify the code when working with structures.

```

typedef struct {
  int age;
  char *name;
} PERSON;

PERSON fede;

// initialize them at declaration 
PERSON fede = { 37, "Flavio" };

```


The preprocessor CPP
--------------------

The preprocessor is a tool that helps us a lot when programming with C. It is part of the C Standard, just like the language, the compiler, and the standard library.

It parses our program and makes sure that the compiler gets all the things it needs before going on with the process.

it looks up all the **header files** you include with the #include directive.

It also looks at **every constant** defined using #define and substitutes it with its actual value.

- [Header Files](https://gcc.gnu.org/onlinedocs/cpp/Header-Files.html#Header-Files)
- [Macros](https://gcc.gnu.org/onlinedocs/cpp/Macros.html#Macros)
- [Pragmas](https://gcc.gnu.org/onlinedocs/cpp/Pragmas.html#Pragmas)


- [tutorialspoint.com](https://www.tutorialspoint.com/cprogramming/c_preprocessors.htm)

This is useful if you pass the ```-DDEBUG flag``` to the gcc compiler at the time of compilation.

```
#ifdef DEBUG
   /* Your debugging statements here */
#endif
```

### Common uses of C preprocessor are:


- Including Header Files: #include   

- Symbolic constants

- Macros

- Conditional Compilation

- Predefined Macros

### Conditionals

```

#include <stdio.h>

const int DEBUG = 0;

int main(void) {
#if DEBUG == 0
  printf("I am NOT debugging\n");
#else
  printf("I am debugging\n");
#endif
}

```

### If defined  #iddef

#ifndev 
#iddef

```

#include <stdio.h>
#define VALUE 1

int main(void) {
#ifdef VALUE
  printf("Value is defined\n");
#else
  printf("Value is not defined\n");
#endif
}

```

We also have **#ifndev** to check for the opposite (macro not defined).

We can also use #if defined and #if !defined to do the same task.

common to wrap some block of code into a block

```
#if 0

#endif


//  temporarily prevent it from running, or to use a DEBUG symbolic constant
#define DEBUG 0

#if DEBUG
  //code only sent to the compiler
  //if DEBUG is not 0
#endif


```


##### Symbolic constants

Symbolic constants are very useful because we can give names to values without creating variables at compilation time.

We can define a symbolic constant:


```

#define VALUE 1
#define PI 3.14
#define NAME "Programmer"

```

##### Macros

With #define we can also define a macro. The difference between a macro and a symbolic constant is that a macro can accept an argument and typically contains code, while a symbolic constant is a value


The big difference with functions is that macros do not specify the type of their arguments or return values, which might be handy in some cases.


```

//  use it in our code like this
#define POWER(x) ((x) * (x))
printf("%u\n", POWER(4)); //16

```



##### Predefined symbolic constants you can use

The preprocessor also defines a number of symbolic constants you can use, identified by the 2 underscores before and after the name, including:

- __LINE__ translates to the current line in the source code file
- __FILE__ translates to the name of the file
- __DATE__ translates to the compilation date, in the Mmm gg aaaa format
- __TIME__ translates to the compilation time, in the hh:mm:ss format


typedef
-------

##### typedef vs #define

#define is a C-directive which is also used to define the aliases for various data types similar to typedef but with the following differences −

> **typedef** is limited to giving symbolic names to types only where as **#define** can be used to define alias for values as well, q., you can define 1 as ONE etc.

> **typedef** interpretation is performed by the *compiler* whereas **#define** statements are processed by the *pre-processor.*


I/O | Input & Output
--------------------

**3 kinds of I/O streams in C:**

- stdin (standard input)
- stdout (standard output)
- stderr (standard error)

#### #include <stdio.h>, have access to:

- printf()
- fprintf()
- scanf() This function is used to get a value from the user, from the command line.

- sscanf()
- fgets()

```
scanf("%d", &age);

// string name is a pointer to the first character, so you don't need the & character before it
char name[20];
scanf("%s", name);

```


Headers files
-------------

You can move parts of a program to a separate file. Then you create a header file.

A header file looks like a normal C file, except it ends with .h instead of .c. Instead of the implementations of your functions and the other parts of a program, it holds the **declarations**.

**#include is a preprocessor directive.**

The preprocessor goes and looks up the stdio.h file in the standard library because you used brackets around it. To include your own header files, you'll use quotes, like this:

```
#include "myfolder/myfile.h"
```

This program calculates the years since a given year

```

#include <stdio.h>

int calculateAge(int year) {
  const int CURRENT_YEAR = 2020;
  return CURRENT_YEAR - year;
}

int main(void) {
  printf("%u", calculateAge(1983));
}

// move the calculateAge function to a separate file
// create a calculate_age.c file
int calculateAge(int year) {
  const int CURRENT_YEAR = 2020;
  return CURRENT_YEAR - year;
}
int calculateAge(int year);

```

Main.c File remove the calculateAge() function definition, and we can import calculate_age.h, which will make the calculateAge() function available

```
#include <stdio.h>
#include "calculate_age.h"

int main(void) {
  printf("%u", calculateAge(1991));
}

```


Command line parameters
-----------------------

```

int main (int argc, char *argv[])

```

**argc** is an integer number that contains the number of parameters that were provided in the command line.

**argv** is an array of strings.


Program that prints the arguments it receives

```

#include <stdio.h>

int main (int argc, char *argv[]) {
  for (int i = 0; i < argc; i++) {
    printf("%s\n", argv[i]);
  }
}
 pass some random parameters, like this: ./hello a b c
```
