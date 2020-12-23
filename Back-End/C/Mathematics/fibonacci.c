// Fibonacci Series up to n terms
#include <stdio.h>

int main(void)
{
    int i, n, t1 = 0, t2 = 1, nextTerm;

    printf("Enter the total Fibunacci's numbers: ");
    scanf("%d", &n);
    printf("Fibonacci Series: ");

    for (i=1; i<=n; i++) {
        printf("%d, ", t1);
        nextTerm =  t1+t2;
        t1 = t2;
        t2 = nextTerm;
    }
    return 0;
}


// Fibonacci Sequence Up to a Certain Number
#include <stdio.h>
int main() {
    int t1 = 0, t2 = 1, nextTerm = 0, n;
    printf("Enter a positive number: ");
    scanf("%d", &n);

    // displays the first two terms which is always 0 and 1
    printf("Fibonacci Series: %d, %d, ", t1, t2);
    nextTerm = t1 + t2;

    while (nextTerm <= n) {
        printf("%d, ", nextTerm);
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
    }

    return 0;
}