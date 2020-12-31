
// Change Value of Pointed Object from a Pointer
// example 1
int* pc, c;
c = 5;
pc = &c;
c = 1;
//printf("%d", c);    // Output: 1
// printf("%d", *pc);  // Ouptut: 1

// example 2
int* pc, c;
c = 5;
pc = &c;
*pc = 1;
//printf("%d", *pc);  // Ouptut: 1
//printf("%d", c);    // Output: 1

// example 3
int* pc, c, d;
c = 5;
d = -15;

//pc = &c; printf("%d", *pc); // Output: 5
// pc = &d; printf("%d", *pc); // Ouptut: -15





#include <stdio.h>
int main()
{
    int* pc, c;

    c = 22;
    printf("Address of c: %p\n", &c);
    printf("Value of c: %d\n\n", c);  // 22

    pc = &c;
    printf("Address of pointer pc: %p\n", pc);
    printf("Content of pointer pc: %d\n\n", *pc); // 22

    c = 11;
    printf("Address of pointer pc: %p\n", pc);
    printf("Content of pointer pc: %d\n\n", *pc); // 11

    *pc = 2;
    printf("Address of c: %p\n", &c);
    printf("Value of c: %d\n\n", c); // 2
    return 0;
}

// OUTPUT
// Address of c: 2686784
// Value of c: 22

// Address of pointer pc: 2686784
// Content of pointer pc: 22

// Address of pointer pc: 2686784
// Content of pointer pc: 11

// Address of c: 2686784
// Value of c: 2


// Pointers and Arrays
#include <stdio.h>

int main ()
{
    int i, x[6], sum = 0;

    printf("Enter 6 nums: ");
    for (i=0; i<6; i++) {
        // Equivalent to scanf("%d", &x[i]);
        scanf("%d", x+i);

        // Equivalent to sum += x[i]
        sum += *(x+i);
    }
    printf("Sum = %d", sum);
    return 0;
}


//Pass Addresses to Functions
#include <stdio.h>

void swap(int *n1, int *n2);

int main()
{
    int num1 = 5, num2 = 10;
    printf("Addr num1 Before swap = %p\n", &num1);
    printf("Addr num2 Before swap = %p\n", &num2);

    // address of num1 and num2 is passed
    swap(&num1, &num2);

    printf("num1 = %d | addr = %p\n", num1, &num1);
    printf("num2 = %d | addr = %p" , num2, &num2);
    return 0;
}

void swap(int* n1, int* n2)
{

    int temp;
    temp = *n1;
    *n1 = *n2;
    *n2 = temp;
    printf("Addr num1 After swap = %p\n", &n1);
    printf("Addr num2 After swap = %p\n", &n2);
}


//Passing Pointers to Functions
#include <stdio.h>

void addOne(int* ptr)
{
    (*ptr)++; // Adding 1 to ptr
}

int main()
{
    int* p, i = 10;
    p = &i;
    addOne(p);

    printf("%d", *p); // 11
    return 0;
}


//e Numbers and Calculate Average Using Arrays
#include <stdio.h>
int main() {
    int n, i;
    float num[100], sum = 0.0, avg;

    printf("Enter the numbers of elements: ");
    scanf("%d", &n);

    while (n > 100 || n < 1) {
        printf("Error! number should in range of (1 to 100).\n");
        printf("Enter the number again: ");
        scanf("%d", &n);
    }

    for (i = 0; i < n; ++i) {
        printf("%d. Enter number: ", i + 1);
        scanf("%f", &num[i]);
        sum += num[i];
    }

    avg = sum / n;
    printf("Average = %.2f", avg);
    return 0;
}




// ====== <  function pointers + typedef > ====== //
// https://stackoverflow.com/a/3674225/13903942

// This code shows that the typedefs without the asterisk are not function pointers 

static int function(void)
{
    return 0;
}

typedef int   fc_name1 (void);
typedef int  (fc_name2)(void);
typedef int (*fc_name3)(void);

// fc_name1 x = function;
// fc_name2 y = function;
// fc_name3 z = function;


// ====== <  Some Pointers > ====== //

#include <stdio.h>

int main(void)
{
    int *pointer;
    int my_var;

    my_var = 'A';

    pointer = &my_var;

    printf("Pointer is at addrr %p\n", &pointer);
    printf("Value in pointer = %c\n\n", *pointer);
    /*
    Pointer is at addrr 0061FF1C
    Value in pointer = A */

    // Arrays 
    char my_array[5] = {'a', 'A', 'b', 'z', 'M'};
    char *ptr_array = my_array;
    char **ptr_of_ptr = &ptr_array;

    printf("array[3] = %c, addr = %p\n", my_array[3], &my_array[3]);
    printf("ptr_array[3] = %c, addr = %p\n", ptr_array[3], &ptr_array[3]);
    printf("**Pointer of Poniter[3] = %c, addr = %p\n", (*ptr_of_ptr[3], &(*ptr_of_ptr[3])));
    /*
    array[3] = z, addr = 0061FF12
    ptr_array[3] = z, addr = 0061FF12
    **Pointer of Poniter[3] = A, addr = 0061FF12
    */
    printf("================================================\n");

    // ---- string 
    printf("Stings Array = %s, addr = %p\n", my_array, &my_array);
    printf("Acces through Pointer = %s, Addr = %p\n", ptr_array, &ptr_array);
    printf("Pointer of Pointer to Array = %s, Addr = %p\n", (*ptr_of_ptr, &(*ptr_of_ptr)));
    /*
    
    Stings Array = aAbzMA, addr = 0061FF0F
    Acces through Pointer = aAbzMA, Addr = 0061FF08
    Pointer of Pointer to Array = ☼ a, Addr = 0061FF08
    */

    printf("================================================\n");

    // ------------ ARRAY OF POINTERS

    char *ptr_array_[2];
    char *ptr1 = NULL, *ptr2 = NULL;
    char char_elements[2] = {'H', 'i'};

    ptr1 = &char_elements[1];
    ptr2 = char_elements;

    ptr_array_[0] = ptr2;
    ptr_array_[1] = ptr1;

    printf("**ptr_array_ = %c\n", **ptr_array_);

    printf("addr at **ptr_array = %p\n", &(**ptr_array_));
    printf("addr at **ptr_array[0] = %p\n\n", &(*ptr_array_[0]));
    
    printf("*ptr_array[1] = %c\n", *ptr_array_[1]);
    printf("addr at *ptr_array[0] = %p\n", &(**ptr_array_));
    printf("addr at *ptr_array[0] = %p\n", &(**ptr_array_));
    printf("addr at *ptr_array[1] = %p\n", &(*ptr_array_[1]));

    /*
    
    **ptr_array_ = H
    addr at **ptr_array = 0061FEF6
    addr at **ptr_array[0] = 0061FEF6

    *ptr_array[1] = i
    addr at *ptr_array[0] = 0061FEF6
    addr at *ptr_array[0] = 0061FEF6
    addr at *ptr_array[1] = 0061FEF7
    */

    return 0;
}