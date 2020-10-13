def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursie case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))

# >>> 120