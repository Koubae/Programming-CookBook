// ====== < Accessing Array Elements > ====== //

#include <stdio.h>

int main()
{
    int my_array[10]; /* Array with 10 Slots */
    int i, j;


    /* Init elements of my_array n to 0*/
    for (i=0; i<100; i++) {
        my_array[i] = i + 100; 
    }

    /* Print nums from my_array*/
    for (j=0; j<10; j++) {
        printf("Element[%d] = %d\n", j, my_array[j]);
    }

    return 0;
}

// Element[0] = 100
// Element[1] = 101
// Element[2] = 102
// Element[3] = 103
// Element[4] = 104
// Element[5] = 105
// Element[6] = 106
// Element[7] = 107
// Element[8] = 108
// Element[9] = 109


// C Program to store and print 12 values entered by the user

#include <stdio.h>
int main()
{
  int test[2][3][2];

  printf("Enter 12 values: \n");

  for (int i = 0; i < 2; ++i)
  {
    for (int j = 0; j < 3; ++j)
    {
      for (int k = 0; k < 2; ++k)
      {
        scanf("%d", &test[i][j][k]);
      }
    }
  }

  // Printing values with proper index.

  printf("\nDisplaying values:\n");
  for (int i = 0; i < 2; ++i)
  {
    for (int j = 0; j < 3; ++j)
    {
      for (int k = 0; k < 2; ++k)
      {
        printf("test[%d][%d][%d] = %d\n", i, j, k, test[i][j][k]);
      }
    }
  }

  return 0;
}

// Passing two-dimensional arrays
#include <stdio.h>
void displayNumbers(int num[2][2]);
int main()
{
    int num[2][2];
    printf("Enter 4 numbers:\n");
    for (int i = 0; i < 2; ++i)
        for (int j = 0; j < 2; ++j)
            scanf("%d", &num[i][j]);

    // passing multi-dimensional array to a function
    displayNumbers(num);
    return 0;
}

void displayNumbers(int num[2][2])
{
    printf("Displaying:\n");
    for (int i = 0; i < 2; ++i) {
        for (int j = 0; j < 2; ++j) {
           printf("%d\n", num[i][j]);
        }
    }
}

// Enter 4 numbers:
// 2
// 3
// 4
// 5
// Displaying:
// 2
// 3
// 4
// 5


//  find the number of elements in an array
int ix;
short anArray[]= { 3, 6, 9, 12, 15 };

/*
for (ix=0; ix< (sizeof(anArray)/sizeof(short)); ++ix) {
  DoSomethingWith("%d", anArray[ix] );
}

*/