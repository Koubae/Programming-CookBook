// ====== < EXAMPLE 1 > ====== //

#include <stdio.h>

int main(void) {
    printf("Char Size: %lu bytes\n", sizeof(char));
    printf("Int Size: %lu bytes\n", sizeof(int));
    printf("Short Size: %lu bytes\n", sizeof(short));
    printf("Long Size: %lu bytes\n", sizeof(long));
    printf("Float Size: %lu bytes\n", sizeof(float));
    printf("Double Size: %lu bytes\n", sizeof(double));
    printf("Long Double size: %lu bytes\n", sizeof(long double));
}

//Char Size: 1 bytes
//Int Size: 4 bytes
//Short Size: 2 bytes
//Long Size: 4 bytes
//Float Size: 4 bytes
//Double Size: 8 bytes
//Long Double size: 16 bytes


// ====== < EXAMPLE 2 > ====== //

#include <stdio.h>
#include <limits.h>
// #include <stdlib.h>
// #include <float.h>


int main (int argc, char** argv) 
{
	printf("\n\n");
	printf("/======== < CHAR > ========\\\n");
	printf("CHAR_BIT  ---> %d\n", CHAR_BIT);
	printf("CHAR_MAX  ---> %d\n", CHAR_MAX);
	printf("CHAR_MIN  ---> %d\n", CHAR_MIN);
	printf("UCHAR_MAX ---> %d\n\n", UCHAR_MAX);

	printf("/======== < SCHAR SIGNED CHAR> ========\\\n");
	printf("SCHAR_MAX  ---> %d\n", SCHAR_MAX);
	printf("SCHAR_MIN  ---> %d\n\n", SCHAR_MIN);

	printf("/======== < SHRT SHORT > ========\\\n");
	printf("SHRT_MAX  ---> %d\n", SHRT_MAX);
	printf("SHRT_MIN  ---> %d\n", SHRT_MIN);
	printf("USHRT_MAX  ---> %d\n\n", (unsigned short) USHRT_MAX);

	printf("/======== < INT > ========\\\n");
	printf("INT_MAX  ---> %d\n", INT_MAX);
	printf("INT_MIN  ---> %d\n", INT_MIN);	
	printf("UINT_MAX  ---> %lu\n\n", (unsigned int) UINT_MAX);


	printf("/======== < LONG > ========\\\n");
	printf("LONG_MAX  ---> %ld\n", (long) LONG_MAX);
	printf("LONG_MIN ---> %ld\n", (long) LONG_MIN);
	printf("ULONG_MAX  ---> %lu\n", (unsigned long) ULONG_MAX);	
	
	

	return 0;
}

// /======== < CHAR > ========\
// CHAR_BIT  ---> 8
// CHAR_MAX  ---> 127
// CHAR_MIN  ---> -128
// UCHAR_MAX ---> 255

// /======== < SCHAR SIGNED CHAR> ========\
// SCHAR_MAX  ---> 127
// SCHAR_MIN  ---> -128

// /======== < SHRT SHORT > ========\      
// SHRT_MAX  ---> 32767
// SHRT_MIN  ---> -32768
// USHRT_MAX  ---> 65535

// /======== < INT > ========\
// INT_MAX  ---> 2147483647
// INT_MIN  ---> -2147483648
// UINT_MAX  ---> 4294967295

// /======== < LONG > ========\
// LONG_MAX  ---> 2147483647
// LONG_MIN ---> -2147483648
// ULONG_MAX  ---> 4294967295


// ====== < EXAMPLE 3 FLOAT > ====== //

#include <stdio.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {

    printf("Storage size for float : %d \n", sizeof(float));
    printf("FLT_MAX    --->   %g\n", (float) FLT_MAX);
    printf("FLT_MIN    --->   %g\n", (float) FLT_MIN);
    printf("-FLT_MAX   --->   %g\n", (float) -FLT_MAX);
    printf("-FLT_MIN   --->   %g\n", (float) -FLT_MIN);
    printf("DBL_MAX    --->   %g\n", (double) DBL_MAX);
    printf("DBL_MIN    --->   %g\n", (double) DBL_MIN);
    printf("-DBL_MAX   --->   %g\n", (double) -DBL_MAX);
    printf("Precision value:  %d\n", FLT_DIG );

    return 0;
}

// Storage size for float : 4 
// FLT_MAX    --->   340282346638528860000000000000000000000.000000
// FLT_MIN    --->   1.17549e-038
// -FLT_MAX   --->   -3.40282e+038
// -FLT_MIN   --->   -1.17549e-038
// DBL_MAX    --->   1.79769e+308
// DBL_MIN    --->   2.22507e-308
// -DBL_MAX   --->   -1.79769e+308
// Precision value:  6