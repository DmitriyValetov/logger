import logging
import time

def run_calcs(message_queue):

    i = 0
    logger = logging.getLogger('main.optalg')
    qh = logging.handlers.QueueHandler(message_queue)
    logger.addHandler(qh)
    logger.setLevel(logging.INFO)
    logger.info('process launched')


    while i < 5:
        i += 1
        time.sleep(1)
        print(i)
        logger.info('online: {}'.format(i))

    logger.info('done')