// ======== < Including Header Files: #include > ======== //

#include <stdio.h>
// #include "my_header.h"

// ======== < Including Header Files: wrapper #ifndef > ======== //

#ifndef HEADER_FILE
#define HEADER_FILE

// the entire header file file

#endif

// ======== < Including Header Files: computed include> ======== //

#if SYSTEM_1
    # include "system_1.h"
#elif SYSTEM_2
    # include "system_2.h"
#elif SYSTEM_3
//    ...
#endif

// Better way

#define SYSTEM_H "system_1.h"
// ...
// #include SYSTEM_H

// ======== < Symbolic constants > ======== //


#define VALUE 1
#define PI 3.14
#define NAME "Programmer"

#define C 299792458  // speed of light

// EXAMPLE
#include <stdio.h>
#define PI 3.1415

int main()
{
    float radius, area;
    printf("Enter the radius: ");
    scanf("%f", &radius);

    // Notice, the use of PI
    area = PI*radius*radius;

    printf("Area=%.2f",area);
    return 0;
}


// ======== < Macros > ======== //

// SYNTAX
#define circleArea(r) (3.1415*(r)*(r))

// EXAMPLE
#include <stdio.h>
#define PI 3.1415
#define circleArea(r) (PI*r*r)

int main() {
    float radius, area;

    printf("Enter the radius: ");
    scanf("%f", &radius);
    area = circleArea(radius);
    printf("Area = %.2f", area);

    return 0;
}

// ======== < Conditional Compilation > ======== //

#ifdef MACRO     
   // conditional codes
#endif

#if expression
   // conditional codes
#endif

#if expression
    // conditional codes if expression is non-zero
#elif expression1
    // conditional codes if expression is non-zero
#elif expression2
    // conditional codes if expression is non-zero
#else
    // conditional if all expressions are 0
#endif


// #defined
// #if defined BUFFER_SIZE && BUFFER_SIZE >= 2048
  // codes


// ======== < Predefined Macros > ======== //

// __DATE__   A string containing the current date
		
// __FILE__    A string containing the file name

// __LINE__  An integer representing the current line number

// __STDC__  If follows ANSI standard C, then the value is a nonzero integer

// __TIME__  A string containing the current date.

// : Get current time using __TIME__


#include <stdio.h>

int main() {

    printf("File :%s\n", __FILE__ );
    printf("Date :%s\n", __DATE__ );
    printf("Time :%s\n", __TIME__ );
    printf("Line :%d\n", __LINE__ );
    // printf("ANSI :%d\n", __STDC__ );

}


#include <stdio.h>
int main()
{
   printf("Current time: %s",__TIME__);   
}
// ======== < PRAGMAS> ======== //