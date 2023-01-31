#include <stdio.h>
#include <string.h>
#include <errno.h>


extern int errno;

int main()
{
    FILE *file;
    int errorNumber;

    file = fopen("no-exist.txt", "r");
    if (file == NULL) {
        errorNumber = errno;
        fprintf(stderr, "Error opening file %d - %s\n", errno, strerror(errorNumber)); // strerror get same error as perror!
        perror("File not found");
        return 1;
    }

    fclose(file);

    return 0;
}