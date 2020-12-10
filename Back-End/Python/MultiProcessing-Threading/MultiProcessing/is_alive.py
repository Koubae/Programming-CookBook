from multiprocessing import Process
import time
import os

def fun(val):
    process = os.getpid()
    print(f'starting fun Process={process} VAL={val}')
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


# NOTE:??? The is_alive method determines if the process is running.
# NOTE:??? If we comment out the join, the process is still alive. 