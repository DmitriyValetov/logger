import logging
import time

def run_calcs():
    i = 0
    logger = logging.getLogger('process')
    logger.setLevel(logging.INFO)
    logger.info('process launched')

    while i < 10:
        i += 1
        time.sleep(1)
        logger.info('online')

    logger.info('done')