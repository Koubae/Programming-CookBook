/*
    Convert base10(decimal) values to base2(binary)
    @Date: 1 - Jan - 2021
*/
#include <stdio.h>

void convert_bin(int power, int num)
{
    int first = 0;

    while (power > 0) {
        if (num >= power) {
            first = 1;
            printf("1");
            num %= power;
        } else if (first == 1) printf("0");        
        power /= 2;
    }   

    printf("\n");
}

int main(int argc, char *argv[]) 
{   

    int num = 0;
    int power = 1;

    printf("Please enter a number: ");
    scanf("%d", &num);
    printf("Hex %x \n", num);
    printf("Bin: ");

    while (power < num) {
        power *=2;
    }

    if (num == 0) printf("0\n");
    else convert_bin(power, num);

    return 0;
}