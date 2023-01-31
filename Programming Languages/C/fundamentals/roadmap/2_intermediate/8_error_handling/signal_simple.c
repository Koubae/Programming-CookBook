// @credit: https://en.wikibooks.org/wiki/C_Programming/Error_handling
#include <stdio.h>
#include <unistd.h> // Unix Standard library, used to import sleep()
#include <stdlib.h>
#include <signal.h>

void handler(int signum) {
   printf("Signal received %d, coming out...\n", signum);
   exit(1);
}


int main () {
   signal(SIGINT, handler); // attaching the handler() function to SIGINT signals; i.e, ctrl+c, keyboard interrupt.

   while(1) {
      printf("Sleeping...\n");
      sleep(1000); // sleep pauses the process for a given number of seconds, or until a signal is received. 
   }
   return(0);
}