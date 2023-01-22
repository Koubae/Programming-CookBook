/*
@credit: https://stackoverflow.com/a/5157549/13903942

Loop through Command line arguments (improved)

*/

#include <stdio.h>
#include <string.h>

int main(int argc, char **argv) 
{
    if (argc < 2) {
        printf("No argument supplied, here we should print some help or usage for the user!\n");
        return 1;
    }

    if (strcmp("run", argv[1]) == 0) {

        printf("Firt value is run = %s\n", argv[1]);
    } else {
        printf("First value should be 'run', %s passed\n", argv[1]);
        return 1;
    }

    return 0;

}