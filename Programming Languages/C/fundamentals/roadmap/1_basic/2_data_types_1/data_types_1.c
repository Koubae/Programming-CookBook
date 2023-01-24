#include <stdio.h>
#include <stdint.h>  // uint8_t uint16_t uint32_t uint64_t
#include <stdbool.h>   // bool true false

void dataTypes__int(void);
void dataTypes__char(void);
void dataTypes__bool(void);
void dataTypes__typeCasting(void);
void dataTypes__stringInterpolation(void);

int main(void)
{
    dataTypes__int();
    dataTypes__char();
    dataTypes__bool();
    dataTypes__typeCasting();
    dataTypes__stringInterpolation();
    return 0;
}


void dataTypes__int(void)
{
    short int_short = -1;                                                   // 2 byte -32,768 -> 32.767
    signed short int_sshort = -1;                                           // 2 bytes −32,768 to 32,767
    unsigned short int_ushort = 10;                                         // 2 bytes 0 to 65,535
    
    int int_int = 1;                                                        // 2 byte -32,768 -> 32.767
    signed int int_sint = 1;                                                // 2 byte -32,768 -> 32.767
    unsigned int int_uint = 1;                                              // 2 bytes 0 to 65,535

    long int_long = 1230;                                                   // 4 bytes -2,147,483,648 to 2,147,483,647
    signed long int_slong = 1230;                                           // 4 bytes -2,147,483,648 to 2,147,483,647
    unsigned long int_ulong = 1230;                                         // 0 to 4,294,967,295

    long long int_long_long = 1321321312;                                   // 8 bytes  -(2^63) to (2^63)-1 
    signed long long int_long_slong = 1321321312;                           // 8 bytes  -(2^63) to (2^63)-1 
    unsigned long long int_long_ulong     = 0xFFFFFFFFFFFFFFFF;             // 8 bytes 0 to 18,446,744,073,709,551,615 

    float float_float = .2;                                                 // 4 bytes 1.2E-38 to 3.4E+38
    double float_double = 12.3203;                                          // 8 bytes 1.7E-308 to 1.7E+308
    long double float_long_double = 1233.12313;                             // 16 bytes  3.4E-4932 to 1.1E+4932

    // 1 byte -> [0-255] or [0x00-0xFF]
    uint8_t number8 = int_long_ulong;    // bytes 1 
    uint16_t number16 = number8;         // bytes 2
    uint32_t number32 = number16;        // bytes 4
    uint64_t number64 = number32;        // bytes 8

    printf("---------------- < Data types: int > ----------------\n");

    printf("short = %ld\n", sizeof(int_short));
    printf("signed short = %ld\n", sizeof(int_sshort));
    printf("unsigned short = %ld\n", sizeof(int_ushort));

    printf("int = %ld\n", sizeof(int_int));
    printf("signed int = %ld\n", sizeof(int_sint));
    printf("unsigned int = %ld\n", sizeof(int_uint));

    printf("long = %ld\n", sizeof(int_long));
    printf("signed long = %ld\n", sizeof(int_slong));
    printf("unsigned long = %ld\n", sizeof(int_ulong));

    printf("long long = %ld\n", sizeof(int_long_long));
    printf("signed long long = %ld\n", sizeof(int_long_slong));
    printf("unsigned long long = %ld\n", sizeof(int_long_ulong));

    printf("float = %ld\n", sizeof(float_float));
    printf("double = %ld\n", sizeof(float_double));
    printf("long double = %ld\n", sizeof(float_long_double));

    printf("uint8_t = %ld\n", sizeof(number8));
    printf("uint16_t = %ld\n", sizeof(number16));
    printf("uint32_t = %ld\n", sizeof(number32));
    printf("uint64_t = %ld\n", sizeof(number64));


    printf("---------------- < ************* > ----------------\n");
  
}

void dataTypes__char(void)
{
    printf("---------------- < Data types: char > ----------------\n");
    // single quote is for character;
 
    char char_simple = 'a'; // bytes 1 : -128 to 127 or 0 to 255
    signed char char_signed = 'a'; // bytes 1: -128 to 127
    unsigned char char_u = 'a';  // bytes 2: 0 to 255

    // double quote is for string.
    char string_simple[] = "myString";
    char string_simple_2[] = {'m', 'S', 't', 'r', 'i', 'n', 'g'};
    char string_fixed_size[8] = "myString";
    char *string_pointer = "myString"; 
    char string_poionter_2 = *"myString";

     printf("char = %ld\n", sizeof(char_simple));
     printf("char_signed = %ld\n", sizeof(char_signed));
     printf("char_u = %ld\n", sizeof(char_u));

     printf("string_simple[] = %ld\n", sizeof(string_simple));
     printf("string_simple_2[] = %ld\n", sizeof(string_simple_2));
     printf("string_fixed_size[8] = %ld\n", sizeof(string_fixed_size));
     printf("*string_pointer = %ld\n", sizeof(string_pointer));
     printf("string_poionter_2 = %ld\n", sizeof(string_poionter_2));

    printf("---------------- < ************* > ----------------\n");    
}

