// ======== < errno, perror(). and strerror() > ======== //
#include <stdio.h>
#include <errno.h>
#include <string.h>

extern int errno;

int main()
{
   FILE * pf;
   int errnum;
   pf = fopen("don_t_exists.txt", "rb");

   if (pf == NULL) {

      errnum = errno;
      fprintf(stderr, "Value of errno ---> %d\n", errno);
      perror("Error of perror");
      fprintf(stderr, "Error opening file: %s\n", strerror(errnum));
   } else {
      fclose(pf);
   }
   
   return 0;
}
 

// ======== < Divide by Zero Errors > ======== //
#include <stdio.h>
#include <stdlib.h>

main() {

   int dividend = 20;
   int divisor = 0;
   int quotient;
 
   if( divisor == 0){
      fprintf(stderr, "Division by zero! Exiting...\n");
      exit(-1);
   }
   
   quotient = dividend / divisor;
   fprintf(stderr, "Value of quotient : %d\n", quotient );

   exit(0);
}


// ======== < Program Exit Status > ======== //

#include <stdio.h>
#include <stdlib.h>

main() {

   int dividend = 20;
   int divisor = 5;
   int quotient;
 
   if( divisor == 0) {
      fprintf(stderr, "Division by zero! Exiting...\n");
      exit(EXIT_FAILURE);
   }
	
   quotient = dividend / divisor;
   fprintf(stderr, "Value of quotient : %d\n", quotient );

   exit(EXIT_SUCCESS);
}



// ======== < errno > ======== //

#include <errno.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	int years;

	printf("Enter your age in years : ");
	fflush(stdout);
	errno = 0;
	if (scanf("%d", &years) != 1 || errno)
		return EXIT_FAILURE;
	printf("Your age in days is %d\n", years * 365);
	return 0;
}