#include <stdio.h>
#include <stdlib.h>

int sum(int numA, int numB); // Function prototype / declaration


int main(void)
{
    // 1, 2 are called 'arguments'
    int total = sum(1, 2);  // function call / function invocation
    printf("Total %d\n", total);

    // Call all functions registered with `atexit' and `on_exit', 
    // in the reverse of the order in which they were registered,
    // perform stdio cleanup, and terminate program execution with STATUS.
    exit(0); 


    return 0;
}

// numA, numB are called 'parameters'
int sum(int numA, int numB) // function definition
{
    return numA + numB;
}