from multiprocessing import Process, current_process
import time
import os


def worker():

    name = current_process().name
    print('==='*15 + ' < ' + f'{name}' + ' > ' + '==='*15)
    time.sleep(1)
    print(f'{name} Exiting...')


def worker_1():

    name = current_process().name
    print('===' * 15 + ' < ' + f'{name}' + ' > ' + '===' * 15)
    time.sleep(1)
    print(f'{name} Exiting...')


def service_a():

    name = current_process().name
    print('===' * 15 + ' < ' + f'{name}' + ' > ' + '===' * 15)
    time.sleep(1)
    print(f'{name} Exiting...')


def service_b():

    name = current_process().name
    print('===' * 15 + ' < ' + f'{name}' + ' > ' + '===' * 15)
    time.sleep(1)
    print(f'{name} Exiting...')


if __name__ == '__main__':

    serviceA = Process(name='Service A', target=service_a)
    serviceB = Process(name='Service B', target=service_b)

    worker_one = Process(name='Worker 1', target=worker)
    worker_two = Process(name='Worker 2', target=worker_1)

    serviceA.start()
    serviceA.join()

    serviceB.start()
    serviceB.join()

    worker_one.start()
    worker_one.join()
    
    worker_two.start()
    worker_two.join()