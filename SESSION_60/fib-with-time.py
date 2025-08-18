from time import time 
from sys import argv, exit

def F(n): 
    if n == 0: 
        return 0 
    if n == 1: 
        return 1 
    return F(n-1) + F(n-2)

def compute_fibo_with_time(n): 
    t_start = time() 
    ret_val = F(n)
    t_end = time() 
    print(f'Fib({n}):{ret_val}, time_required:{t_end-t_start}')

if len(argv) != 2: 
    print('UsageError:must give one integer on command line')
    exit() 

N = int(argv[1])

if N <= 0: 
    print('UsageError: Command line number must be positive')
    exit() 

for i in range(1, N+1): 
    compute_fibo_with_time(i)