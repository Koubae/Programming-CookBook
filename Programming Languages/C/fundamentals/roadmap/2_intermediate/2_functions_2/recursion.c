#include <stdio.h>

/** 
 * Just a simple function that calculates recursivly the steps to go from one number to another
 * by N steps
 * 
 * Did not test it, is just to demostrate a recursive function
*/
int recursionCounter(int minuend, int subtrahend, int target)
{   
    static int count = 0;
    // Condition to terminate the recursion
    if (subtrahend > minuend) 
        return count;
    else if (count >= target)
        return count;

    int calculatedValue = minuend - subtrahend;
    count ++; 
    recursionCounter(calculatedValue, subtrahend, target);  // recursive call

}


void main(void)
{
    int minuend = 100;
    int subtrahend = 3;
    int target = 74; 

    int cycleCount = recursionCounter(minuend, subtrahend, target);
    printf("%d steps to reach %d from %d by step of %d\n", cycleCount, target, minuend, subtrahend);   

}
