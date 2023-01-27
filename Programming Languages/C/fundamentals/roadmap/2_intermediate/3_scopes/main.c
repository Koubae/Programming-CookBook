#include <stdio.h>

// Also see: Scope - cppreference.com : https://en.cppreference.com/w/c/language/scope for more details


int sumGlobal = 0;

int addNumbers(int a, int b)
{
    int sum = a + b; // local scope
    return sum;
}


void addNumbersGlobal(int a, int b)
{
    sumGlobal = sumGlobal + a + b;
}

int main(void)
{
    int result = addNumbers(5, 5);
    // printf("sum = %d\n", sum); error. sum is not declared inside main
    int sum = 20; // local scope

    printf("sum = %d\n", sum);
    printf("result = %d\n", result);

    // using global variables
    printf("sumGlobal = %d\n", sumGlobal);
    addNumbersGlobal(5, 5);
    printf("sumGlobal = %d\n", sumGlobal);

    addNumbersGlobal(5, 5);
    printf("sumGlobal = %d\n", sumGlobal);

    return 0;
}