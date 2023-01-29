#include <stdio.h>
#include <stdlib.h>
#include <string.h>

const char FILE_NAME[] = "2_file_handling.txt"; 

/**
 * 
    // There are 3 functions to write into a file
    // fprintf
    // fputc
    // fputs
    // fwrite
*/
void writeIntoTextFile()
{
    printf("\n---------------------- < writeIntoTextFile > ----------------------\n");

    const char *data[] = { 
        "Line 1",
        "Line 2",
        "Line 3"
    };

    FILE *file; 
    if ((file = fopen(FILE_NAME, "w")) == NULL) {
        char error[200];
        snprintf(error, sizeof error, "Error opening file %s, error: ", FILE_NAME);
        perror(error);
        exit(1);
    }


    // fprintf   
    for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++) {
        char line[sizeof(data[0])];
        strcpy(line, data[i]);
        fprintf(file, "- fprintf = %s\n", line);        
    }
    fflush(file);

    // fputc
    for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++) {
        char line[sizeof(data[0]) + 20];
        snprintf(line, sizeof line, "- fputc = %s\n", data[i]);
        for (int y = 0; y < sizeof(line); y++) {
            if (line[y] == '\0')
                break;
            fputc(line[y], file);
        }
    }
    fflush(file); 


    // fputs
    for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++) {
        char line[sizeof(data[0]) + 20]; 
        snprintf(line, sizeof line, "- fputs = %s\n", data[i]);
        fputs(line, file);
    }
    fflush(file);

    // fwrite for fwrite is bit different
    // we need to build the final string in memory and then add it all in once!
    char lines[sizeof(data) * 100];
    for (int i = 0; i < sizeof(data) / sizeof(data[0]); i++) {
        char line[sizeof(data[0]) + 20];
        snprintf(line, sizeof line, "- fwrite = %s\n", data[i]);
        // concatenate string
        strcat(lines, line);

    }
    fwrite(lines, sizeof(lines[0]), sizeof(lines), file); 

    fflush(file);


    fclose(file);
}


/**
 * 
    // There are 3 functions to read into a file
    // fscanf
    // getc
    // fgetc
    // fgets
    // fread
*/
void readFromTextFIle()
{
    const int BUFFER_SIZE = 1024;

    printf("\n---------------------- < readFromTextFIle > ----------------------\n");

    FILE *file;
    if ((file = fopen(FILE_NAME, "r")) == NULL) {
        char error[200];
        snprintf(error, sizeof error, "Error openin file %s, error: ", FILE_NAME); 
        perror(error);
        exit(-1);
    }
    // fscanf
    printf("\n ****** fscanf: \n");
    char buffer[BUFFER_SIZE];
    fscanf(file, "%s", buffer);
    printf("%s\n", buffer);
    fseek(file, 0, SEEK_SET);

    // fgetc
    printf("\n ****** getc: \n");
    char charValue1;
    while ( ( charValue1 = getc(file)) != EOF ) {
        printf("%c", charValue1);
    }
    fseek(file, 0, SEEK_SET);

    // fgetc
    printf("\n ****** fgetc: \n");
    int charValue2; 
    /*while (1) {  // more readable ???
        charValue = fgetc(file);
        if (feof(file)) 
            break;
        printf("%c", charValue);
    }*/
    while ((charValue2 = fgetc(file)) && !feof(file)) {
        printf("%c", charValue2);
    }
    fseek(file, 0, SEEK_SET);

    // fgets
    
    char buffer2[BUFFER_SIZE];
    printf("\n ****** fgets: \n");
    while (fgets(buffer2, BUFFER_SIZE, file) != NULL) 
        printf("%s", buffer2);

    fseek(file, 0, SEEK_SET);

    fclose(file);
}



int main(void)
{
    writeIntoTextFile();
    readFromTextFIle();


    return 0;
}