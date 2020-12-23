#include <stdio.h>
#include <string.h>

int main()
{
    char str1[20] = "C programming";
    char str2[20];

    // Copy str1 to str2
    strcpy(str2, str1);

    puts(str2);
    return 0;
}



// shows the usage of fgets() function
#include <stdio.h>

int main () {
    FILE *fp;
    char str[60];

    /* opening file for reading */
    fp = fopen("file.txt" , "r");
    if(fp == NULL) {
        perror("Error opening file");
        return(-1);
    }
    if( fgets (str, 60, fp)!=NULL ) {
        /* writing content to stdout */
        puts(str);
    }
    fclose(fp);
    
    return(0);
}

// fgets() and puts()
#include <stdio.h>
int main()
{
    char name[30];
    printf("Enter name: ");
    fgets(name, sizeof(name), stdin);  // read string
    printf("Name: ");
    puts(name);    // display string
    return 0;
}



//Passing string to a Function
#include <stdio.h>

void displayString(char str[]);

int main ()
{
    char my_string[50];
    printf("Enter a string:");

    fgets(my_string, sizeof(my_string), stdin);
    displayString(my_string);
    return 0;
}

void displayString(char str[])
{
    printf("String Output: ");
    puts(str);
}

// Strings and Pointers
#include <stdio.h>

int main(void) {
    char name[] = "Harry Potter";

    printf("%c", *name);     // Output: H
    printf("%c", *(name+1));   // Output: a
    printf("%c", *(name+7));   // Output: o

    char *namePtr;

    namePtr = name;
    printf("%c", *namePtr);     // Output: H
    printf("%c", *(namePtr+1));   // Output: a
    printf("%c", *(namePtr+7));   // Output: o
}

// ========= strlen() ======================= // 

#include <stdio.h>
#include <string.h>
int main()
{
    char a[20]="Program";
    char b[20]={'P','r','o','g','r','a','m','\0'};

    // using the %zu format specifier to print size_t
    printf("Length of string a = %zu \n",strlen(a));
    printf("Length of string b = %zu \n",strlen(b));

    return 0;
}

// ==== < strcat() > ==== //

// char *strcat(char *destination, const char *source)
#include <stdio.h>
#include <string.h>
int main() {
    char str1[100] = "This is ", str2[] = "c_programming";

    // concatenates str1 and str2
    // the resultant string is stored in str1.
    strcat(str1, str2);

    puts(str1);
    puts(str2);

    return 0;
}
//This is c_programming
//c_programming


// ==== < strcmp() > ==== //
// int strcmp (const char* str1, const char* str2);



//Sort strings in the dictionary order
#include <stdio.h>
#include <string.h>

int main ()
{
    char str[5][50], temp[50];
    printf("Enter 5 words: ");

    for (int i=0; i<5; ++i){
        fgets(str[i], sizeof(str[i]), stdin);
    }

    for (int i=0; i<5;++i) {
        for (int j=i+1; j<5;++j) {
            if (strcmp(str[i], str[j]) > 0) {
                strcpy(temp, str[i]);
                strcpy(str[i], str[j]);
                strcpy(str[j], temp);
            }
        }
    }
    printf("\nIn the lexicographical order: \n");
    for (int i=0; i<5;++i) {
        fputs(str[i], stdout);
    }
}
