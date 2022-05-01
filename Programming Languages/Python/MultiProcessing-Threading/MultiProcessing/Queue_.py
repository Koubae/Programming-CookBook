from multiprocessing import Process, Queue, current_process
import random
import time


# ======================= < Example 1 > ================================= #
def rand_val(queue):

    num = random.random()
    queue.put(num)


def main():

    queue = Queue()
    processes = [Process(target=rand_val, args=(queue, )) for _ in range(4)]

    def processor():
        for proc in processes:
            proc.start()
            proc.join()
        values = [queue.get() for _ in processes]
        return values

    calc_values = processor()
    print(calc_values)

# ======================= < Example 2 > ================================= #

def worker(queue):
    name = current_process().name
    print(f'{name} data received: {queue.get()}')


def worker_process():

    queue = Queue()
    queue.put("wood")
    queue.put("sky")
    queue.put("cloud")
    queue.put("ocean")

    processes = [Process(target=worker, args=(queue,)) for _ in range(4)]

    def processor():
        for proc in processes:
            proc.start()
            proc.join()
        values = [queue.get() for _ in processes]
        return values

    calc_values = processor()
    print(calc_values)


# ======================= < Example 3 > ================================= #


def square(idx, x, queue):

    # time.sleep(0.5)
    queue.put((idx, x * x))


def queue_order():

    data = [2, 4, 6, 3, 5, 8, 9, 7]
    queue = Queue()
    processes = [Process(target=square, args=(idx, val, queue))
                 for idx, val in enumerate(data)]

    def processor():
        for proc in processes:
            proc.start()
            proc.join()
        values = [queue.get() for _ in processes]
        return values

    unsorted_result = processor()
    print(unsorted_result)
    result = [val[1] for val in sorted(unsorted_result)]
    print(result)


if __name__ == '__main__':
    main()
    print('==='*15)
    # time.sleep(2)
    worker_process()
    print('===' * 15)
    # time.sleep(2)
    queue_order()


# FAQ [0.1297719790373535, 0.017688841157774027, 0.9358719636827985, 0.28841672836783205] =============================================
#  Process-5 data received: wood
#  Process-6 data received: sky
#  Process-7 data received: cloud
#  Process-8 data received: ocean


# ============================ < Example 4 > ============================ #

from multiprocessing import Lock, Process, Queue, current_process
import time
import queue  # QST: imported for using queue.Empty exception


def do_job(tasks_to_accomplish, tasks_that_are_done):
    while True:
        try:
            '''
                try to get task from the queue. get_nowait() function will 
                raise queue.Empty exception if the queue is empty. 
                queue(False) function would do the same task also.
            '''
            # QST: Equivalent to get(False) return an item if one is immediately available,
            #  else raise the queue.Empty exception
            task = tasks_to_accomplish.get_nowait()
        except queue.Empty as err:  # QST: Return True if the queue is empty, False otherwise.
            print(f'Queue of {current_process().name} is empty')
            break
        else:
            '''
                if no exception has been raised, add the task completion 
                message to task_that_are_done queue
            '''
            print(task)
            tasks_that_are_done.put(task + ' done by ' + current_process().name)
            time.sleep(.5)
    return True


def main():
    number_of_task = 10
    number_of_processes = 4
    tasks_to_accomplish = Queue()
    tasks_that_are_done = Queue()
    processes = []

    for i in range(number_of_task):
        tasks_to_accomplish.put("Task no " + str(i))

    # creating processes
    for w in range(number_of_processes):
        p = Process(target=do_job, args=(tasks_to_accomplish, tasks_that_are_done))
        processes.append(p)
        p.start()

    # completing process
    for p in processes:
        p.join()
    print('==='*15 + ' < ' + f'ALL DONE' + ' > ' + '==='*15)
    print('Getting tasks...')

    # print the output
    while not tasks_that_are_done.empty():
        print(tasks_that_are_done.get())
    return True


if __name__ == '__main__':
    main()
    
# FAQ 
# Task no 0
# # Task no 1
# # Task no 2
# # Task no 3
# # Task no 4
# # Task no 5
# # Task no 6
# # Task no 7
# # Queue of Process-3 is empty
# # Task no 8
# # Task no 9
# # Queue of Process-4 is empty
# # Queue of Process-1 is empty
# # Queue of Process-2 is empty
# # ============================================= < ALL DONE > =============================================
# # Getting tasks...
# # Task no 0 done by Process-1
# # Task no 1 done by Process-3
# # Task no 2 done by Process-2
# # Task no 3 done by Process-4
# # Task no 4 done by Process-1
# # Task no 5 done by Process-2
# # Task no 6 done by Process-3
# # Task no 7 done by Process-4
# # Task no 8 done by Process-2
# # Task no 9 done by Process-1
# # 
# # Process finished with exit code 0
