from multiprocessing import Queue, Process
import time
import builtins


def my_print(message):
    global main_queue
    main_queue.put_nowait(message)

def log_process():
    global main_queue

    log_file = 'dump.txt'
    with open(file=log_file, mode='w+') as fout:
        pass

    while True:
        if not main_queue.empty():
            while not main_queue.empty():
                with open(file=log_file, mode='a+') as fout:
                    fout.write(main_queue.get())
        else:
            time.sleep(0.0001)


class Logger:
    def __init__(self, queue):
        self.queue = queue
        self.queue.put_nowait('logger activate\n')
        self.log_process = Process(target = log_process) 
        self.log_process.start()

    def info(self, message):
        self.queue.put_nowait(message)

    def stop(self):
        self.log_process.terminate()
        

main_queue = Queue()
logger = Logger(main_queue)
builtins.print = my_print