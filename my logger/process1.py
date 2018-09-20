from logger import logger
import time
import random


def process1():
    i = 0
    while i < 10:
        i += 1
        time.sleep(random.random())
        logger.info('process1: {}\n'.format(i))