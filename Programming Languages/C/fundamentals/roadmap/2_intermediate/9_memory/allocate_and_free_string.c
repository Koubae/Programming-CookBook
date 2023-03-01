// @credit: https://stackoverflow.com/a/24908/13903942
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char *duplicateString(char *src);


int main(void)
{
    char *pString;
    pString = duplicateString("hello");
    printf("%s\n", pString);
    free(pString);
    pString = duplicateString("world");
    printf("%s\n", pString);
    free(pString);

    for (int i = 0; i < 1000; ++i) {
        pString = duplicateString("hello world");
        printf("%s\n", pString);
        free(pString);
    }


    return 0;
}


char *duplicateString(char *src)
{
    char * dest;
    dest = malloc(strlen(src) + 1);
    if (dest == NULL)
        abort();
    strcpy(dest, src);
    return dest;
}