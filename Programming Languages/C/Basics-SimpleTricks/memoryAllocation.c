#include <stdlib.h>
// Syntax of malloc()
// ptr = (castType*) malloc(size);

// ptr = (float*) malloc(100 * sizeof(float));
// The expression results in a NULL pointer if the memory cannot be allocated.


// "calloc" stands for contiguous allocation.
// SYNTAX
// ptr = (castType*)calloc(n, size);
// ptr = (float*) calloc(25, sizeof(float));

// free
// SYNTAX
free(ptr);

// ======== < malloc > ======== //
/*  void *malloc(int num); */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() 
{
   char name[100];  /* Create var name with 100 slots*/
   char *description; /*Create a pointer */

   strcpy(name, "Federico B");  /*Add name to name var*/

   description = malloc(200 * sizeof(char));  /* Add Size dynamically */

   if (description == NULL) 
      fprintf(stderr, "Error -- unable to allocate required memory\n");
   else
      strcpy(description, "Federico B is the best programmer : )");

   printf("Name = %s\n", name);
   printf("Description = %s\n", description);

   return 0;


}


// ======== < calloc > ======== //
/* void *calloc(int num, int size); */


#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() 
{
   char name[100];  /* Create var name with 100 slots*/
   char *description; /*Create a pointer */

   strcpy(name, "Federico B");  /*Add name to name var*/

   description = calloc(200, sizeof(char));  /* Add Size dynamically */

   if (description == NULL) 
      fprintf(stderr, "Error -- unable to allocate required memory\n");
   else
      strcpy(description, "Federico B is the best programmer : )");

   printf("Name = %s\n", name);
   printf("Description = %s\n", description);

   return 0;


}


// ======== < realloc +  free> ======== //
/* void *realloc(void *address, int newsize); */
/* void free(void *address); */



#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{

   char name[100]; 
   char * description;

   strcpy(name , "Fede b");

   /*Allocate Memory to Pointer dynamically */
   description = malloc(30*sizeof(char));

   if (description == NULL) 
      fprintf(stderr, "Error -- unable to allocate required memory\n");
   else
      strcpy(description, "Fede is the best programmer ;)");


   /* Change allocated memory on run time*/
   description = realloc(description, 100*sizeof(char));

   if (description == NULL)
      fprintf(stderr, "Error -- unable to allocate required memory\n");
   else 
      strcat(description, "Still the best!!!");

   printf("NAME = %s\n", name);
   printf("DESCRIPTION = %s\n", description);

   /* Memory free up*/
   free(description);

   return 0;
}

// NAME = Fede b
// DESCRIPTION = Fede is the best programmer ;)Still the best!!!

// Program to calculate the sum of n numbers entered by the user

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, *ptr, sum = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    ptr = (int*) malloc(n * sizeof(int));
 
    // if memory cannot be allocated
    if(ptr == NULL)                     
    {
        printf("Error! memory not allocated.");
        exit(0);
    }

    printf("Enter elements: ");
    for(i = 0; i < n; ++i)
    {
        scanf("%d", ptr + i);
        sum += *(ptr + i);
    }

    printf("Sum = %d", sum);
  
    // deallocating the memory
    free(ptr);

    return 0;
}


// Program to calculate the sum of n numbers entered by the user

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, *ptr, sum = 0;
    printf("Enter number of elements: ");
    scanf("%d", &n);

    ptr = (int*) calloc(n, sizeof(int));
    if(ptr == NULL)
    {
        printf("Error! memory not allocated.");
        exit(0);
    }

    printf("Enter elements: ");
    for(i = 0; i < n; ++i)
    {
        scanf("%d", ptr + i);
        sum += *(ptr + i);
    }

    printf("Sum = %d", sum);
    free(ptr);
    return 0;
}

//realloc()
// SYNTAX
// ptr = realloc(ptr, x);


#include <stdio.h>
#include <stdlib.h>

int main()
{
    int *ptr, i , n1, n2;
    printf("Enter size: ");
    scanf("%d", &n1);

    ptr = (int*) malloc(n1 * sizeof(int));

    printf("Addresses of previously allocated memory: ");
    for(i = 0; i < n1; ++i)
         printf("%u\n",ptr + i);

    printf("\nEnter the new size: ");
    scanf("%d", &n2);

    // rellocating the memory
    ptr = realloc(ptr, n2 * sizeof(int));

    printf("Addresses of newly allocated memory: ");
    for(i = 0; i < n2; ++i)
         printf("%u\n", ptr + i);
  
    free(ptr);

    return 0;
}

// Enter size: 2
// Addresses of previously allocated memory:26855472
// 26855476

// Enter the new size: 4
// Addresses of newly allocated memory:26855472
// 26855476
// 26855480
// 26855484