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
    bool myBoolTrue = true;
    bool myBoolFalse = false;
    char myNull = '\0';
    char *myNullPointer = NULL;

    printf("myBoolTrue %ld\n", sizeof(myBoolTrue));
    printf("myBoolTrue %ld\n", sizeof(myBoolTrue));
    printf("myNull %ld\n", sizeof(myNull));
    printf("myNullPointer %ld\n", sizeof(myNullPointer));


    printf("---------------- < ************* > ----------------\n");    
}
void dataTypes__typeCasting(void)
{
    printf("---------------- < Type Casting > ----------------\n");
    printf("---------------- < ************* > ----------------\n");    
    }
void dataTypes__stringInterpolation(void)
{
  printf("---------------- < String Interpolation > ----------------\n");
  printf("---------------- < ************* > ----------------\n");          
}
