// SYNTAX
// struct structureName 
// {
//     dataType member1;
//     dataType member2;
//     ...
// };
// When a struct type is declared, no storage or memory is allocated. To allocate memory of a given structure type and work with it, we need to create variables.
struct Person
{
    char name[50];
    int citNo;
    float salary;
};

// Struct Var
struct Person
{
    char name[50];
    int citNo;
    float salary;
};

int main()
{
    struct Person person1, person2, p[20];
    return 0;
}

// Variation
struct Person
{
    char name[50];
    int citNo;
    float salary;
} person1, person2, p[20];





// Program to add two distances (feet-inch)
#include <stdio.h>
struct Distance
{
    int feet;
    float inch;
} dist1, dist2, sum;

int main()
{
    printf("1st distance\n");
    printf("Enter feet: ");
    scanf("%d", &dist1.feet);

    printf("Enter inch: ");
    scanf("%f", &dist1.inch);
    printf("2nd distance\n");

    printf("Enter feet: ");
    scanf("%d", &dist2.feet);

    printf("Enter inch: ");
    scanf("%f", &dist2.inch);

    // adding feet
    sum.feet = dist1.feet + dist2.feet;
    // adding inches
    sum.inch = dist1.inch + dist2.inch;

    // changing to feet if inch is greater than 12
    while (sum.inch >= 12) 
    {
        ++sum.feet;
        sum.inch = sum.inch - 12;
    }

    printf("Sum of distances = %d\'-%.1f\"", sum.feet, sum.inch);
    return 0;
}



// ====== < Nested Struct > ====== //

struct complex
{
    int imag;
    float real;
};

struct number
{
    struct complex comp;
    int integers;
} num1, num2;



//Access members using Pointer

    // personPtr->age is equivalent to (*personPtr).age
    // personPtr->weight is equivalent to (*personPtr).weight

#include <stdio.h>
struct person
{
   int age;
   float weight;
};

int main()
{
    struct person *personPtr, person1;
    personPtr = &person1; // addr person1 stored in personPtr
 
    printf("Enter age: ");
    scanf("%d", &personPtr->age);

    printf("Enter weight: ");
    scanf("%f", &personPtr->weight);

    printf("Displaying:\n");
    printf("Age: %d\n", personPtr->age);
    printf("weight: %f", personPtr->weight);

    return 0;
}



//  Dynamic memory allocation of structs
#include <stdio.h>
#include <stdlib.h>

struct person
{
    int age;
    float weight;
    char name[30];
};

int main()
{
    struct person *ptr;
    int i, n;

    printf("Enter the number of persons: ");
    scanf("%d", &n);

    // Allocating mem for n nums of struct person
    ptr = (struct person*) malloc(n*sizeof(struct person));

    for (i=0; i<n;++i)
    {
        printf("Enter First name and age respectively: ");
        // To access members of 1st struct person,
       // ptr->name and ptr->age is used

       // To access members of 2nd struct person,
       // (ptr+1)->name and (ptr+1)->age is used
       scanf("%s %d", (ptr+i)->name, &(ptr+i)->age);
    }

    printf("Displaying Information:\n");
    for (i=0; i<n; ++i)
        printf("Name: %s\tAge: %d\n", (ptr+i)->name, (ptr+i)->age);

    return 0;
}


// ====== < struct from a function > ====== \\ 

#include <stdio.h>
struct student
{
    char name[50];
    int age;
};

// function prototype
struct student getInformation();

int main()
{
    struct student s;

    s = getInformation();

    printf("\nDisplaying information\n");
    printf("Name: %s", s.name);
    printf("\nRoll: %d", s.age);
    
    return 0;
}
struct student getInformation() 
{
  struct student s1;

  printf("Enter name: ");
  scanf ("%[^\n]%*c", s1.name);

  printf("Enter age: ");
  scanf("%d", &s1.age);
  
  return s1;
}	


// ====== < struct by reference > ====== \\ 

#include <stdio.h>
typedef struct Complex
{
    float real;
    float imag;
} complex;

void addNumbers(complex c1, complex c2, complex *result); 

int main()
{
    complex c1, c2, result;

    printf("For first number,\n");
    printf("Enter real part: ");
    scanf("%f", &c1.real);
    printf("Enter imaginary part: ");
    scanf("%f", &c1.imag);

    printf("For second number, \n");
    printf("Enter real part: ");
    scanf("%f", &c2.real);
    printf("Enter imaginary part: ");
    scanf("%f", &c2.imag);

    addNumbers(c1, c2, &result); 
    printf("\nresult.real = %.1f\n", result.real);
    printf("result.imag = %.1f", result.imag);
    
    return 0;
}
void addNumbers(complex c1, complex c2, complex *result) 
{
     result->real = c1.real + c2.real;
     result->imag = c1.imag + c2.imag; 
}

// ====== < Bit Fields > ====== \\ 
/*   https://en.wikipedia.org/wiki/Bit_field  */

#include <stdio.h>
#include <string.h>

struct {
   unsigned int age : 3;
} Age;

int main( ) {

   Age.age = 4;
   printf( "Sizeof( Age ) : %d\n", sizeof(Age) );
   printf( "Age.age : %d\n", Age.age );

   Age.age = 7;
   printf( "Sizeof( Age ) : %d\n", sizeof(Age) );
   printf( "Age.age : %d\n", Age.age );

   Age.age = 8;
   printf( "Age.age : %d\n", Age.age );

   return 0;
}

// Sizeof( Age ) : 4
// Age.age : 4
// Sizeof( Age ) : 4
// Age.age : 7
// Age.age : 0


// ====== < Linked List Simple > ====== \\ 

struct restaurant_order {
    char description[100];
    double price;
    struct restaurant_order *next_order;
};

// ====== <  partial declaration of the String class > ====== \\ 
// https://stackoverflow.com/a/840703/13903942

typedef struct String_Struct* String;

struct String_Struct
{
    char* (*get)(const void* self);
    void (*set)(const void* self, char* value);
    int (*length)(const void* self);
};

char* getString(const void* self);
void setString(const void* self, char* value);
int lengthString(const void* self);

String newString();

String newString()
{
    String self = (String)malloc(sizeof(struct String_Struct));

    self->get = &getString;
    self->set = &setString;
    self->length = &lengthString;

    self->set(self, "");

    return self;
}

char* getString(const void* self_obj)
{
    return ((String)self_obj);//->internal->value;
}