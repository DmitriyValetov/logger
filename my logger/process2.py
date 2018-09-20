from logger import logger
import time
import random

def process2():
    i = 0
    while i < 10:
        i += 1
        time.sleep(random.random())
        logger.info('process2: {}\n'.format(i))