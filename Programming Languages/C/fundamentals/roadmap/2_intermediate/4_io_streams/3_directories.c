/*
@credit: https://stackoverflow.com/a/4204758/13903942
*/

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>

void readDir()
{
    DIR *directory;
    struct dirent *directoryStruct;
    const char dirName[] = ".";


    directory = opendir(dirName);
    if (!directory) {
        perror("Not a directory, error: ");
        exit(-1);
    } 
    while((directoryStruct = readdir(directory)) != NULL) {
        printf("%s\n", directoryStruct->d_name);
    }
    closedir(directory);

}

int main(void)
{

    readDir();
    return 0;
}