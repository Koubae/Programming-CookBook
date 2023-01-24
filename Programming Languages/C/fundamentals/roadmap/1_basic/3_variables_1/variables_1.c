#include <stdio.h>


// @ref https://en.cppreference.com/w/c/language/const
/*
In a function declaration, the keyword const may appear inside the square brackets 
that are used to declare an array type of a function parameter. 
It qualifies the pointer type to which the array type is transformed.

The following two declarations declare the same function: 
*/
void f1(double x[const], const double y[const]);
void f2(double * const x, const double * const y);

// macro definition
#define X 30;  // NOTE Avoid do this, thi is a macro handle by prepocessor use const instead! @see https://stackoverflow.com/a/6274042/13903942
// global integer constant
const int Y = 10;


int main(void)
{   
    const int integerConst = 1;
    // integerConst = 2; error: assignment of read-only variable ‘integerConst’

    // Using Pointers

    int integer = 10;

    // const pointer
    const int *pInteger = &integer;
    printf("Pointer(value=%d, pointer=%p))\n", *pInteger, pInteger);
    //*pInteger = 100; error: assignment of read-only location ‘*pInteger’

    // @ref https://en.cppreference.com/w/c/language/const

    const int n = 1; // object of const type
    //n = 2; // error: the type of n is const-qualified
    
    int x = 2; // object of unqualified type
    const int* p = &x;
    //*p = 3; // error: the type of the lvalue *p is const-qualified
    
    struct {int a; const int b; } s1 = {.b=1}, s2 = {.b=2};
    //s1 = s2; // error: the type of s1 is unqualified, but it has a const member 

    // A member of a const-qualified structure or union type acquires the qualification of the type it belongs to (both when accessed using the . operator or the -> operator). 
    struct s { int i; const int ci; } s;
    // the type of s.i is int, the type of s.ci is const int
    const struct s cs;
    // the types of cs.i and cs.ci are both const int


    typedef int A[2][3];
    const A a = {{4, 5, 6}, {7, 8, 9}}; // array of array of const int
    int* pi = a[0]; // Error: a[0] has type const int*
    void *unqual_ptr = a; // OK until C23; error since C23
    // Notes: clang applies the rule in C++/C23 even in C89-C17 modes


    const int* p1 = (const int[]){1, 2, 3};
    const int* p2 = (const int[]){2, 3, 4}; // the value of p2 may equal p1+1
    _Bool b = "foobar" + 3 == (const char[]){"bar"}; // the value of b may be 1

    int* p3 = 0;
    const int* cp2 = p3; // OK: adds qualifiers (int to const int)
    //p = cp; // Error: discards qualifiers (const int to int)
    p3 = (int*)cp2; // OK: cast

    return 0;

}