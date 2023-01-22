/**
 * @credit: https://stackoverflow.com/a/64044782/13903942
 * 
 * C print function similar to Python
 * 
 * The difference is that pyhton print function adds alwats a new line (whereas, C does not)
 * Also, you can pass all possible variable in python (int, float, dict, tuple) while in c is strongly typed
 * 
*/

#include <stdio.h>

#define print(X) printf(_Generic((X),    \
                        double: "%f \n", \
                        float:  "%f \n", \
                        char *: "%s \n", \
                        int:    "%d \n"  \
                ), (X));

int main(int argc, char **argv) 
{
    print(21);
    print(21.5);
    print(21.5f);
    print("Hello world");  

    return 0;
}
