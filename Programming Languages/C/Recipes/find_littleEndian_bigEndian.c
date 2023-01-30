#include <stdio.h>
// @ref: https://en.cppreference.com/w/c/language/object#Strict_aliasing
int main(void)
{
    int i = 7;
    char* pc = (char*)(&i);
    
    if (pc[0] == '\x7') { // aliasing through char is ok
        puts("This system is little-endian");
    } else {
        puts("This system is big-endian");
    }

    return 0;
}