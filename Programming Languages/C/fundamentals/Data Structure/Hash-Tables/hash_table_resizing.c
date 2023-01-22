/*
    Hash Table implementation with Auto expansion given a certain amount of Collisions

    @Author: Federico Baù 
    @Date: 1/2/2021

*/

#ifndef __HASHTABLE_H__
#define __HASHTABLE_H__

typedef size_t (*hash_Function)(void * );
typedef size_t (*compare_Equal)(void *, void *);


typedef struct Node 
{
    void *key;
    void *value;
    struct Node *next;
} Node;

typedef struct HashTable 
{
    size_t size;
    size_t max_collisions;
    size_t growth_factor;
    Node **table;  // Array of pointer used to call next Node 
    hash_Function hashFunction;
    compare_Equal compareEqual;
}  HashTable;


/*
    Initialize HashTable and Returns an Object Instance of HashTabale

*/
HashTable* hashtable_Init(size_t, size_t, size_t, hash_Function, compare_Equal);


void * hashtable_Get(HashTable *, void *);


int hashtable_Destroy(HashTable *);


int hashtable_Resize(HashTable *, size_t);


int hashtable_Add(HashTable *, void *, void *);


int hashtable_Remove(HashTable *, void *);


#endif


#include <stdlib.h>
#include <stdio.h>


int main(int argc, char **argv) 
{
    printf("Hello Man\n");
    return 0;
}




HashTable *hashtable_Init(size_t size, size_t max_collision, size_t grow_factor, hash_Function h_function, compare_Equal c_equal)
{
    HashTable *hash_table = malloc(sizeof (HashTable));


    if (hash_table == NULL) {
        printf("\nERROR: Cannot create hash table. Terminating...");
        exit(EXIT_FAILURE); // TODO: Simple Err handler. 
    }

    // ----------------- Setting Up the HasTable's instance attr
    hash_table->hashFunction = h_function;
    hash_table->compareEqual = c_equal;
    hash_table->size = size;
    hash_table->max_collisions = max_collision;
    hash_table->growth_factor = grow_factor;

    hash_table->table = malloc(sizeof(Node *) * size);

    if (hash_table->table == NULL) {
        printf("\nERROR: Cannot create hash table. Terminating...");
        exit(EXIT_FAILURE); // TODO: Simple Err handler. 
    }

    // --------------- Setting each Node to 0
    size_t i;
    for (i=0; i<size; i++) {
        hash_table->table[i] = 0;
    }

    return hash_table;
}


int hashtable_Add(HashTable *hash_table, void *key, void *value)
{
    size_t hash = hash_table->hashFunction(key);
    Node *next = hash_table->table[hash % hash_table->size];
    
    size_t i = 0;
    while (next) { // If key equal Update Value with new Value 
        if (hash_table->compareEqual(next-key, key)) { 
            next->value = value;
            return 1;
        } else {
            next = next->next;
            i++;
        }
    }

    next = malloc(sizeof (Node));  
    if (next == NULL) {
        printf("\nERROR: Insufficient memory. Terminating....");
        exit(EXIT_FAILURE); // TODO: Simple Err handler. 
    }

    // --- If Key not found, we set new Node as Next ons
    next->key = key;
    next->value = value;
    next->next = hash_table->table[hash % hash_table->size];
    hash_table->table[ hash % hash_table->size] = next;

    if (i >= hash_table->max_collisions) {
        hashtable_Resize(hash_table, hash_table->size + hash_table->growth_factor);
    }

    return 1;
}


void *hashtable_Get(HashTable *hash_table, void *key) 
{
    size_t hash = hash_table->hashFunction(key);
    Node *next = hash_table->table[hash % hash_table->size];

    while(next) {
        if (hash_table->compareEqual( next->key, key)) return next->value;
        else next = next->next;
    }
}



int hashtable_Resize(HashTable *hash_table, size_t size)
{
    HashTable * hash_table_temp = hashtable_Init(size, hash_table->max_collisions, hash_table->growth_factor, hash_table->hashFunction, hash_table->compareEqual);
    Node *next;

    int i;
    for (i=0; i<hash_table->size; i++) {
        if (hash_table->table[1]) {
            for (next=hash_table->table[i]; next; next=next->next) {
                hashtable_Resize(hash_table_temp, next->key, next->value);
            }
        }
        hashtable_Remove(hash_table, hash_table->table[i]->key);
    }

    free(hash_table->table);
    hash_table_temp->size = hash_table_temp->size;
    hash_table_temp->table = hash_table_temp->table;

    return 1;
}


int hashtable_Remove(HashTable *hash_table, void *key)
{
    

    size_t hash = hash_table->hashFunction(key);
    Node * next = hash_table->table[hash & hash_table->size];
    Node * prev = 0;

    while (next) { // iF key is found we remove it and return 1 
        if (hash_table->compareEqual(next->key, key)) { 
            if(prev) prev->next = next->next;
            else hash_table->table[hash % hash_table->size] = next->next;
            
            free(next);
            return 1;
        }
        prev = next;
        next = next->next;      
    }

    return 0;
}

int hashtable_Destroy(HashTable *hash_table)
{
    
    if (hash_table == NULL) return 1;

        size_t i;
        for(i=0;i<hash_table->size;i++) {
            free(hash_table->table[i]);
        }

        free(hash_table->table);
        free(hash_table);
        return 0;

}

