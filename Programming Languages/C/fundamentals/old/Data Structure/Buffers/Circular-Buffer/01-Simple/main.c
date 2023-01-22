#include <stdio.h>
#include <stdlib.h>

#include "circular_buffer.h"

void flushBuffer(void *data)
{
    /*
    Deletes all data from Buffer | Call back meant to be called by circularbuffer_destroy()
    */
    data = 0;
}


int main(int argc, char **arcv) 
{

    CircularBuffer *cb = circularbuffer_initialize(10, (void *)'0');
    int i;

    // Load Buffer up to 20  (Max 10 Char)
    for (i=0; i<10; i++) {
        printf("%c\n", 'A' + i);
        circularbuffer_add(cb, (void *)('A' + i));
    }
      
        
    
    // Read Buffer
    for (i=0; i<11; i++)
        printf("%d: %c\n", i, circularbuffer_read(cb));

    printf("============ < ADDING MORE DATA TO BUFFER :) > ===========");
    
    int off_set = 10;
    // Load Buffer up to 40
    for (i=0; i<1; i++) 
        circularbuffer_add(cb, (void *)('A' + i + off_set));

    // Read Buffer
    for (i=0; i<11; i++)
        printf("%d: %c\n", i, circularbuffer_read(cb));

    printf("============ < ADDING MORE DATA TO BUFFER :) > ===========");

    int off_set2 = 11;
    // Load Buffer up to 40
    for (i=0; i<1; i++) 
        circularbuffer_add(cb, (void *)('A' + i+ off_set2));

    // Read Buffer
    for (i=0; i<11; i++)
        printf("%d: %c\n", i, circularbuffer_read(cb));

    // Destroy Buffer.
    circularbuffer_destroy(cb, flushBuffer);

    // Destroy local Handle
    free(cb);


    return (0);
}


// ===================== < CIRCULAR BUFFER FUNCTIONS DEFINITIONS > ===================== //

CircularBuffer* circularbuffer_initialize(size_t size, void *val)
{
    size_t i;

    // -------------------------- > MEMORY ALLOCATION 
    CircularBuffer *cb = (CircularBuffer *) malloc(sizeof (CircularBuffer));


    if (cb == NULL) { // ERROR HANDLING 
        printf("\nError: Insufficient memory. Programm Terminating...");
        exit(EXIT_FAILURE);
    }

    cb->buffer = (Item *) calloc(size, sizeof (Item));


    if (cb->buffer == NULL) {  // ERROR HANDLING 
        printf("\nERROR: Insufficient memory. Terminating...");
        exit(EXIT_FAILURE);
    }
    // ---------------------------------------------


    for (i=0; i<size; i++) 
        cb->buffer[i].data = val;

    cb->size = size;
    cb->start = 0;
    cb->end = 0;

    return(cb);
}


int circularbuffer_add(CircularBuffer *cb, void *val) 
{   
    // Set Last Item to End (FIFO)
    cb->buffer[ cb->end ].data = val;
    cb->end = (cb->end + 1) % cb->size;

    if (cb->end == cb->start)
        cb->start = (cb->start + 1) % cb->size;

    return(1);
}

void* circularbuffer_read(CircularBuffer *cb)
{
    size_t start = cb->start;
    cb->start = (cb->start + 1) % cb->size;  // Adding (start) cursor to the next item

    return(cb->buffer[start].data);
}


int circularbuffer_destroy(CircularBuffer *cb, circularbuffer_destroybuffer df)
{
    size_t i;

    for (i=0; i < cb->size; i++) {  // Delete each elemen in Buffer
        df(cb->buffer[i].data);  
    }

    free(cb->buffer);
    return(1);

}