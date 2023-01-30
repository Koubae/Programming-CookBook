#include <stdio.h>

extern int globalInt;

void printSource2()
{
    printf("source2.c,  globalInt=%d\n ", globalInt);
}