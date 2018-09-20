from logger import logger
import time
import random


def processi(x):
    i = 0
    while i < 10:
        i += 1
        time.sleep(random.random())
        message = 'process{}: {}\n'.format(x, i)
        # logger.info('process{}: {}\n'.format(x, i))
        print(message)