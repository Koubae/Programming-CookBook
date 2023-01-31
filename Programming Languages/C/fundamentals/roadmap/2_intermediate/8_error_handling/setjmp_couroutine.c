// @credit: https://stackoverflow.com/a/14685524/13903942
#include <stdio.h>
#include <setjmp.h>

jmp_buf bufferA, bufferB;

void routineB(); // forward declaration 

void routineA()
{
    int r ;

    printf("- 12 : (A1)\n");

    r = setjmp(bufferA);
    if (r == 0) routineB();

    printf("- 17 : (A2) r=%d\n",r);

    r = setjmp(bufferA);
    if (r == 0) longjmp(bufferB, 20001);

    printf("- 22 : (A3) r=%d\n",r);

    r = setjmp(bufferA);
    if (r == 0) longjmp(bufferB, 20002);

    printf("- 27 : (A4) r=%d\n",r);
}

void routineB()
{
    int r;

    printf("- 34 : (B1)\n");

    r = setjmp(bufferB);
    if (r == 0) longjmp(bufferA, 10001);

    printf("- 39 : (B2) r=%d\n", r);

    r = setjmp(bufferB);
    if (r == 0) longjmp(bufferA, 10002);

    printf("- 44 : (B3) r=%d\n", r);

    r = setjmp(bufferB);
    if (r == 0) longjmp(bufferA, 10003);
}


int main(int argc, char **argv) 
{
    routineA();
    return 0;
}