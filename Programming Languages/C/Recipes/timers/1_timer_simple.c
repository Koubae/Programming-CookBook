#include <stdio.h>
#include <time.h>


unsigned sink;

int main(void)
{
    clock_t start = clock();

    for (size_t i=0; i < 10000000; i++)
        sink++;
    
    clock_t end = clock();

    double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("For loop took %f seconds to execute \n", cpu_time_used);
    printf("Clock %ld \n", CLOCKS_PER_SEC);
}