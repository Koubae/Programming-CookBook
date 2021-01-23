SCOPES, CLOSURES AND DECORATORS
=================================


Names refer to objects. Names are introduced by name binding operations. Each occurrence of a name in the program text refers to the binding of that name established in the innermost function block containing the use.

*Python determines the scope of objects at compile-time, not at run-time.*

- [DOCS](https://docs.python.org/3.3/reference/executionmodel.html)

## BLOCKS:

- *Module*
- *Function*
- *Body*
- *Class Definition*
- *Code block* --> Scripts file, a Scripts command, arguments.

> Each command typed interactively is a block

## Features

- Variable is **bound** to object => Reffers to the connection between variable and obj.
- **Lexical scope** --> The portions of code where name/binding is defined.
- **Namesspaces** --> Where these bindings are stored, each scope has its own namespace.
- **Namespace lookups** ---> When requesting the object bound to a variable name.
- **Variable goes out of scope** ---> When a function finishes running the scope is gone.
- **Execution Frame** -- > A frame containing some administrative information.
- **Scope** ---> Defines the visibility of a name within a block.
- **Block’s environment** --- >Set of scopes visible to a code block.
- **Fre variable** --> Variable is used in a code block but not defined (assigned) in the block.

-----------------------------------------------------------------------------------------

- **[NameError](https://docs.python.org/3.3/library/exceptions.html#NameError)**
- **[UnboundLocalError](https://docs.python.org/3.3/library/exceptions.html#UnboundLocalError**
- **[builtins](https://docs.python.org/3.3/library/builtins.html#module-builtins)**



## Global Scope

The global scope is essentially the module scope, It spans a single file only.
There is no concept of a truly global (across all the modules in our entire app) scope in Python, The only exception to this are some of the built-in globally available objects, such as:

> *True False None dict print*

-----------------------------------------------------------------------------------------------------

## Local Scope

When we create functions, we can create variable names inside those functions (using assignments).
When retrieving the value of a global variable from inside a function, Python automatically
searches the local scope's namespace, and up the chain of all enclosing scope namespaces

**local → global → built-in**

> Variables defined inside a function are not created until the function is called.*

> *Every time the function is called, a new scope is created*

The actual object the variable references could be different each time the function is called.



#### This is why recursion works!

-----------------------------------------------------------------------------------------------------

## Non Local Scope

Whenever Python is told that a variable is nonlocal. it will look for it in the enclosing local scopes chain until it first encounters the specified variable
name.

***Beware**: It will only look in local scopes, it will not look in the global scope*



-----------------------------------------------------------------------------------------------------

## Free Variables & Closures

Python does this by creating a cell as an intermediary object, You can think of the closure as a function plus an *extended scope* that contains the free variables.

The free variable's value is the object the cell points to – so that could change over time!
Every time the function in the closure is called and the free variable is referenced:

> **Python looks up the cell object, and then whatever the cell is pointing to**
> **Every time we run a function, a new scope is created.**
> **If that function generates a closure, a new closure is created every time as well**

Very often, classes that define a single method (other than initializers) can be implemented using a closure instead.

----------------------------------------------------------------------------------------------------