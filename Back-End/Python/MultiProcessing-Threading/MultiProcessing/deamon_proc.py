import multiprocessing
import time
import logging

def daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid, flush=True)
    time.sleep(2)
    print('Exiting :', p.name, p.pid, flush=True)


def non_daemon():
    p = multiprocessing.current_process()
    print('Starting:', p.name, p.pid, flush=True)
    print('Exiting :', p.name, p.pid, flush=True)


if __name__ == '__main__':
    print(print('==='*15 + ' < ' + 'MAIN PROCESS' + ' > ' + '==='*15))
    logger = multiprocessing.log_to_stderr(logging.INFO)
    d = multiprocessing.Process(name='MyDaemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False

    d.start()
    print('==='*15)
    time.sleep(1)
    n.start()

    d.join()
    n.join()