void dataTypes__bool(void)
{
    printf("---------------- < Data types: bool > ----------------\n");
    bool boolTrue = true;
    bool boolFalse = false;

    bool boolTrueInt = 1;
    bool boolFalseInt = 0;

    char myNull = '\0';
    char *myNullPointer = NULL;

    printf("myBoolTrue %ld\n", sizeof(boolTrue));
    printf("boolFalse %ld\n", sizeof(boolFalse));
    printf("boolTrueInt %ld\n", sizeof(boolTrueInt));
    printf("boolFalseInt %ld\n", sizeof(boolFalseInt));
    printf("myNull %ld\n", sizeof(myNull));
    printf("myNullPointer %ld\n", sizeof(myNullPointer));

    printf("---------------- < ************* > ----------------\n");    
}
void dataTypes__typeCasting(void)
{
    printf("---------------- < Type Casting > ----------------\n");

    // Implicit type casting / data conversion
    char char_var = 'a';
    int int_var = char_var; // char to int implicity
    printf("char_var = %c, int_var = %d\n", char_var, int_var); // char_var = a, int_var = 97



    // Explicit type casting 
    int a_char_int = 97; 
    char a_char_char = (char) a_char_int;
    printf("a_char_int=%d -> %c \n", a_char_int, a_char_char);

    int int_var2 = 10;
    double double_var = (double) int_var2;
    printf("int_var2=%d, double_var=%.6lf\n", int_var2, double_var);

    unsigned char unsigned_char = (unsigned char) (0x87 + 0xFF00);

    float float_value1 = (float) 80 / 3;
    float float_value2 = (float) ((float) 80 / (float) 30);
    
    // Warning!!!
    // Pointer conversions --> https://learn.microsoft.com/en-us/cpp/cpp/type-conversions-and-type-safety-modern-cpp?view=msvc-170#pointer-conversions
    /*
    In many expressions, a C-style array is implicitly converted to a pointer to the first element in the array, 
    and constant conversions can happen silently. Although this is convenient, it's also potentially error-prone.
     For example, the following badly designed code example seems nonsensical, and yet it will compile and produces a result of 'p'. 
     First, the "Help" string constant literal is converted to a char* that points to the first element of the array;
      that pointer is then incremented by three elements so that it now points to the last element 'p'.
    
    */
    char* s = "Help" + 3;
    printf("pointer:, %p, %c\n", s, *s);




    printf("---------------- < ************* > ----------------\n");    
    }

void dataTypes__stringInterpolation(void)
{
  printf("---------------- < String Interpolation > ----------------\n");
   
    char a = 'C';                       // single character    %c
    char b[] = "Hello";                   // array of characters %s 
    char f = 120;                         // 1 byte (-128 to +127) %d or %c
    unsigned char g = 255;               // 1 byte (0 to +255) %d or %c 

    float c = 3.141592;                         // 4 bytes (32 bits of precision) 6 - 7 digits %f
    double d = 3.141592653589793;               // 8 bytes (64 bits of precision) 15 - 16 digits %lf

    bool e = true;                        // 1 byte (true or false) %d

    short h = 32767;                  // 2 bytes (−32,768 to +32,767) %d
    unsigned short i = 65535;           // 2 bytes (0 to +65,535) %d

    int j = 2147483647;                     // 4 bytes (-2,147,483,648 to +2,147,483,647) %d
    unsigned int k = 4294967295;            // 4 bytes (0 to +4,294,967,295) %u

    long long int l = 9223372036854775807;                         // 8 bytes (-9 quintillion to +9 quintillion) %lld
    unsigned long long int m = 18446744073709551615U; // 8 bytes (0 to +18 quintillion) %llu

    int *pointer = &j;

    int octal = 610;
    int hexadecimal = 0X7FA;
    float hexadecimal_float = -0XC.90FEP-2;
    int scientific_notation = 3.9265e+2;


    printf("%c\n", a);  // char
    printf("%s\n", b);  // character array
    printf("%d\n", f);  // char as numeric value
    printf("%d\n", g);  // unsigned char as numeric value
    printf("%f\n", c);  // float
    printf("%lf\n", d); // double
    printf("%d\n", e);  // bool
    printf("%d\n", h);  // short
    printf("%d\n", i);  // unsigned short
    printf("%d\n", j);  // int
    printf("%u\n", k);  // unsigned int
    printf("%lld\n", l);  // long long int
    printf("%llu\n", m);  // unsigned long long int
    printf("%p\n", pointer); // pointer


    printf("%o\n", octal);  // octal
    printf("%x\n", hexadecimal);  //     char hexadecimal = 0X7FA;
    printf("%a\n", hexadecimal_float);  // Hexadecimal floating point, lowercase
    printf("%e\n", scientific_notation);  //  Scientific notation (mantissa/exponent)
    printf("%g\n", d);  //  Use the shortest representation: %e or %f
    printf("%n", pointer); // nothing
    printf("%%\n"); // print the '%' litteral

    // --------- Flags
    // - left-justify (right justify is default)
    // + Forces to preceed the result with a plus or minus sign
    // # Used with o, x or X specifiers the value is preceeded with 0, 0x or 0X respectively for values different than zero. Used with a, A, e, E, f, F, g or G it forces the written output to contain a decimal point even if no more digits follow. By default, if no digits follow, no decimal point is written.
    // .numbeber : preciosion
    // .* The precision is not specified in the format string, but as an additional integer value argument preceding the argument that has to be formatted.

    // right justify (default)
    printf("Left justify %45s This will be printed after -45 n\n", b);
    printf("Left justify %45s This will be printed after -45 n\n", b);
    printf("Left justify %45s This will be printed after -45 n\n", b);

    // left justify
    printf("Left justify %-45s This will be printed after -45 n\n", b);
    printf("Left justify %-45s This will be printed after -45 n\n", b);
    printf("Left justify %-45s This will be printed after -45 n\n", b);

    // Decimal precision
    printf("Precision 2: %.2lf\n", d);
    printf("Precision 3: %.3lf\n", d);
    printf("Precision 4: %.4lf\n", d);
    printf("Precision 5: %.5lf\n", d);
    printf("Precision 6: %.6lf\n", d);
    printf("Precision *: %.*f\n", c);


  printf("---------------- < ************* > ----------------\n");          
}
