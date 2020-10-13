
def fact(n, cache=[]):

    if n < 1:
        return 1
    elif n in cache:
        return cache
    else:
        #print(cache)
        print(f'Calc {n}')
        #print('Before recursion')
        result = n * fact(n -1)
        #print(result)
        #print('==='*30)
        #print('After Recursion')
        cache.append(result)
        print(cache)
        return result

print(fact(4))


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n-1)
        cache[n] = result
        return result

factorial(3)