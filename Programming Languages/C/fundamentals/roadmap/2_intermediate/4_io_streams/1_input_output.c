#include <stdio.h>
#include <stdlib.h>

void getchar__putchar()
{
    int c;

    printf("Enter a Value: ");
    c = getchar();

    printf("Entered: ");
    putchar(c);
    printf("\n");
}

// https://learn.microsoft.com/en-gb/cpp/c-runtime-library/reference/getchar-getwchar?view=msvc-170#example
void crt_getchar()
{
    int valueSize = 80;
    char buffer[valueSize + 1]; // require 1 additional space for the null char
    int i;
    int ch;

    // this was the provided example. I prefer though the logic is inside the for loop
    /*for (i = 0; (i < valueSize) && ( (ch = getchar()) != EOF ) && (ch != '\n'); i++ ) {
        buffer[i] = (char) ch;
    }*/

    for (i = 0; i < valueSize; i++) {
        ch = getchar(); 
        if (ch == EOF || ch == '\n') 
            break;
        buffer[i] = (char) ch;
    }


    buffer[i] = '\0'; // terminate string with null char;
    printf("Input: %s\n", buffer);
}

// https://learn.microsoft.com/en-gb/cpp/c-runtime-library/reference/putchar-putwchar?view=msvc-170#example
void crt_putchar()
{
    //FILE *stream; unsued
    char *p;
    char buffer[] = "This is the line of output\n";
    int ch;
    // provided in the example
    /*for (p = buffer; (ch != EOF) && (*p != '\0'); p++ ) 
        ch = putchar( *p );*/

    for (p = buffer; ch != EOF; p++) {
        if (*p == '\0')
            break;
        ch = putchar( *p );
    }
    


}


void printf__scanf()
{
    char str[100];
    int i;

    printf("Enter [str] [int]\n");
    printf(">>> ");
    scanf("%s %d", str, &i);

    printf("---> %s %d\n", str, i);
}

// https://learn.microsoft.com/en-gb/cpp/c-runtime-library/reference/fgetc-fgetwc?view=msvc-170#example
void crt_fgetc()
{   
    FILE *stream;
    char buffer[81];
    int i;
    int ch; 

    // open the file
    stream = fopen("fgetc.txt", "r");
    if (stream == NULL) {
        perror("File 'fgetc.txt' not found, error: ");
        exit(1);
    }

    // read 80 char in place in buffer
    ch = fgetc(stream);
    for (i = 0; (i < 80) && (feof(stream) == 0); i++) {
        buffer[i] = (char) ch;
        ch = fgetc(stream);
    }

    // add null to buffer
    buffer[i] = '\0';
    printf("%s\n", buffer);
    fclose(stream);
}

void crt_fgetc_putchar()
{
    FILE *stream;
    char buffer[81];
    int i;
    int ch;

    stream = fopen("fgetc.txt", "r");
    if (stream == NULL) {
        perror("File 'fgetc.txt' not found, error: ");
        exit(1);
    }

    ch = fgetc(stream);
    for (i = 0; i  < 80; i++) {
        if (feof(stream) != 0)
            break;
        buffer[i] = (char) ch;
        ch = fgetc(stream);
    }
    fflush(stream);
    buffer[i] = '\0';
    
    char *p;
    ch = 0;

    for (p = buffer; ch != EOF; p++) {
        if (*p == '\0')
            break;
        ch = putchar( *p );
    }
    
    putchar('\n');

    fclose(stream);

}


int main(int argc, char *argv[])
{
    //getchar__putchar();
    // crt_getchar();
    //crt_putchar();
    //crt_fgetc();
    crt_fgetc_putchar();

    //printf__scanf();

    return 0;
}