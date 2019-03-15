# import logging
# logging.basicConfig(filename="process.log", level=logging.INFO)
# logging.info("some message")





import logging
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
# formatter = logging.Formatter('%(message)s') # this is just message, no status and time

def setup_logger(name, log_file, level=logging.INFO):
    """Function setup as many loggers as you want"""

    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

# first file logger
logger = setup_logger('first_logger', 'first_logfile.log')
logger.info('This is just info message')

# second file logger
super_logger = setup_logger('second_logger', 'second_logfile.log')
super_logger.error('This is an error message')

def another_method():
   # using logger defined above also works here
   logger.info('Inside method')