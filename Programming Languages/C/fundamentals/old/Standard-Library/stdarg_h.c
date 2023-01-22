// ======== < DOCUMENTATION > ======== //
// variable argument lists 
//         https://linux.die.net/man/3/stdarg

// https://www.cprogramming.com/tutorial/c/lesson17.html

// ======== < Calc Average> ======== //


#include <stdio.h>
#include <stdarg.h>

double average(int num, ...) {

   va_list valist;
   double sum = 0.0;
   int i;

   /* initialize valist for num number of arguments */
   va_start(valist, num);

   /* access all the arguments assigned to valist */
   for (i = 0; i < num; i++) {
      sum += va_arg(valist, int);
   }
	
   /* clean memory reserved for valist */
   va_end(valist);

   return sum/num;
}

int main() {
   printf("Average of 2, 3, 4, 5 = %f\n", average(4, 2,3,4,5));
   printf("Average of 5, 10, 15 = %f\n", average(3, 5,10,15));
}

// Average of 2, 3, 4, 5 = 3.500000
// Average of 5, 10, 15 = 10.000000