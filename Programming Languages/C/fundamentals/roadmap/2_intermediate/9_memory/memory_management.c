// https://stackoverflow.com/questions/722922/best-way-to-handle-memory-allocation-in-c
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    char *p;
    // ALWAYS check the returned pointer from malloc for NULL
    if((p = (char *) malloc(BUFSIZ)) == NULL ) {
    /* then malloc failed do some error processing. */
    }

    // For belt and suspenders safety, set a pointer to NULL after freeing it.
    free(p);
    p = NULL ;

    ///try to malloc and free a chunk of memory within the same scope if possible:

    {  
        char * p ;
        if((p = malloc(BUFSIZ)) == NULL ) {
            /* then malloc failed do some error processing. */
        }

        /* do your work. */

        /* now you're done, free the memory */

        free(p);
        p = NULL ;  /* belt-and suspenders */
    }


    return 0;
}

// When you can't, make it clear that what you're returning is malloc'ed memory, so the caller can free it.
 /* foo: do something good, returning ptr to malloc memory */
 char * foo(int bar) {
     return (char *) malloc(bar);
 }