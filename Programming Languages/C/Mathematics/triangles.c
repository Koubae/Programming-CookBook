// Half Pyramid of *
#include <stdio.h>

int main() {
    int i, j, rows;
    printf("Enter total number of rows: ");
    scanf("%d", &rows);
    for (i=1; i<=rows; ++i) {
        for (j=1; j<=i; ++j) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}

// *
// * *
// * * *
// * * * *
// * * * * *


// Half Pyramid of Numbers
#include <stdio.h>


int main()
{
    int i, j, rows;
    printf("Enter N of Rows: ");
    scanf("%d", &rows);

    for (i=i; i<=rows; ++i) {
        for (j=1; j<=i; ++j) {
            printf("%d", j);
        }
        printf("\n");
    }
    return 0;
}

// 1
// 1 2
// 1 2 3
// 1 2 3 4
// 1 2 3 4 5

//Half Pyramid of Alphabet
#include <stdio.h>
int main()
{
   int i, j;
   char input, alphabet = 'A';
   printf("Enter an uppercase character you want to print in the last row: ");
   scanf("%c", &input);
   for (i = 1; i <= (input - 'A' + 1); ++i) {
      for (j = 1; j <= i; ++j) {
         printf("%c ", alphabet);
      }
      ++alphabet;
      printf("\n");
   }
   return 0;
}

//A
//B B
//C C C
//D D D D
//E E E E E
//F F F F F F


//  Inverted half pyramid of *
#include <stdio.h>

int main ()
{
    int i, j, rows;
    printf("Enter the number of Rows: ");
    scanf("%d", &rows);

    for (i=rows; i>=1; --i) {
        for (j=1;j<=i;++j) {
            printf("*");
        }
        printf("\n");
    }
    return 0;
}

//* * * * *
//* * * *
//* * * 
//* *
//*


// Inverted half pyramid of numbers
#include <stdio.h>

int main ()
{
    int i, j, rows;
    printf("Enter number of rows:");
    scanf("%d", &rows);

    for (i=rows; i >=1; --i) {
        for (j=1; j<=i; ++j) {
            printf("%d", j);
        }
        printf("\n");
    }
    return 0;
}

//1 2 3 4 5
//1 2 3 4 
//1 2 3
//1 2
//1


// Full Pyramid of *
#include <stdio.h>

int main ()
{
    int i, space, rows, k = 0;
    printf("Enter N of rows: ");
    scanf("%d", &rows);

    for (i=1; i<=rows; ++i, k=0) {
        for (space=1; space<=rows-i ; ++space) {
            printf("  ");
        }
        while (k != 2*i-1) {
            printf("* ");
            ++k;
        }
        printf("\n");
    }
    return 0;
}

//        *
//      * * *
//    * * * * *
//  * * * * * * *
//* * * * * * * * *

//Full Pyramid of Numbers
#include <stdio.h>
int main() {
   int i, space, rows, k = 0, count = 0, count1 = 0;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = 1; i <= rows; ++i) {
      for (space = 1; space <= rows - i; ++space) {
         printf("  ");
         ++count;
      }
      while (k != 2 * i - 1) {
         if (count <= rows - 1) {
            printf("%d ", i + k);
            ++count;
         } else {
            ++count1;
            printf("%d ", (i + k - 2 * count1));
         }
         ++k;
      }
      count1 = count = k = 0;
      printf("\n");
   }
   return 0;
}

//         1
//       2 3 2
//     3 4 5 4 3
//   4 5 6 7 6 5 4
// 5 6 7 8 9 8 7 6 5


#include <stdio.h>
int main() {
   int rows, i, j, space;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = rows; i >= 1; --i) {
      for (space = 0; space < rows - i; ++space)
         printf("  ");
      for (j = i; j <= 2 * i - 1; ++j)
         printf("* ");
      for (j = 0; j < i - 1; ++j)
         printf("* ");
      printf("\n");
   }
   return 0;
}

// * * * * * * * * *
//   * * * * * * *
//     * * * * *
//       * * *
//         *



// Inverted full pyramid of *
#include <stdio.h>

int main () {
    int rows, coef = 1, space, i, j;
    printf("Enter N of rows: ");
    scanf("%d", &rows);

    for (i=0; i<rows; i++) {
        for (space=1; space<=rows-i; space++)
            printf("  ");

        for (j=0; j<=i; j++) {
            if (j==0 || i==0)
                coef = 1;
            else
                coef = coef*(i-j+1)/j;
            printf("%4d", coef);
        }
        printf("\n");
    }
    return 0;
}


//            1
//          1   1
//        1   2   1
//      1   3   3    1
//    1  4    6   4   1
//  1  5   10   10  5   1