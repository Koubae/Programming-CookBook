#include <stdio.h>

int main(void) {
    printf("Char Size: %lu bytes\n", sizeof(char));
    printf("Int Size: %lu bytes\n", sizeof(int));
    printf("Short Size: %lu bytes\n", sizeof(short));
    printf("Long Size: %lu bytes\n", sizeof(long));
    printf("Float Size: %lu bytes\n", sizeof(float));
    printf("Double Size: %lu bytes\n", sizeof(double));
    printf("Long Double size: %lu bytes\n", sizeof(long double));
}

//Char Size: 1 bytes
//Int Size: 4 bytes
//Short Size: 2 bytes
//Long Size: 4 bytes
//Float Size: 4 bytes
//Double Size: 8 bytes
//Long Double size: 16 bytes