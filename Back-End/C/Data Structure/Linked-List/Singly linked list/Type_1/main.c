/*
	
    Singly linked list example Programm
    @Author: Federico Baú 
    @Date: 02 - Jan 2021
    
*/

#include <stdio.h>
#include <stdlib.h>

#include "linked_list.h"
#include "linked_list.c"

void main_linked_list_Print(int idx, void *data) 
{
    printf("%d: %d, ", idx, (int) data);
}

int main_linked_list_Delete(void *data) 
{
    return 1;
}

int main(int argc, char **argv) 
{
    
    LinkedList linked_list;
    ListItem *list_item; 

    linked_list = linked_list_Init(); 

    int data;
    for (data = 0; data < 10; data++) { // Add Item into list (at the end) type int casted to void* 
        list_item = list_item_Init();
        list_item_Add(list_item, (void *) data);
        linked_list_AddItemEnd(&linked_list, list_item);
    }

    // ================ < Print Values > ================ // 
	linked_list_Loop(&linked_list, main_linked_list_Print);
	printf("\n=============================\n");

    // ================ < Add item after first one > ================ // 
	list_item = list_item_Init();
	list_item_Add(list_item, (void *) -1 );
	linked_list_AddItemAfter(& linked_list, 0, list_item);

    // ================ < Add item after Before second one > ================ // 
    list_item = list_item_Init();
	list_item_Add(list_item, (void *) -2 );
	linked_list_AddItemBefore(& linked_list, 2, list_item);

    // ================ < Print Values > ================ // 
    linked_list_Loop(& linked_list, main_linked_list_Print);
	printf("\n=============================\n");

    // ================ < Remove Head | Tail | At > ================ // 
    linked_list_RemoveHead(& linked_list, main_linked_list_Delete);
	linked_list_RemoveTail(& linked_list, main_linked_list_Delete);
	linked_list_RemoveAt(& linked_list, 5, main_linked_list_Delete);


    // ================ < Set > ================ // 
    linked_list_Set(& linked_list, (void *) 100, 7);

    // ================ < Print Values > ================ // 
    linked_list_Loop(& linked_list, main_linked_list_Print);
	printf("\n=============================\n");


    // ================ < Remove List > ================ // 
	linked_list_Remove(& linked_list, main_linked_list_Delete);

    return 0;
}   

