import logging
import threading
import time

total_jobs = 0


def common_function(name, sleep_time):
    """Function meant to be used by the Sub Threads (Tasks)"""
    global total_jobs
    main_thread = threading.main_thread()
    logging.info(f'MAIN THREAD --> {main_thread}')
    logging.info(f"Sub Thread %s: starting sub process %r", name, common_function.__name__)
    for i in ["job_1", "job_2", "job_3", "job_4", "job_5", "job_6", "job_7", "job_8", "job_9", "job_10"]:
        logging.info(f'{name} Do job --> {i} ')
        total_jobs += 1
    time.sleep(sleep_time)
    for i in ["job_1", "job_2", "job_3", "job_4", "job_5", "job_6", "job_7", "job_8", "job_9", "job_10"]:
        logging.info(f'{name} Do job --> {i} ')
        total_jobs += 1
    logging.info(f"Sub Thread %s: finishing sub process %r", name, common_function.__name__)
    logging.info(f' {name} Finish -> {total_jobs}')


def thread_function(name):
    """Function where The Thread will interacts and spawn Sub Threads (Tasks) """
    logging.info("Thread %s: starting", name)

    # --------- SUB THREADS (Tasks)
    tasks = list()
    for index in range(10):
        task_name = f'Task -> {index}'
        logging.info(f"{thread_function.__name__}    : create and start task: {task_name}")
        task = threading.Thread(target=common_function, args=(task_name, 1))
        tasks.append(task)
        task.start()

    for index, task in enumerate(tasks):
        task_name = f'Task -> {index+1}'
        logging.info(f"{thread_function.__name__}    : before joining task: {task_name}")
        task.join()
        logging.info("Main    : thread %d done", index+1)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)
    logging.info(f'Finish -> {total_jobs}')


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    #-------------------- THREAD
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()