// different storage classes in a C program:

// auto
// register
// static
// extern


// ====== < STATIC > ====== //

#include <stdio.h>


/* Function Declaration */
void func(void); 

/*Global Variable with Static*/
static int count = 5;

int main (void) 
{
    while (count--){
        func();
    }

    return 0;
}


/* Function Definition */
void func(void) 
{
    static int local_var = 5; /*Local Var */
    local_var++;

    printf("local_var --> %d  | Count --> %d\n", local_var, count);
}


// ====== < EXTERN > ====== //


// File: main.c
#include <stdio.h>


int count;
extern void extern_func();


int main ()
{   
    count = 5;
    extern_func();

}

// File: other.c
#include <stdio.h>

extern int count;

void extern_func()
{
	printf("count is %d\n", count);
}


