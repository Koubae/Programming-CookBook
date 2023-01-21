#ifndef __QUEUE_H__
#define __QUEUE_H__

// ---------------------- STRUCTURES

struct QueueNode {
    struct QueueNode *next;
    void *data;
} QueueNode;


struct Queue {
    struct QueueNode *head;
    int size;
} Queue;


// ---------------------- FUNCTION POINTERS

typedef int (*queue_CallBackFunction)(int, void *);
typedef int (*queue_CallBackFunctionPop)(void *);

struct Queue queue_Init();

// ---------------------- FUNCTION PROTOTYPES

// Add a QueueNode Item of any value to the Rear Queue
int queue_Push(struct Queue *, void *);


// Removes & Returns the first Item Added in Queue (FIFO).
int queue_Pop(struct Queue *, queue_CallBackFunctionPop);


// Return next item's in queue data 
void* queue_Next(struct Queue *);


// Util Function, loops the entire Queue (Used to all the Item in the queues).
void queue_Loop(struct Queue *, queue_CallBackFunction);


// Delete All data from Queue
int queue_DeleteAll(struct Queue *, queue_CallBackFunctionPop);

#endif
