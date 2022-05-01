Functions Parameters
=======================


## Features

- [sys.getrecursionlimit()](https://docs.python.org/3/library/sys.html#sys.getrecursionlimit)

Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. It can be set by setrecursionlimit().

- [sys.setrecursionlimit(limit)](https://docs.python.org/3/library/sys.html#sys.setrecursionlimit)

Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.

## Recursive Functions
=======================

A recursive function is a function defined in terms of itself via self-referential expressions. This means that the function will continue to call itself and repeat its behavior until some condition is met to return a result.

![img](rec1.png)

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.


*Recursive function for calculating n! implemented in Python:*

- **INPUT**
```
def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)
```
- **OUTPUT**
```
>>> factorial_recursive(5)
120
```

Behind the scenes, each recursive call adds a **stack frame** (containing its execution context) to the call stack until we reach the base case. Then, the stack begins to **unwind** as each call returns its results:

![img](rec_stack.webp)

------------------------------------------
### Each recursive call has its own **execution context**

* Thread the state through each recursive call so that the current state is part of the current call’s execution context.

* Keep the state in global scope

- **INPUT**
```
def sum_recursive(current_number, accumulated_sum):
    # Base case
    # Return the final state
    if current_number == 11:
        return accumulated_sum

    # Recursive case
    # Thread the state through the recursive call
    else:
        return sum_recursive(current_number + 1, accumulated_sum + current_number)
```
- **OUTPUT**
```
# Pass the initial state
>>> sum_recursive(1, 0)
55
```

![img](recu3.png)

------------------------------------------

### Recursive Data Structures


A data structure is recursive if it can be deﬁned in terms of a smaller version of itself. A list is an example of a recursive data structure. 

- **INPUT**
```
# Return a new list that is the result of
# adding element to the head (i.e. front) of input_list
def attach_head(element, input_list):
    return [element] + input_list

```

- **OUTPUT**
```
tach_head(1,                                                  # Will return [1, 46, -31, "hello"]
            attach_head(46,                                     # Will return [46, -31, "hello"]
                        attach_head(-31,                        # Will return [-31, "hello"]
                                    attach_head("hello", [])))) # Will return ["hello"]

[1, 46, -31, 'hello']
```
![img](list.4.gif)


------------------------------------------

#### Advantages of Recursion

* Recursive functions make the code look clean and elegant.
* A complex task can be broken down into simpler sub-problems using recursion.
* Sequence generation is easier with recursion than using some nested iteration.

#### Disadvantages of Recursion

* Sometimes the logic behind recursion is hard to follow through.
* Recursive calls are expensive (inefficient) as they take up a lot of memory and time.
* Recursive functions are hard to debug.

![img](python-factorial-function.png)





### Notes

```
def my_func(a, b):
    # code here

X = 10
Y = 'Hello'

my_func(x, y)
```

*In this context, a and b are called **parameters** of my_func, Also note that a and b are **variables**, **local** to my_func*
 
*And y are called the **arguments** of my_func, Also note that x and y are passed by **reference***

x, y ==> MODULE SCOPE

a, b ==> FUNCTION SCOPE



-----------------------------------------------------------------------------------------------------