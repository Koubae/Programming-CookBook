#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int dividend = 20;
    int divisor = 0;
    int quotient;

    if (divisor == 0) {
        fprintf(stderr, "Division by zero! Exiting...\n");
        //exit(-1);
        exit(EXIT_FAILURE);
    }

    quotient = dividend / divisor;
    fprintf(stdout, "Value of quotient : %d\n", quotient );
    //return 0;
    exit(EXIT_SUCCESS);
}