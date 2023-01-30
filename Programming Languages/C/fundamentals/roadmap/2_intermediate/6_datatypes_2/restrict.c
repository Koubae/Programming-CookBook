// @ref: https://learn.microsoft.com/en-us/cpp/c-language/type-qualifiers?view=msvc-170#restrict

void test(int* restrict first, int* restrict second, int* val)
{
    *first += *val;
    *second += *val;
}

int main()
{
    int i = 1, j = 2, k = 3;
    test(&i, &j, &k);

    return 0;
}

// Marking union members restrict tells the compiler that
// only z.x or z.y will be accessed in any scope, which allows
// the compiler to optimize access to the members.
union z 
{
    int* restrict x;
    double* restrict y;
};