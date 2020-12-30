#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <assert.h>

#include "circular_buffer.h"
#include "circular_buffer.c"

#define BUFFER_SIZE 10

void print_buffer_status(buffer_handle buffer);

int main(void)
{
    uint8_t *buffer = malloc(BUFFER_SIZE * sizeof (uint8_t));

    printf("\n=== C Circular Buffer Check ===\n");

    buffer_handle buffer = circular_buffer_init(buffer, BUFFER_SIZE); // Circular Buffer Init
    printf("Buffer initialized.\n ");
	print_buffer_status(buffer);

    // --------------------------------> Adding 9 Values
    printf("\n******\nAdding %d values\n", BUFFER_SIZE - 1);
    for(uint8_t i = 0; i < (BUFFER_SIZE - 1); i++) {
		circular_buffer_put(buffer, i);
		printf("Added %u, Size now: %zu\n", i, circular_buffer_size(buffer));
	}
    print_buffer_status(buffer);
    // ----------------------------------

    // --------------------------------> Adding 10 Values
    printf("\n******\nAdding %d values\n", BUFFER_SIZE);
	for(uint8_t i = 0; i < BUFFER_SIZE; i++)
	{
		circular_buffer_put(buffer, i);
		printf("Added %u, Size now: %zu\n", i, circular_buffer_size(buffer));
	}
	print_buffer_status(buffer);
    // ----------------------------------


    // --------------------------------> Reading From Buffer
    printf("\n******\nReading back values: ");
	while(!circular_buffer_empty(buffer))
	{
		uint8_t data;
		circular_buffer_get(buffer, &data);
		printf("%u ", data);
	}
	printf("\n");
    print_buffer_status(buffer);
    // ----------------------------------

    // --------------------------------> Adding 15 Values
    printf("\n******\nAdding %d values\n", BUFFER_SIZE + 5);
	for(uint8_t i = 0; i < BUFFER_SIZE + 5; i++)
	{
		circular_buffer_put(buffer, i);
		printf("Added %u, Size now: %zu\n", i, circular_buffer_size(buffer));
	}
	print_buffer_status(buffer);
     // ----------------------------------


    // --------------------------------> Reading From Buffer
	printf("\n******\nReading back values: ");
	while(!circular_buffer_empty(buffer))
	{
		uint8_t data;
		circular_buffer_get(buffer, &data);
		printf("%u ", data);
	}
	printf("\n");
    // ----------------------------------



    // --------------------------------> Adding 15 Values Method 2 
    printf("\n******\nAdding %d values using non-overwrite version\n", BUFFER_SIZE + 5);
	for(uint8_t i = 0; i < BUFFER_SIZE + 5; i++)
	{
		circular_buffer_put2(buffer, i);
	}
	print_buffer_status(buffer);
    // ----------------------------------

    // --------------------------------> Reading From Buffer
	printf("\n******\nReading back values: ");
	while(!circular_buffer_empty(buffer))
	{
		uint8_t data;
		circular_buffer_get(buffer, &data);
		printf("%u ", data);
	}
	printf("\n");
    // ----------------------------------

    free(buffer);
	circular_buffer_free(buffer);


}

void print_buffer_status(buffer_handle buffer)
{
    printf("Full -> %d  | Empty -> %d  | Size -> %zu\n",
            circular_buffer_full(buffer),
            circular_buffer_empty(buffer),
            circular_buffer_size(buffer));
}