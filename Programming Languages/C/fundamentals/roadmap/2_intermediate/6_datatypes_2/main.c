#include <stdio.h>
// @credit: https://en.cppreference.com/w/c/language/pointer

void pointerSyntax();
void pointerToObjects();
void pointerToFunctions();
void pointerToVoid();
void pointerToNull();
int f(int n);

int main(void)
{
    pointerSyntax();

    // pointers to objects
    pointerToObjects();

    // pointers to functions
    pointerToFunctions();

    // pointers to void
    pointerToVoid();

    // pointers to NULL
    pointerToNull();

    return 0;
}


void pointerSyntax()
{
    float *p, **pp; // p is a pointer to float | pp is a pointer to a pointer to float
    int (*fp)(int); // fp is a pointer to function with type int(int)
    int n;
    const int * pc = &n; // pc is a non-const pointer to a const int
    // *pc = 2; // Error: n cannot be changed through pc without a cast
    pc = NULL; // OK: pc itself can be changed
    
    int * const cp = &n; // cp is a const pointer to a non-const int
    *cp = 2; // OK to change n through cp
    // cp = NULL; // Error: cp itself cannot be changed
    
    int * const * pcp = &cp; // non-const pointer to const pointer to non-const int
}

void pointerToObjects()
{
    int n;
    int *np = &n; // pointer to int
    int *const *npp = &np; // non-const pointer to const pointer to non-const int
    
    int a[2];
    int (*ap)[2] = &a; // pointer to array of int
    
    struct S { int n; } s = {1};
    int* sp = &s.n; // pointer to the int that is a member of s

    int a[2];
    int *p = a; // pointer to a[0]
    
    int b[3][3];
    int (*row)[3] = b; // pointer to b[0]

}


void pointerToFunctions()
{

    void (*pf1)(int) = &f;
    void (*pf2)(int) = f; // same as &f

    int (*p)(int) = f;
    int x = p(7);

    int f();
    int (*p)() = f;    // pointer p is pointing to f
    (*p)(); // function f invoked through the function designator
    p();    // function f invoked directly through the pointer

    // pointers to functions whose parameters only differ in their top-level qualifiers are interchangeable: 
    int f(int), fc(const int);
    int (*pc)(const int) = f; // OK
    int (*p)(int) = fc;       // OK
    pc = p;                   // OK
}

void pointerToVoid()
{
    // Pointers to void are used to pass objects of unknown type, which is common in generic interfaces: malloc returns void*,
    // qsort expects a user-provided callback that accepts two const void* arguments. pthread_create expects a user-provided callback that accepts and returns void*. 
    // In all cases, it is the caller's responsibility to convert the pointer to the correct type before use. 
    int n=1, *p=&n;
    void* pv = p; // int* to void*
    int* p2 = pv; // void* to int*
    printf("%d\n", *p2); // prints 1
}

void pointerToNull()
{
    /*
    Pointers of every type have a special value known as null pointer value of that type.
     A pointer whose value is null does not point to an object or a function (dereferencing a null pointer is undefined behavior),
      and compares equal to all pointers of the same type whose value is also null.

    To initialize a pointer to null or to assign the null value to an existing pointer, a null pointer constant 
    (NULL, or any other integer constant with the value zero) may be used. static initialization also initializes pointers to their null values.

    Null pointers can indicate the absence of an object or can be used to indicate other types of error conditions. 
    In general, a function that receives a pointer argument almost always needs to check if the value is null and handle that case differently 
    (for example, free does nothing when a null pointer is passed). 
    
    */
}

int f(int n)
{
    printf("%d\n", n);
    return n*n;
}