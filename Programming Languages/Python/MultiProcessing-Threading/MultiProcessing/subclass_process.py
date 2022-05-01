from multiprocessing import Process, current_process
import time
import os


class Worker(Process):

    def run(self):
        print(f'In {self.name}')
        time.sleep(1)


def main() -> None:

    worker_1 = Worker()
    worker_1.start()

    worker_2 = Worker()
    worker_2.start()

    worker_3 = Worker()
    worker_3.start()

    worker_1.join()
    worker_2.join()
    worker_3.join()


if __name__ == '__main__':
    main()