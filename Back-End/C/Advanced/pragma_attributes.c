// ----------- WEAK SYMBOL
/*
    GNU --> https://gcc.gnu.org/onlinedocs/gcc-4.7.2/gcc/Function-Attributes.html

    Declaring Attributes of Functions
    https://gcc.gnu.org/onlinedocs/gcc-3.2/gcc/Function-Attributes.html

    Declaring Attributes of Functions
    https://gcc.gnu.org/onlinedocs/gcc-4.7.2/gcc/Function-Attributes.html

    Stack Overflow 
    __attribute__((weak)) and static libraries
    https://stackoverflow.com/questions/51656838/attribute-weak-and-static-libraries

    Wikipedia
    https://en.wikipedia.org/wiki/Weak_symbol

    https://www.keil.com/support/man/docs/ARMCC/armcc_chr1359124983745.htm

*/
// Pragma
// function declaration
#pragma weak power2

int power2(int x);

// Attribute
// function declaration
/*
int __attribute__((weak)) power2(int );

  // or

int power2(int x) __attribute__((weak));

// variable declaration;
extern int __attribute__((weak)) global_var;

*/