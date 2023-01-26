#include <stdio.h>


int main(void)
{

    // -------------------------------
    //  Conditionals
    // -------------------------------
    printf("\n------------------- < Conditionals > -------------------\n");
    // if, else if, else 
    int number1 = 10;
    int numberInput;
    printf("Enter a int:\n");
    printf(">>> ");
    scanf("%d", &numberInput);

    if (number1 == numberInput) {
        printf("%d == %d\n", number1, numberInput);
    } else if (number1 < numberInput) {
        // nested 
        printf("%d < %d (nested\n)", number1, numberInput);
        if (numberInput == 1) {
            printf("%d == 1\n", number1);
        } else {
            printf(" Nested else\n");
        }
    } else {
        printf("%d > %d\n", number1, numberInput);
    }

    // If the logic is 1 line only, we can ommit the parethesis, use with precaution and when is actually more readable
    if (number1 > numberInput)
       printf("%d > %d\n", number1, numberInput);
    else if (number1 == numberInput)
        printf("%d == %d\n", number1, numberInput);
    else
        printf("%d < %d\n", number1, numberInput);
    // can do this way as well, but can get messy very quickly!
    if (number1 > numberInput)  printf("%d > %d\n", number1, numberInput);      
    else if (number1 == numberInput) printf("%d == %d\n", number1, numberInput);        
    else printf("%d < %d\n", number1, numberInput);


    // switch 
    switch (numberInput)
    {
    case 0:
        printf("numberInput is 0 \n");
        break;       
    case 2:  // fall through
    case 4:
    case 6:
    case 8:
    case 10:
        printf("numberInput is even \n");
        break;
    case 3:   // fall through
    case 5:
    case 7:
    case 9:
        printf("numberInput is odd \n");
        break;
    
    default:   // default
        printf("numberInput is not between 0 to 10! \n");
        break;
    }

    // NOTE: Look what we can do with a falltrhogh, we can actually perform operation. Use with precaution though
    int fallThroughCount = 0;
    switch (numberInput)
    {
    case 0:
        printf("numberInput is 0 \n");
        break;       
    case 2:  // fall through
        fallThroughCount ++;
    case 4:
        fallThroughCount ++;
    case 6:
        fallThroughCount ++;
    case 8:
        fallThroughCount ++;
    case 10:
        fallThroughCount ++;
        printf("numberInput is even fallThroughCount value %d\n", fallThroughCount);
        break;
    case 3:   // fall through
        fallThroughCount ++;
    case 5:
        fallThroughCount ++;
    case 7:
        fallThroughCount ++;
    case 9:
        fallThroughCount ++;
        printf("numberInput is odd fallThroughCount value %d\n", fallThroughCount);
        break;
    
    default:   // default
        printf("numberInput is not between 0 to 10! \n");
        break;
    }


    // ternary operator
    char *valueType = (numberInput % 2 == 0) ? "EVEN" : "ODD";
    printf("numberInput is of type %s\n", valueType);
    // also can be done this way
    (number1 >= numberInput) ? printf("number1 >= numberInput\n") : printf("number1 < numberInput\n");
    // We can nest ternaryr operator inside another ternary operator (the second is inside the 'False'), but, use with precaution!
    (number1 > numberInput) ? printf("number1 > numberInput\n") : (number1 < numberInput) ? printf("number1 < numberInput\n") : printf("number1 == numberInput\n");


    // -------------------------------
    //  Loops
    // -------------------------------
    printf("\n------------------- < loops > -------------------\n");
    // while
    int counter = 0;
    while (counter < 10) {
        printf("(while loop) Counter %d\n", counter);
        counter ++;

        int counterInner = 0;
        while (counterInner < 3) {
            printf("(while loop) CounterInner %d\n", counterInner);
            counterInner ++;
        }
         printf("Exited the nested while loop, Counter %d\n", counter);
    }
    printf("Exited the first while loop, Counter %d\n", counter);

    int counter2 = 0;
    while (counter2 < 10) {
        printf("(while loop) Counter %d\n", counter);
        counter2 ++;

        if (counter2 < 4) 
            continue; 
        else if (counter2 > 9)
            break;
       
    }
    printf("Exited the Second while loop, Counter %d\n", counter);

    // do while
    do {
       printf("(do while loop) Counter %d\n", counter); // executes at least once
       counter ++;  
    } while (counter < 10);
    printf("Exited the first do while loop, Counter %d\n", counter);

    // for loop
    for(int i = 0; i < 10; i++) {
        // nested loop
        for (int y = 10; y > 0; y --) { // notice, we count in reverse :)
            printf("(for loop) i=%d, y=%d\n", i, y);
        }
    }

    // -------------------------------
    //  goto 
    // -------------------------------
    // Be careful with goto, is a tool that should be used by C expert only, but just know exist and don't start to use it till people call u C senior!
    printf("\n------------------- < goto > -------------------\n");
    // this example is just to illustrate the goto, it doesnt have a real application in the real world. 
    const int BUFFER_SIZE = 255;
    int dataInput = 10000;
    int dataOutput = 0;
    int buffer = 0;
    
    while (dataOutput < dataInput) {

        printf("- (while loop) buffer=%d,  dataOutput=%d\n", buffer, dataOutput);

        if (buffer >= BUFFER_SIZE) 
             goto loadBuffer;
        
        buffer ++;

    }

    loadBuffer:
        dataOutput += buffer;
        buffer = 0;

    printf("- Buffer Loaded size dataOutput=%d\n", dataOutput);

    return 0;
}