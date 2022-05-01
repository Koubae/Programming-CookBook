#include <stdio.h>

#include "queue.h"
#include "queue.c"


// ---------------------- FUNCTION CALLBACK

int call_back_func_Printer(int idx, void *data)
{
    printf("%d: %c", idx, (char*) data);
    return 1;
}


int call_back_func_Delete(void *data)
{
    data = 0;
    return 1;
}


int main (int argc, char **argv)
{

    struct Queue queue = queue_Init();

    int i = 0;
    // ---------------------- Add Values to Queue
	for(i=0; i < 5; i++){
		queue_Push( & queue, (void *)('a' + i) );
	}

    // ---------------------- Print out the queue
	queue_Loop(&queue, call_back_func_Printer);
	printf("\n==============================\n");

	// ---------------------- Pop Item
	for(i=0; i < 5; i++){
		queue_Pop(&queue, call_back_func_Delete);
	}

	// ---------------------- Print out the queue
	queue_Loop(&queue, call_back_func_Printer);
	printf("\n==============================\n");

	// ---------------------- Add Values to Queue & Get Next Value in front 
	queue_Push(&queue, (void *) 'z');
	printf("Front: %c\n", (char *) queue_Next(&queue));

	// ---------------------- Delete All Values in Queue
	queue_DeleteAll(&queue, call_back_func_Delete);

    
    return 0;
}