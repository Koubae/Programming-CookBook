fib_list = []

def fib_rec(n):

    print('Calculating F', '(', n, ')', sep='', end=',\n')

    # Base Case
    if not n:
        return 0
    elif n == 1:
        return 1
    # Recursive CAse
    else:
        result = n - 1 + n - 2
        fib_list.append(result)
        return fib_rec(n-1) + fib_rec(n -2)

print(fib_rec(10))
print(fib_list)

# 55
# [17, 15, 13, 11, 9, 7, 5, 3, 1, 1, 3, 1, 5, 3, 1, 1, 7, 5, 3, 1,
#  1, 3, 1, 9, 7, 5, 3, 1, 1, 3, 1, 5, 3, 1, 1, 11, 9, 7, 5, 3, 1,
#  1, 3, 1, 5, 3, 1, 1, 7, 5, 3, 1, 1, 3, 1, 13, 11, 9, 7, 5, 3, 1,
#  1, 3, 1, 5, 3, 1, 1, 7, 5, 3, 1, 1, 3, 1, 9, 7, 5, 3, 1, 1, 3, 1, 5, 3, 1, 1]
