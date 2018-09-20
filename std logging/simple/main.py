import logging
from multiprocessing import Process
from subpkg.process import run_calcs


# logging.basicConfig(filename="sample.log", level=logging.DEBUG) 
# # Сообщение отладочное
# logging.debug( u'This is a debug message' )
# # Сообщение информационное
# logging.info( u'This is an info message' )
# # Сообщение предупреждение
# logging.warning( u'This is a warning' )
# # Сообщение ошибки
# logging.error( u'This is an error message' )
# # Сообщение критическое
# logging.critical( u'FATAL!!!' )


logger = logging.getLogger('main')
logger.setLevel(logging.INFO)


logger.info('start process')
proc = Process(target=run_calcs)
proc.start()
proc.join()
logger.info('all ended')