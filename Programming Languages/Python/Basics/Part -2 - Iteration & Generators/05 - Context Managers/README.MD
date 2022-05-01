# Context Manager
=======================


- **The "with" Statement** [PEP 343](https://www.python.org/dev/peps/pep-0343/)

- [@contextlib.contextmanager](https://docs.python.org/3/library/contextlib.html#contextlib.contextmanager)
-----------------------------------------------------------------------------------------------------

## Features

###**CONTEXT MANAGEMENT PROTOCOL**

- **__enter__**

- **__exit__**


## Context Manager Patterns


### Open - Close

- Open File
    * Operate with File.
- Close File.

- Open Socket.
    * Operate on Socket.
- Close Socket.

### Start - Stop

- Start Databade Transaction.
    * Perform database Operations
- Commit or rollback transaction.

- Start Timer.
    *perform operations.
- Stop Timer.

### Lock - Relase

- Acquire thread lock
    * Perform some Operations.
- Release thread Lock.

### Change - Reset 

- Change Decimal context Precision.
    * Perform some operations using the new precision.
- Reset Decimal context precision back to original value.

- Redirect stdout to a file.
    * Perfoms some operations that write to stdout.
- Reset stdout to original value.

### Oter

- HTML Tag- 


-----------------------------------------------------------------------------------------------------