#ifndef CIRCULAR_BUFFER_H_
#define CIRCULAR_BUFFER_H_

#include <stdbool.h>

// Opaque struct
typedef struct CircularBuffer CircularBuffer;


// CircularBuffer Handle
typedef CircularBuffer *buffer_handle;

/* *************
    Init Circular Buffer in an empty states
    Arguments: 
            (uint8_t) Buffer ! NULL
            (size_t)  size > 0
    Returns:
            Circular Buffer Handle
*****************/ 
buffer_handle circular_buffer_init(uint8_t *buffer, size_t size);


/* *************
    Free a Circular Buffer Structure
    Arguments:  
            buffer (buffer_handle)
    Note:
        Doesn't free up data buffer
^*****************/
void circular_buffer_free(buffer_handle buffer);


/* **************
    Resets the Circular Buffers and makes it empty.
    Arguments:  
            buffer (buffer_handle)
*****************/
void circular_buffer_reset(buffer_handle buffer);

/* ************
    Ver 1 -> Continues to put data if buffer is full, deleting the oldest one FIFO
    Old Data is Overwritten
    Arguments:  
            buffer (buffer_handle)
            data (uint8_t)
******************/
void circular_buffer_put(buffer_handle buffer, uint8_t data);

/* *****************
    Ver 2 -> Rejects Data if Buffer is Full
    Arguments:  
            buffer (buffer_handle)
            data (uint8_t)
    Return:
        0 -> Succes || -1 Buffer full
*********************/
int circular_buffer_put2(buffer_handle buffer, uint8_t data);


// Get a Value from buffer, Returns 0 success | -1 Buffer empty
int circular_buffer_get(buffer_handle buffer, uint8_t *data);


// Checks if Buffer is Empty (bool) 
bool circular_buffer_empty(buffer_handle buffer);

// Checls if Buffer is Full
bool circular_buffer_full(buffer_handle buffer);


// Checks the max Buffer capacity
size_t circular_buffer_capacity(buffer_handle buffer);

// Checks N of Element in Currently Stored in Buffer
size_t circular_buffer_size(buffer_handle buffer);


#endif  // circular_bufferFER_H_