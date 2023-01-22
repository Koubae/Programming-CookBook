#include <stdio.h>
#include <string.h>  

int main(int argc, char **argv)
{
    char str[11] = "Hello world";
    printf("str = %s \n", str);
    printf("str reversed = %s", strrev(str));

    return 0;
}