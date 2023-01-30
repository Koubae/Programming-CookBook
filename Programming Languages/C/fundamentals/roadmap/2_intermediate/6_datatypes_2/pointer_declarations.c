// @credit:  https://learn.microsoft.com/en-us/cpp/c-language/pointer-declarations?view=msvc-170#examples


/*
The variable line has the structure type named list. 
The list structure type has three members: the first member is a pointer to a char value, 
the second is an int value, and the third is a pointer to another list structure.
*/
struct list
{
    char *token;
    int count;
    struct list *next;
} line;

/*
The variable record has the structure type id.
 pname is declared as a pointer to another structure type named name. 
 This declaration can appear before the name type is defined.
*/
struct id
{
    unsigned int id_no;
    struct name *pname;
} record;


struct name {
    char badge;
};

int main(void)
{

 /* Declares a pointer variable named message 
    The message pointer points to a variable with char type.
 */
char *message;

 /* Declares an array of pointers 
    The pointers array has 10 elements; each element is a pointer to a variable with int type.
 */
int *pointers[10]; 

/* Declares a pointer to an array of 10 elements
  The pointer variable points to an array with 10 elements. Each element in this array has int type.
 */
int (*pointer)[10]; 

/* Declares a pointer variable, x,
to a constant value 

The pointer x can be modified to point to a different int value, but the value to which it points can't be modified.
*/
int const *x;    

/* Uses the tag for list 
This example declares two pointer variables (next and previous) that point to the structure type list. This declaration can appear before the definition of the list structure type (see the next example), as long as the list type definition has the same visibility as the declaration.
*/
struct list *next, *previous; 


    return 0;
}