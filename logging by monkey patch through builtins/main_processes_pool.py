from logger import logger
from multiprocessing import Pool, Queue

from processi import processi


nCPU = 5
pool = Pool(processes = nCPU)
pool.map(processi, [i for i in range(nCPU)])


logger.info('all ended\n')