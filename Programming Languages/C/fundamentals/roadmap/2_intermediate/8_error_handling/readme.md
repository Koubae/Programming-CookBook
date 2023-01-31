C Roadmap - Error Handling
=======================

- [C Programming/Error handling - en.wikibooks.org](https://en.wikibooks.org/wiki/C_Programming/Error_handling)
- [C - Error Handling - tutorialspoint.com](https://www.tutorialspoint.com/cprogramming/c_error_handling.htm)

- [Practical usage of setjmp and longjmp in C - /stackoverflow.com](https://stackoverflow.com/questions/14685406/practical-usage-of-setjmp-and-longjmp-in-c)

- [ meaning-matters/Except - github](https://github.com/meaning-matters/Except)

### Signals

```c
#define SIGHUP  1   /* Hangup the process */ 
#define SIGINT  2   /* Interrupt the process. C standard */ 
#define SIGQUIT 3   /* Quit the process */ 
#define SIGILL  4   /* Illegal instruction. C standard.*/ 
#define SIGTRAP 5   /* Trace trap, for debugging. C standard.*/ 
#define SIGABRT 6   /* Abort. C standard. */
#define SIGFPE  8   /* Floating Point Error. C standard. */
#define SIGSEGV 11  /* Memory error. C standard.  */
#define SIGTERM 15  /* Termination request. C standard. */
```