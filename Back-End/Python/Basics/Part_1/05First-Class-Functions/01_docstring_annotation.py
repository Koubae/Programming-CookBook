def my_func(a, b):
    '''
    Returns the product of a and b
    :param a: Must be a interger, is the first parameter
    :param b: Must be a string, must be a string
    :return: Transforms param b into a int and returns a + b
    '''
    try:
        b = int(b)
        result = b + a
    except Exception as e:
        return f' there was a problem.. look --> {e}'

    finally:
        print('I always execute')
    return result

help(my_func)
print(my_func.__doc__)
# Returns the product of a and b
#     :param a: Must be a interger, is the first parameter
#     :param b: Must be a string, must be a string
#     :return: Transforms param b into a int and returns a + b


def my_func_a(a: int, b: 'str turn into int')-> 'returns a + b':

    try:
        b = int(b)
        result = b + a
    except Exception as e:
        return f' there was a problem.. look --> {e}'

    finally:
        print('I always execute')
    return result


help(my_func_a)
# Help on function my_func_a in module __main__:
#
# my_func_a(a: int, b: str) -> 'returns a + b'
print(my_func_a.__annotations__)
# {'a': <class 'int'>, 'b': 'str turn into int', 'return': 'returns a + b'}

#  we can combine both docstrings and annotations:


def fact(n: 'int >= 0') -> int:
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)

help(fact)

def my_func_2(a:str='a', b:int=1)->str:
    return a*b


# The annotations can be any expression, not just strings:

x = 3
y = 5


def my_func_3(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
	return a*max(x, y)

help(my_func_3)