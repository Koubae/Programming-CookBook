#include <stdio.h>
#include <string.h>

#define BUF_SIZE 1024

int main()
{

    // ------- READING FROM FGETS AND OPENING FILE 
    char str[20];
    FILE *f;
    fgets(str, 20, stdin); // Reasind typing from Terminal stdin
    puts(str);            // Outputs back 

    f = fopen("test.txt", "r+");
    
    if (f == NULL) {
        perror("Error while opening the file");
        return(-1);
    }
    else {

        if (fgets(str, 20, f) != NULL) 
            puts(str);
        else
            perror("File is empty;( ");      
    }

    fclose(f);

    // -------------> Reading from user Keybord, press CTRL+D for exit
    char buffer[BUF_SIZE];

    printf("Type anything to the keyboard!\n");
    char msg[] = "Type CTRL+D or CTRL+C to exit";
    while (fgets(buffer, BUF_SIZE, stdin)) {
        puts(buffer);

        puts(msg);
        printf("=========================\n");        
    }

    printf("Byeeee");

    return 0;    
}