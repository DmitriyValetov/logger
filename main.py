from logger import logger
from multiprocessing import Process, Queue

from process1 import process1
from process2 import process2




proc1 = Process(target=process1)
proc2 = Process(target=process2)

proc1.start()
proc2.start()

proc1.join()
proc2.join()

logger.info('all ended\n')