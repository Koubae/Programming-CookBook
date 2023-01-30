#include <stdio.h>
/*
auto - automatic duration and no linkage
register - automatic duration and no linkage; address of this variable cannot be taken
static - static duration and internal linkage (unless at block scope)
extern - static duration and external linkage (unless already declared internal) 
*/

void counterFunc();
void funcExtern();

static int counterGlobal = 0;

// Refers to the i that is defined in Source1.c:
extern int i;
// global var used by other scripts using extern keyword
int globalInt;
extern void printSource2(); // referenced in source2.c

int main(void)
{
    // local lifetimes
    // auto - register

    // auto 
    // auto is the default storage class. myInt and myIntLocal are the same. auto can (and should) be ommitted
    int myInt = 10;  
    auto int myIntLocal = 10;

    // register
    // deprecated: (SON'T USE IT)
    // only allowed for objects declared at block scope, including function parameter lists
    // indicates automatic storage duration and no linkage, hints the optimizer to store the value of this variable in a CPU register if possible
    // can't apply the unary address-of operator (&) to a register object nor can the register keyword be used on arrays.
    register int myIntRegister = 25;
    

    printf("locals (%d, %d, %d)\n", myInt, myIntLocal, myIntRegister); // just to remove -Wunused-variable

    // global lifetime
    // static extern

    // static A variable declared at the internal level with the static storage-class specifier has a global lifetime but is visible only within the block in which it is declared. F
    counterFunc();
    counterFunc();

    // extern
    // It is used to make the external-level variable definition visible.
    // A variable declared as extern has no storage allocated for itself; it is only a name.
    printf("extern var i = %d\n", i);
    funcExtern();
    printSource2();

    return 0;
}


void counterFunc()
{
    static int counter = 0; // local static
    counter ++;
    counterGlobal ++;
    printf("Counter = %d GlobalCounter = %d\n", counter, counterGlobal);
}


void funcExtern()
{
    // Address of global i assigned to pointer variable:
    static int *pExternI = &i;

    // This definition of i hides the global i in Source.c:
    int i = 16;

    
    // Prints 16, 1:
    printf("funcExtern, i=%d, pExternI=%d\n", i, *pExternI);
}