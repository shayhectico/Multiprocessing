
##import dask
##import time
##import dask.multiprocessing
##import dask.threaded
##import dask.distributed as dd
##import dask.delayed as delay
##from math import sqrt
##from dask.distributed import Client
##
##
##now = time.time()
##client = Client('127.0.0.1:8786')
##client = Client()
##def square(x):
##    return x ** 2
##
##def neg(x):
##    return -x
##
##A = client.map(square, range(10))
##B = client.map(neg, A)
##total = client.submit(sum, B)  
##    
##print(time.time() - now)


from distributed import Client, LocalCluster
cluster = LocalCluster()
client = Client(cluster)
