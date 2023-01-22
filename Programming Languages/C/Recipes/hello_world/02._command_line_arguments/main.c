/*
@credit: https://stackoverflow.com/a/5157549/13903942

Loop through Command line arguments

*/
#include <stdio.h>


int main(int argc, char **argv) 
{

    printf("Called %s with %d arguments\n", argv[0], argc);
    for (int i = 0; i < argc; ++i) {    
        if (i == 0) continue; // First argument is the script/executable name
        printf("argc[%d]: %s\n", i, argv[i]);
    }

    return 0;
}