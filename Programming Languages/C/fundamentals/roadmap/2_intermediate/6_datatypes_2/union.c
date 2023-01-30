// A union is a user-defined type similar to structs in C except for one key difference. Structs allocate enough space to store all its members wheres unions allocate the space to store only the largest member.

// NOTE:
// When a union is defined, it creates a user-defined type. However, no memory is allocated. To allocate memory for a given union type and work with it, we need to create variables.

// NOTE:
// With a union, all members share the same memory.

union car
{
    char name[50];
    int price;
};

int main()
{
    union car car1, car2, *car3;
    return 0;
}

// Variant 

union car
{
    char name[50];
    int price;
} car1, car2, *car3;

// ======= < Difference between unions and structures > ======= \\

#include <stdio.h>
union unionJob
{
   //defining a union
    char name[32];
    float salary;
    int workerNo;
} uJob;

struct structJob
{
    char name[32];
    float salary;
    int workerNo;
} sJob;

int main()
{
    printf("size of union = %d bytes", sizeof(uJob));  // size of union = 32
    printf("\nsize of structure = %d bytes", sizeof(sJob));  // size of structure = 40
    return 0;
}


#include <stdio.h>
union Job {
   float salary;
   int workerNo;
} j;

int main() {
   j.salary = 12.3;

   // when j.workerNo is assigned a value,
   // j.salary will no longer hold 12.3
   j.workerNo = 100;

   printf("Salary = %.1f\n", j.salary);
   printf("Number of workers = %d", j.workerNo);
   return 0;
}

// Salary = 0.0
// Number of workers = 100