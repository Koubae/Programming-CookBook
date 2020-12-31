#ifndef __CIRCULARBUFFER_H__
#define __CIRCULARBUFFER_H__

typedef void (* circularbuffer_destroybuffer)(void *); // Function prototype --> Function Pointer + 1 void pointer argument | Function callback


typedef struct Item 
{
    void *data;
} Item;

typedef struct CircularBuffer
{
    size_t size;
    size_t start;
    size_t end;
    Item *buffer;
} CircularBuffer;



/*********************
Returns Initialized CircularBuffer instance of size 'size_t' 
And all items initialized to second parameter
*********************/
CircularBuffer* circularbuffer_initialize(size_t, void *);


// * Overwrites oldest item in buffer.
int circularbuffer_add(CircularBuffer *, void *);


// * Returns oldest item from buffer.
void * circularbuffer_read(CircularBuffer *);


// * Flush and destroy the buffer.
int circularbuffer_destroy(CircularBuffer *, circularbuffer_destroybuffer);


#endif