/*
	Singly linked list Implementation
    @Author: Federico Baú 
    @Date: 02 - Jan 2021
    
*/

#ifndef __LINKEDLIST_C__
#define __LINKEDLIST_C__

#include <stdio.h>
#include <stdlib.h>

#include "linked_list.h"



// ================= < ListItem's Functions Definitions > ================= //


ListItem * list_item_Init()
/*
	Allocate New memory to ListItem Object 
	Returns: ListItem Pointer
*/
{	
	ListItem *list_item = malloc(sizeof (ListItem));
	if ( list_item == NULL) {
		printf("\nERROR: Insufficient memory. Terminating...");
        exit(EXIT_FAILURE);   
	}

	list_item->next = 0; // Set next Node to 0
	return list_item;
}


int list_item_Remove(ListItem *list_item, list_item_CallbackFunctionRemove call_back_Remove)
{
	return (call_back_Remove(list_item->data));
}


int list_item_Add(ListItem *list_item, void *data)
{
	list_item->data = data;
	return 1;
}

// ================= < LinkedList's Functions Definitions > ================= //

LinkedList linked_list_Init()
{
	LinkedList linked_list = { NULL };
	return linked_list;
}


int linked_list_AddItemEnd(LinkedList *linked_list, ListItem * list_item)
/*
	Add Item at end of list.
	Returns: 1 if Succesful 0 For Unsucessful
*/
{ 
	ListItem *next_item = linked_list->head; // Get the List Head

	if (!linked_list->head) { // Check if Head was set already set
		linked_list->head = list_item;
		return 1;
	} else {
		while (next_item->next) { // Iterate to the List end
			next_item = next_item->next;
		}

		if (!list_item->next) next_item->next = list_item; // End of list Connect last item with head
		else return 0;

		return 1;
	}

}


int linked_list_AddItemAfter(LinkedList *linked_list, int idx,  ListItem *list_item)
/*
	Add Item after a given Index (To the Right) into the list.
	Returns: 1 if Succesful 0 For Unsucessful
*/
{
	ListItem *next_item = linked_list->head; // Get the List Head

	while (idx > 0) { // Move cursor to given index
		if (!next_item->next) { // Index Not in Table
			return 0;
		} else {
			next_item = next_item->next;
			idx--;
		}
	}

	if (next_item->next) { // check if Cursor is within the List or at the end 

		if (!list_item->next) {
			ListItem *tmp_item = list_item_Init(); // 1. Create Temp Linked-List obj.
			tmp_item = next_item->next; // 2. Save next Item into the Temp item
			next_item->next = list_item;  // 3. Add next item as current item's next pointer
			list_item->next = tmp_item; // 4. Save Temp next item into current next
		} else return 0;

	} else if (!next_item->next){ // Cursor end of list

		if (!list_item->next) next_item->next = list_item;
		else return 0;

	}

	return 1;
}


int linked_list_AddItemBefore(LinkedList *linked_list, int idx,  ListItem *list_item)
/*
	Add Item before a given Index (To the Right) into the list.
	Returns: 1 if Succesful 0 For Unsucessful
*/
{
	ListItem *next_item = linked_list->head; // Get the List Head

	while (idx-1 > 0) { // Move cursor to before index
		if (!next_item->next) { // Index Not in Table
			return 0;
		} else {
			next_item = next_item->next;
			idx--;
		}
	}

	if (next_item->next) { // check if Cursor is within the List or at the end 

		if (!list_item->next) {
			ListItem *tmp_item = list_item_Init(); // 1. Create Temp Linked-List obj.
			tmp_item = next_item->next; // 2. Save next Item into the Temp item
			next_item->next = list_item;  // 3. Add next item as current item's next pointer
			list_item->next = tmp_item; // 4. Save Temp next item into current next
		} else return 0;

	} else if (!next_item->next){ // Cursor end of list

		if (!list_item->next) next_item->next = list_item;
		else return 0;

	}

	return 1;

}


int linked_list_Remove(LinkedList *linked_list, list_item_CallbackFunctionRemove call_back_Remove)
{
	while (1) { // Loop To entire List and remove each Item
		if (linked_list_RemoveHead(linked_list, call_back_Remove)) {

			if (!linked_list->head) break;
			else return 0;

		} else return 0;
	}
	return 1;
}


int linked_list_RemoveHead(LinkedList *linked_list, list_item_CallbackFunctionRemove call_back_Remove) 
{
	if (linked_list->head) {
		ListItem *tmp_head = linked_list->head; // Temporary list's head

		if (list_item_Remove(tmp_head, call_back_Remove)) {
			linked_list->head = tmp_head->next;
			free(tmp_head);
			return 1;
		} else return 0;
	} else return 1; // List is Already Empty
}


int linked_list_RemoveTail(LinkedList *linked_list, list_item_CallbackFunctionRemove call_back_Remove)
{
	ListItem *next_item = linked_list->head; // Temp iterator

	while (next_item->next) { // Move at the end of the list

		if (!next_item->next->next) {
			if (list_item_Remove(next_item->next, call_back_Remove)) {
				free(next_item->next);
				next_item->next = 0;
				return 1;
			} else return 0;			
		} else next_item = next_item->next;			
	}
	return 0;
}


int linked_list_RemoveAt(LinkedList *linked_list, int idx, list_item_CallbackFunctionRemove call_back_Remove)
{
	ListItem *next_item, *last_item;

	// Check if there is a head or if index given is the head
	if (!linked_list->head) return 1; 
	if (idx == 0 && !linked_list->head->next) return linked_list_RemoveHead(linked_list, call_back_Remove);

	next_item = linked_list->head;
	last_item = NULL;

	while (idx-1 > 0) { // Move Cursor to Index
		if (!next_item->next) return 0; // Idex Not exists
		else { // Move forward to next
			last_item = next_item; 
			next_item = next_item->next;
		}
		idx--;
	}

	if (!next_item->next) {// if we readched the end of list
		free(next_item);
		return 1;
	} else { // Not end of list
		last_item->next = next_item->next;
		free(next_item);
		return 1;
	}
}

int linked_list_Loop(LinkedList *linked_list, list_item_CallbackFunction call_back)
{
	ListItem *next_item;
	if (!linked_list->head) return 0; 

	next_item = linked_list->head;
	int idx = 0;
	while (next_item) {
		call_back(idx, next_item->data);
		next_item = next_item->next;
		idx++;
	}
	return 1;

}


// Returns the ListItem Data given a Linked List and Index (void *).
void* linked_list_Get(LinkedList *linked_list, int idx)
{
	ListItem *next_item;
	if (!linked_list->head) return (void *)1;
	if (idx == 0) return (void *) linked_list->head->data;

	next_item = linked_list->head;
	while (idx > 0) { // Iterate to the given index

		if (!next_item->next) return (void *)-1;
		else next_item = next_item->next;
		idx--;
	}
	return next_item->data;
}


// Returns int the gets ListItem Data gicen a Linked List and Index (void *) and update it
int linked_list_Set(LinkedList *linked_list, void *data, int idx) 
{
	ListItem *next_item;
	if (!linked_list->head) return 0;
	if (idx == 0) {
		linked_list->head->data = data;
		return 0;
	} 

	next_item = linked_list->head;

	while (idx > 0 ) { // Iterate to the given index 

		if (!next_item->next) return 0;
		else next_item = next_item->next;

		idx--;
	}

	if (list_item_Add(next_item, data)) return 1;

	return 0;
}

#endif