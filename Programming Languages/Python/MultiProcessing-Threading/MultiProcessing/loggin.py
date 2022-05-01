import multiprocessing
import logging
import sys


def worker():
    print('Doing some work', flush=True)


if __name__ == '__main__':
    multiprocessing.log_to_stderr(logging.DEBUG)
    p = multiprocessing.Process(target=worker)
    p.start()
    p.join()
    print('==='*15)
    # MANIPULATE THE LOGGER DIRECTLY    
    multiprocessing.log_to_stderr()
    logger = multiprocessing.get_logger()
    logger.setLevel(logging.INFO)
    p2 = multiprocessing.Process(target=worker)
    p2.start()
    p2.join()