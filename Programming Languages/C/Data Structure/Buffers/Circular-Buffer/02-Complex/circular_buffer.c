#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <assert.h>

#include "circular_buffer.h"

// Hidden Definition of circular Buffer 
struct CircularBuffer 
{   
    uint8_t *buffer;
    size_t head;
    size_t tail;
    size_t max;
    bool full;
};

#pragma mark - Private Functions - 

static void advance_pointer(buffer_handle buffer)

{
    assert(buffer);

    if (buffer->full) {
        buffer->tail = (buffer->tail + 1) % buffer->max;
    }

    buffer->head = (buffer->head + 1) % buffer->max;
    buffer->full = (buffer->head == buffer->tail);
}


static void retreat_pointer(buffer_handle buffer)
{
    assert(buffer);

    buffer->full = false;
    buffer->tail = (buffer->tail +1 ) % buffer->max;
}



#pragma mark - APIs -

buffer_handle circular_buf_init(uint8_t *buffer_, size_t size)
{
    assert(buffer_ && size);

    buffer_handle buffer = malloc(sizeof (CircularBuffer));  // Init Circular Buffer Handle
    assert(buffer);

    buffer->buffer = buffer_; 
    buffer->max = size;

    circular_buffer_reset(buffer); // All Properties of buffer init to 0

    assert(circular_buffer_empty(buffer));  // Check current state of Buffer

    return buffer;
}


void circular_buffer_free(buffer_handle buffer)
{
    assert(buffer);
	free(buffer);
}


void circular_buffer_reset(buffer_handle buffer)
{
    assert(buffer);

    buffer->head = 0;
    buffer->tail = 0;
    buffer->full = false; 
}


size_t circular_buffer_size(buffer_handle buffer)
{
    assert(buffer);

	size_t size = buffer->max;

    if (!buffer->full) {
        if (buffer->head >= buffer->tail) 
            size = (buffer->head - buffer->tail);
        else 
            size = (buffer->max + (buffer->head - buffer->tail));

    }
    return size; 
}


size_t circular_buffer_capacity(buffer_handle buffer)
{
    assert(buffer);

	return buffer->max;
}


void circular_buffer_put(buffer_handle buffer, uint8_t data)
{
    assert(buffer && buffer->buffer);
    buffer->buffer[buffer->head] = data;

    advance_pointer(buffer);
}


int circular_buffer_put2(buffer_handle buffer, uint8_t data)
{
    int r = -1;

    assert(buffer && buffer->buffer);

    if(!circular_buffer_full(buffer)) {
        buffer->buffer[buffer->head] = data;
        advance_pointer(buffer);
        r = 0;
    }

    return r;
}


int circular_buffer_get(buffer_handle buffer, uint8_t *data)
{
    assert(buffer && data && buffer->buffer);

    int r = -1;

    if (!circular_buffer_empty(buffer)) {
        *data = buffer->buffer[buffer->tail];
        retreat_pointer(buffer);
        r = 0;
    }
    return r;
}


// ------- FLAGS

bool circular_buffer_empty(buffer_handle buffer)
{
    assert(buffer);
    return (!buffer->full && (buffer->head == buffer->tail));
}


bool circular_buffer_full(buffer_handle buffer)
{
    assert(buffer);
    return buffer->full;
}