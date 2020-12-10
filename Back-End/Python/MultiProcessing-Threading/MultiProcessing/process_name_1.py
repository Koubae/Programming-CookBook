from multiprocessing import Process, current_process
import time
import os


def fun(val):
    process = os.getpid()
    parent_process = os.getppid()
    name = current_process().name
    print('==='*15 + ' < ' + f'{name}' + ' > ' + '==='*15)
    print(f'starting fun Process={process} VAL={val}')
    print(f'Parent ID={parent_process}')
    time.sleep(val)
    print(f'finishing fun Process={process}  VAL={val}')
    print('==='*15)


def main():

    p1 = Process(target=fun, args=(3, ))
    p1.start()
    p1.join()
    print(f'Process p is alive: {p1.is_alive()}')

    p2 = Process(target=fun, args=(2,))
    p2.start()
    p2.join()
    print(f'Process p is alive: {p2.is_alive()}')

    p3 = Process(target=fun, args=(1,))
    p3.start()
    p3.join()
    print(f'Process p is alive: {p3.is_alive()}')

if __name__ == '__main__':
    print('starting main')
    main()
    print('finishing main')


# NOTE:FAQ The os.getpid returns the current process Id,
#  while the os.getppid returns the parent's process Id.
#  The parent Id is the same, the process Ids are different for each child process.