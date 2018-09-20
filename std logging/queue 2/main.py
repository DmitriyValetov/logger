import logging
from logging.handlers import QueueHandler 
from multiprocessing import Process, Queue

from subpkg.process import run_calcs





logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

message_queue = Queue()

qh = QueueHandler(message_queue)
logger.addHandler(qh)
logger.addHandler(logging.FileHandler('all.log', mode='a+'))



logger.info('start process')

proc = Process(target=run_calcs, args=(message_queue,))
proc.start()

proc.join()
logger.info('all ended')