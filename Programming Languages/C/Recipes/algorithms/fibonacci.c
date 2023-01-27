#include <stdio.h>


int getFibonacciValueByPosition(int position);
void fibonacciSequence1(int nthSequence);

void fibonacciSequence2(int nthSequence);


int main()
{
    printf("Sequence 1: ");
    fibonacciSequence1(10);    

    printf("\n ---------------------------------------------------------------\n");

    printf("Sequence 2: ");
    fibonacciSequence2(10);

    return 0;
}

void fibonacciSequence1(int nthSequence)
{
    int sequence[nthSequence];
    for (int i = 0; i <= nthSequence; i ++) {
        sequence[i] = getFibonacciValueByPosition(i);
    }

    for (int i = 0; i < sizeof(sequence) / sizeof(int); i++) {
        if (i != 0) 
            printf(", ");
        printf("%d", sequence[i]);
    }
}

int getFibonacciValueByPosition(int position)
{
    if (position <= 1)
        return position; 

    return getFibonacciValueByPosition(position - 1) + getFibonacciValueByPosition(position - 2);
}

void fibonacciSequence2(int nthSequence)
{
    static int temp = 0;
    static int leftValue = 0;
    static int rightValue = 1;
    static int count = -1;

    if (count == -1)
    {
        count = nthSequence - 2;  // Note: a real fibonacci sequence must have as first values 0, 1. Subtract 2 to keep count of that too!
        printf("%d %d ", leftValue, rightValue);
    }
       
    if (count <= 0) 
        return;

    temp = leftValue + rightValue;

    leftValue = rightValue;
    rightValue = temp;
    count --;

    printf("%d ", temp);    
    fibonacciSequence2(nthSequence - 1);


}