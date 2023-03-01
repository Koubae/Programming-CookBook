C Roadmap - Memory
=======================


- Memory
    - Dynamic Memory Allocation
        - malloc
        - calloc
        - realloc
        - free
        - bfree
    - volatile (studied earlier, but re-inforce it now with memory)


- []()
- []()
- []()


### stackoverflow

- [C Memory Management](https://stackoverflow.com/questions/24891/c-memory-management)
- [difference between memory management &memory allocation.do they both work together when allocation/access happens2 memory|how they are exactly related](https://stackoverflow.com/questions/71261411/difference-between-memory-management-memory-allocation-do-they-both-work-togeth)
- [Patterns for freeing memory in C?](https://stackoverflow.com/questions/692119/patterns-for-freeing-memory-in-c)
- [Best way to handle memory allocation in C?](https://stackoverflow.com/questions/722922/best-way-to-handle-memory-allocation-in-c)



### quora

- [What are good memory management tips for C?](https://qr.ae/prk7t6)


- Don’t. Simply don’t use dynamic memory or allocate from the heap as you have alternatives like the Global space (extern/static globals and local static variables go here) or use the Stack space (typically 1MB limit on Windows, 8MB on Linux distros for every thread).
    This is preferred if all your data has a known limit and is mostly deterministic.
    The vast majority of the source of bugs from C stems from dynamic memory allocation, so keep this in mind as well.
- If you HAVE/NEED to use some form of dynamic memory (you’re making a linked list, dynamic array, etc.), then I’d say to give yourself headache only once by implementing your own allocator or memory pool. An allocator pool will allow you to turn a single byte buffer into your own little form of malloc.
    - Benefit to writing your own allocator is you can back it with a single malloc/calloc call and destroy the entire allocator with a single free call.
    - Downside to writing your own allocator is that you’ll need to make the allocator global in some form or else you’ll have to pass it around to all functions and data that require dynamic memory.
    - There are many different allocators you might need but you also need to keep track of things such as data alignment, etc.
    - If the data you allocate is of a fixed size — Use an object pool.
    - If the data is of a variadic size but you don’t want to free the data pointer given — Use a linear or arena allocator and destroy it when you’re done with it entirely.
    - If the data is of a variadic size and you’ll need to free at various times — use a Free List allocator.
- If you are in a scenario where you do NOT have the luxury to use the global or stack space AND you cannot write your own allocator, then here’s what you do.
    - For each type, create a cleaner function which are like destructor functions they take a pointer TO a pointer of the type you make, deallocate the data that the double pointer references, then set the pointer, that it points to, to NULL. Here’s an example using a linked list:
```c
struct mylist { 
    struct mylist *next; 
    intmax_t idata; 
}; 
    
void mylist_cleanup(struct mylist **noderef) 
{ 
    if( *noderef==NULL ) { 
        return; 
    } else { 
        mylist_cleanup(&(*noderef)->next); 
        free(*noderef), *noderef = NULL; 
    } 
} 
```

The cleaner function for the linked list reference will recursively free by continuously going to the next node, cleaning up the next-next node, and then stopping once we hit a NULL node and then going back to free the node data and then set its pointer to NULL. With this method, you can be sure that all your pointers will be set to NULL and NULL-checks will be consistent.

    - Having a consistent memory management policy such as documenting a policy as to who deals with the memory, the end user or the library? My personal policy is that whatever end-user developer allocates or requests from my library, they must free it.
        - Such as if they allocate/request a linked list and the library API allocates it, then the end user must deallocate that linked list using the appropriate API given.
        - If my library allocates something internally, then it is my responsibility as the library dev to deallocate that internal buffer.
        - If I have an API that allocates to the end-user AND allocates internally (such as my personal implementation of a JSON parser), then the end-user is only responsible for calling the deallocation functions specific to that API and the internal API is responsible for the rest of the data that is internal to it.
            - Remember that this is all MY memory management policies, yours can be different as you see fit or require as your C code.
    - Never, ever, EVER change the pointer value of the original allocated pointer… I’ve seen newbies asking me for help doing this in their code. It’s rare but I’ve seen it… I’d like to think this is a good reason to make pointer values constant: int *const p = malloc(sizeof *p);
    - If you need your allocated data zeroed out when given, use calloc.
    - If you need to resize your data and you’re resizing it to a smaller or larger buffer, use realloc as it’ll be many times more performant than using malloc & memcpy.

These are my tips that I’ve learned over the 7 years I’ve been doing C programming for my own projects. I hope you find many of these useful.

My final piece of advice: When you’re in trouble, printf-debugging, GNU Debugger and Valgrind are your best friends and will always be there for you.

EDIT:

Concerning Allocators, having a good sized allocator buffer is also more cache-friendly (cache-friendly = better performance) if it’s at a good size (typically at page size or lower) and is able to fit in L1 Cache.

Concerning Stack memory, Stack memory is almost always hot in the cache, so it’s alot more performant than using a massive heap-allocated buffer. Just remember not to go past the stack size limit per thread.