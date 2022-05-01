/*
    > Hash Table implemented with Singly Linked List.
    > Collisions are handled with  Separate chaining with linked lists

    @Author: Federico Baú 
    @Date: 21/12/2020
    
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TABLE_SIZE 20000

// STRUCTURE OF EACH ENTRY WITHIN THE HASH TABLE
typedef struct mapped_entry 
{
    char *key;
    char *value;
    struct mapped_entry *next;
    
} mapped_entry;


// HASH TABLE 
typedef struct
{
    mapped_entry **map_node;
} HASH_TABLE;


unsigned int hash(const char *key) 
{
    unsigned long int hash_value = 0;
    unsigned int i = 0; // Why unsigned? for the size and not negative?
    unsigned int key_len = strlen(key);

    // QST??? What does this? Why 37??
    for (; i<key_len; ++i) {
        hash_value = hash_value*37 + key[i]; // Gets the Unicode Number (if char) or int
    }

    // Check that Value is between 0 and size TABLE_SIZE
    hash_value = hash_value % TABLE_SIZE;
    return hash_value;
}

mapped_entry *hashTable_pair(const char *key, const char *value)
/*

*/
{
    // Allocate Entry memory
    mapped_entry *entry = malloc(sizeof (mapped_entry) *1);
    entry->key = malloc(strlen(key) + 1);
    entry->value = malloc(strlen(value) + 1 );


    // Copy Key, value in place
    strcpy(entry->key, key);
    strcpy(entry->value, value);

    // Set neighbour node to Null (may be re-set later if neighbour exists);
    entry->next = NULL;

    return entry;
}

HASH_TABLE* hashTable_create(void)
/*
    Creates a New Table with as many nodes as the TABLE_SIZE number.
    Each Node is an Array of Pointer set to Null
    returns -> HashTable instance.
*/
{
    // Allocate Table
    HASH_TABLE *hashtable = malloc(sizeof (HASH_TABLE) * 1);

    // Allocate Table map
    /*
        NOTE: We use mapped_entry* instead of mapped_entry so that we take the size of the pointer (4 bit) and not of the Struct (12) of better memory management
    */
    hashtable->map_node = malloc(sizeof (mapped_entry*) * TABLE_SIZE);
    
    // Set each map_node to Null (Better operation)
    int i = 0;
    for (; i < TABLE_SIZE; i++) {
        hashtable->map_node[i] = NULL;
    }

    return hashtable;

}

// TODO: value can be not const?
void hashTable_set(HASH_TABLE *hashtable, const char *key, const char *value)
/*
    Add a new (key, value) pair into The Hash Table.
    Variable slot: Get Hash Value using a deterministic Value based on the char unicode 
    Arguments:
        hashtable (HASH_TABLE) The Instance created of the Hash Table 
        key (const char) is an ummutable data tape and must be Unique.
        Value (consta char) A value 
*/
{
    unsigned int slot = hash(key);  
    mapped_entry *entry = hashtable->map_node[slot];

    if (entry == NULL) {  // no entry means slot empty, insert immediately
        hashtable->map_node[slot] = hashTable_pair(key, value);
        // printf("Here %s \n", hashtable->map_node[slot]->value);
        return;
    } else {
        mapped_entry *prev; // set previous pointer

        //  walk through each entry until either the end reached or a matching key is found
        while (entry != NULL) {
            if (strcmp(entry->key, key) == 0) { // iF is found replace old value wiht new
                free(entry->value); // Free memory
                entry->value = malloc(strlen(value) + 1);
                strcpy(entry->value, value);
                return; 
            }
        }
        // end of chain reached without a match, add new
        prev->next = hashTable_pair(key, value);
    }   
    
}

char *hashTable_get(HASH_TABLE *hashtable, const char *key)
{
    unsigned int slot = hash(key);

    // Find Valid Slot
    mapped_entry *entry = hashtable->map_node[slot];

    // NO slot = None
    if (entry == NULL) {
        return NULL;
    } else {
        // walk through each entry in the slot
        while (entry != NULL) {
            if (strcmp(entry->key, key) == 0) {
                return entry->value;
            } else {
                entry = entry->next; //         // proceed to next key if available
            }
        }
        return NULL;
    }
}

char *hashTable_del(HASH_TABLE *hashtable, const char *key)
{
    unsigned int bucket = hash(key);

    mapped_entry *entry = hashtable->map_node[bucket];  // try to find a valid bucket

    if (entry == NULL) {
        return 0;
    } else {
        mapped_entry *prev;
        int idx = 0;
        // walk through each entry until either the end is reached or a matching key is found
        while (entry != NULL) {
            // check key
            if (strcmp(entry->key, key) == 0) {               
                if (entry->next == NULL && idx == 0) {  // first item and no next entry
                    hashtable->map_node[bucket] = NULL;
                }               
                if (entry->next != NULL && idx == 0) {  // first item with a next entry
                    hashtable->map_node[bucket] = entry->next;
                }               
                if (entry->next == NULL && idx != 0) {  // last item
                    prev->next = NULL;
                }               
                if (entry->next != NULL && idx != 0) {  // middle item
                    prev->next = entry->next;
                }             
                free(entry->key);    // free the deleted entry
                free(entry->value);
                free(entry);
                return 0;
            }            
            prev = entry; // walk to next
            entry = prev->next;
            ++idx;
        }
    }

}


void hashTable_showEntry(HASH_TABLE *hashtable)
{
    for (int i = 0; i < TABLE_SIZE; ++i) {
        mapped_entry *entry = hashtable->map_node[i];

        if (entry == NULL) {
            continue;
        }

        printf("slot[%4d]: ", i);

        for(;;) {
            printf("%s = %s ", entry->key, entry->value);

            if (entry->next == NULL) {
                break;
            }

            entry = entry->next;
        }

        printf("\n");
    }
}

int main(int argc, char **argv) 
{
    HASH_TABLE *hash_table = hashTable_create();

    hashTable_set(hash_table, "naame1", "em");
    hashTable_set(hash_table, "name2", "russian");
    hashTable_set(hash_table, "name3", "pizza");
    hashTable_set(hash_table, "name4", "doge");
    hashTable_set(hash_table, "name5", "pyro");
    hashTable_set(hash_table, "name6", "joost");
    hashTable_set(hash_table, "name7", "kalix");

    hashTable_showEntry(hash_table);

    return 0;
}