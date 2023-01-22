#ifndef __LINKEDLIST_H__
#define __LINKEDLIST_H__

// ---------------------- Structures

typedef struct ListItem 
{
	struct ListItem *next;
	void *data;
} ListItem;

typedef struct LinkedList
{
	ListItem *head;
} LinkedList;



// ---------------------- FUNCTION POINTERS

typedef void (*list_item_CallbackFunction)(int, void *);
typedef int (*list_item_CallbackFunctionRemove)(void *);


// ---------------------- FUNCTION PROTOTYPES

// ----- *** ListItem *** declarations

ListItem * list_item_Init();

int list_item_Remove(ListItem *, list_item_CallbackFunctionRemove);

int list_item_Add(ListItem *, void *);


// ----- *** LinkedList *** declarations

LinkedList linked_list_Init();

// Add Item at end of list
int linked_list_AddItemEnd(LinkedList *, ListItem *);


// Add Item After a Given Index
int linked_list_AddItemAfter(LinkedList *, int,  ListItem *);

// Add Item Before a Given Index
int linked_list_AddItemBefore(LinkedList *, int,  ListItem *);

// Remove and free List
int linked_list_Remove(LinkedList *, list_item_CallbackFunctionRemove);

// Remove Linked List's Head
int linked_list_RemoveHead(LinkedList *, list_item_CallbackFunctionRemove);

// Remove Linked List's Tail
int linked_list_RemoveTail(LinkedList *, list_item_CallbackFunctionRemove);

// Remove and free a Linked List Node and Updates it
int linked_list_RemoveAt(LinkedList *, int, list_item_CallbackFunctionRemove);

// Loop through all Item in the List and applies the Callback function
int linked_list_Loop(LinkedList *, list_item_CallbackFunction);


// Returns the ListItem Data given a Linked List and Index (void *).
void* linked_list_Get(LinkedList *, int);


// Returns int the gets ListItem Data gicen a Linked List and Index (void *) and update it
int linked_list_Set(LinkedList *, void *, int);


// TODO: Delete this
void printer(char *);
#endif