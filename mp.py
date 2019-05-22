from multiprocessing import Pool
import time

def sqrt(x):
    return x**.5

now = time.time()

if __name__ == "__main__":
    numbers = [i for i in range(1000000)]
    with Pool(1) as pool:
        sqrt_ls = pool.map(sqrt, numbers)

print (time.time() - now)
