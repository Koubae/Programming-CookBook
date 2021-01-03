/*
	Simple Queue Implementation 
    @Author: Federico Baú 
    @Date: 03 - Jan 2021
    
*/

#include <stdio.h>
#include <stdlib.h>

#include "queue.h"


struct Queue queue_Init()
{
    struct Queue queue = {0, 0};
    return queue;
} 


int queue_Push(struct Queue *queue, void *value)
{
    

    if (queue->size == 0) { // Check if Queue is empty 

        queue->head = malloc( sizeof (struct QueueNode));

        if (queue->head == NULL) {
            printf("\nERROR: Insufficient memory. Terminating...");
            exit(EXIT_FAILURE);
        } else {
            queue->head->next = 0;
            queue->head->data = value;
        }

    } else {
        
        struct QueueNode *temp_node;
        temp_node = queue->head;
        queue->head = malloc(sizeof (struct QueueNode));
        
        if (queue->head == NULL) {
            printf("\nERROR: Insufficient memory. Terminating...");
            exit(EXIT_FAILURE);
        } else {
            queue->head->next = temp_node;
            queue->head->data = value;
        }    
    }

    queue->size++;
    return 1;
}


int queue_Pop(struct Queue *queue, queue_CallBackFunctionPop cb_pop)
{
    struct QueueNode *next_item = queue->head; // Temp iterator
    if (queue->size == 0) return 0;
    else if (queue->size == 1) {

        if (cb_pop(queue->head->data)) {
            free(queue->head);
            queue->size--;
            return 1;
        } else return 0;

    }

    while (next_item->next) { // Move up to one Node before the last node (index[-2])
        if (!next_item->next->next) {
            if (cb_pop(next_item->next->data)) free(next_item->next);
            else return 0;
            printf("Hello World");
            next_item->next = 0;
            queue->size--;
            return 1;

        } else { 
            next_item = next_item->next;
        }
    }
    return 0;
}


void* queue_Next(struct Queue *queue)
{
    if (queue->size == 0) return (void *)0;
    struct QueueNode *temp_node = queue->head;

    while (temp_node->next) {
        temp_node = temp_node->next;
    }
    return temp_node->data;    
}


void queue_Loop(struct Queue *queue, queue_CallBackFunction cb_func)
{
    if (queue->size == 0) return;

    struct QueueNode *next = queue->head;

    int idx = 0;
    while (next) {
        cb_func(idx, next->data);
        idx++;
        next = next->next;
    }   
}


int queue_DeleteAll(struct Queue *queue, queue_CallBackFunctionPop cb_pop)
{
    struct QueueNode *next = queue->head;
    struct QueueNode *temp_node;

    while (next) {
        temp_node = next;
        next = next->next;

        if (cb_pop(temp_node->data)) free(temp_node);
        else return 0;
    }

    return 0;

}