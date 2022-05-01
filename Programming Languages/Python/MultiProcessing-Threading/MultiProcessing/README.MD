Multiprocessing
=======================



-----------------------------------------------------------------------------------------------------

Multiprocessing has Separate memory in a process, In multiprocessing, each worker has its own memory. The memory is not shared like in threading. 

*In multiprocessing, there is no guarantee that the processes finish in a certain order.*

> **Sharing state between processes**

Data can be stored in a shared memory using **Value** or **Array**. 

**Note**: It is best to avoid sharing data between processes. Message passing is preferred.

> **Message passing with queues**

The message passing is the preferred way of communication among processes. Message passing avoids having to use synchronization primitives such as locks, which are difficult to use and error prone in complex situations. 

### Loggin

```
logger = multiprocessing.log_to_stderr(logging.INFO)
```

Process
-------

The Process object represents an activity that is run in a separate process. 

The multiprocessing.Process class has equivalents of all the methods of threading.Thread. 

The **Process** constructor should always be called with keyword arguments.

* The **target** argument of the constructor is the callable object to be invoked by the run method. 

* The **name** is the process name. 

* The **start** method starts the process's activity. 

> **join()**

#### Waiting for ProcessesWaiting for Processes


* The **join** method blocks until the process whose join method is called terminates.  Without the join method, the main process won't wait until the process gets terminated. 

* If the timeout option is provided, it blocks at most timeout seconds. 

* the **is_alive()** method returns a boolean value indicationg whether the process is alive. 

* The **terminate()** method terminates the process. 



> **os.getpid()** => Current Process ID

> ***os.getppid()** => Parent ID, always the same.

> **current_process().name** => Process Name.

multiprocessing.current_process().pid


> **deamon** (bool): default False

By default the main program will not exit until all of the children have exited. There are times when starting a background process that runs without blocking the main program from exiting is useful, such as in services where there may not be an easy way to interrupt the worker, or where letting it die in the middle of its work does not lose or corrupt data (for example, a task that generates “heart beats” for a service monitoring tool).

To mark a process as a daemon, set its daemon attribute with a boolean value. The default is for processes to not be daemons, so passing True turns the daemon mode on.


The daemon process is terminated automatically before the main program exits, to avoid leaving orphaned processes running. You can verify this by looking for the process id value printed when you run the program, and then checking for that process with a command like ps.


*To wait until a process has completed its work and exited, use the join() method.*


> **terminate()**

##### Note

*It is important to join() the process after terminating it in order to give the background machinery time to update the status of the object to reflect the termination.*



-----------------------------------------------------------------------------------------------------

Pool
-------

It controls a pool of worker processes to which jobs can be submitted. 

* **cpu_unit** 

The number of cores is determined with the cpu_unit function.


* **map**
* **starmap**

-----------------------------------------------------------------------------------------------------

Pathos
---------


- [pathos --GITHUB--](https://github.com/uqfoundation/pathos)
- [pathos --DOCS--](https://pathos.readthedocs.io/en/latest/pathos.html#pathos-module-documentation)



### Notes


#### Global Interpreter Lock (GIL)

Global Interpreter Lock (GIL) by using subprocesses instead of threads.


 A global interpreter lock (GIL) is a mechanism used in Python interpreter to synchronize the execution of threads so that only one native thread can execute at a time, even if run on a multi-core processor.

The C extensions, such as numpy, can manually release the GIL to speed up computations. Also, the GIL released before potentionally blocking I/O operations.



Python has three modules for concurrency: **multiprocessing** |  **hreading**  | **asyncio.**

> When the tasks are CPU intensive, we should consider the **multiprocessing** module. 

> When the tasks are I/O bound and require lots of connections, the **asyncio** module.

> For other types of tasks and when libraries cannot cooperate with asyncio, the **threading** module can be considered. 


- [when-to-use-apply-apply-async-or-map SOO](https://stackoverflow.com/questions/8533318/multiprocessing-pool-when-to-use-apply-apply-async-or-map)

-----------------------------------------------------------------------------------------------------


### Credits

- [ZetCode --Python multiprocessing tutorial](http://zetcode.com/python/multiprocessing/)
- [Long-running task in Tkinter](http://zetcode.com/articles/tkinterlongruntask/)

- [pymotw.com](https://pymotw.com/2/multiprocessing/basics.html)