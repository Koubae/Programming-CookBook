#include <stdio.h>

void print(char values[]);  // function prototype
int sum(int a, int b);      // function prototype

void main(void)
{
    // ------------ Prototype
    print("Hello world");


}


// ------------ Prototype
void print(char values[])   // function declaration
{
    printf("%s\n", values);

    int total = sum(10, 5);
    printf("Total: %d\n", total);

}

int sum(int a, int b)   // function declaration
{
    return a + b;
}
