// @credit: https://en.wikibooks.org/wiki/C_Programming/Error_handling
#include <stdio.h>
#include <stdlib.h>
#include <setjmp.h>

int main(void) {
   int val;
   jmp_buf environment;

   val = setjmp(environment); // val is set to 0 the first time this is called

   if (val !=0) 
   {
      printf("You returned from a longjmp call, return value is %d\n", val); // now, value is 1, passed from longjmp()
      exit(0);
   }

   puts("Calling longjmp now");
   longjmp(environment, 1);

   return(0);
}