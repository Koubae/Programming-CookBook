/**
@credit: https://stackoverflow.com/a/53063656/13903942

# Test it like this

#!/usr/bin/env bash
for std in c89 c99 c11 c17 gnu89 gnu99 gnu11 gnu17; do
  echo $std
  gcc -std=$std -o c.out c.c
  ./c.out
  echo
done
echo default
gcc -o c.out c.c
./c.out

*/

#include <stdio.h>

int main(void) {
#ifdef __STDC_VERSION__
    printf("__STDC_VERSION__ = %ld \n", __STDC_VERSION__);
#endif
#ifdef __STRICT_ANSI__
    puts("__STRICT_ANSI__");
#endif
    return 0;
}