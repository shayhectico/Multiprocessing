##from dask.distributed import Client
##
##client = Client('localhost:8786')
from dask.distributed import Client, LocalCluster
cluster = LocalCluster(
     n_workers=4,
     ip='127.0.0.1',
)
client = Client(cluster)
