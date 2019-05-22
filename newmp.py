##import os
## 
##from multiprocessing import Process, current_process
## 
## 
##def doubler(number):
##    """
##    A doubling function that can be used by a process
##    """
##    result = number * 2
##    proc_name = current_process().name
##    print('{0} doubled to {1} by: {2}'.format(
##        number, result, proc_name))
## 
## 
##if __name__ == '__main__':
##    numbers = [5, 10, 15, 20, 25]
##    procs = []
##    proc = Process(target=doubler, args=(5,))
## 
##    for index, number in enumerate(numbers):
##        proc = Process(target=doubler, args=(number,))
##        procs.append(proc)
##        proc.start()
## 
##    proc = Process(target=doubler, name='Test', args=(2,))
##    proc.start()
##    procs.append(proc)
## 
##    for proc in procs:
##        proc.join()

import multiprocessing as mp
import time

def foo_pool(x):
    return x*x

result_list = []
def log_result(result):
    # This is called whenever foo_pool(i) returns a result.
    # result_list is modified only by the main process, not the pool workers.
    result_list.append(result)

def apply_async_with_callback(processes = 4):
    pool = mp.Pool()
    for i in range(100000):
        pool.apply_async(foo_pool, args = (i, ), callback = log_result)
    pool.close()
    pool.join()
    #print(result_list)

now = time.time()

if __name__ == '__main__':
    apply_async_with_callback()
    print(time.time() - now)




