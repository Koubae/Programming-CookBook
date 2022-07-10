#include <stdio.h>
#include <stdint.h>


void func(int i) {
    printf("%s\n", __FUNCTION__);
}

int main()
{
    __int8 vari8 = 100;
    func(vari8);   // no void func(__int8 i8) function
                // __int8 will be promoted to int

    return 0;

}