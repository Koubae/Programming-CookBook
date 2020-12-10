from multiprocessing import Process, Value
from time import sleep


def f(counter):

    sleep(1)

    with counter.get_lock():
        counter.value += 1

    print(f'Counter: {counter.value}')

def main():

    counter = Value('i', 0)

    processes = [Process(target=f, args=(counter, )) for _ in range(30)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

if __name__ == '__main__':
    main()