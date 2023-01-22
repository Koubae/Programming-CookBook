/**
 * @credit: https://stackoverflow.com/a/64044782/13903942
 * 
 * C print function similar to Python
 * 
 * The difference is that pyhton print function adds alwats a new line (whereas, C does not)
 * Also, you can pass all possible variable in python (int, float, dict, tuple) while in c is strongly typed
 * 
 *  X-macros to have really powerful constructs easily
*/

#include <stdio.h>


// Easily add new supported types here

#define PRINT_FORMATS(X) \
    X(double, "%f")    \
    X(float,  "%f")    \
    X(char *, "%s")    \
    X(int,    "%d")

#define GENERIC_ENTRY(type, format), type: format " "

#define print(X)                        \
    printf(_Generic((X)             \
        PRINT_FORMATS(GENERIC_ENTRY)    \
    ), (X))


int main(int argc, char **argv)
{
    print(21);
    print(21.5);
    print(21.5f);
    print("Hello world");

    return 0;
}