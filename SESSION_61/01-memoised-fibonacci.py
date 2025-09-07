from time import time 
import sys 

sys.setrecursionlimit(100000)

class MemoisedFibonacci: 
    def __init__(self, initN:int): 
        assert initN >= 0, "Fibonacci of negative number cannot be computed"
        self.N = initN 
        self.L = [None for i in range(self.N+1)]
        self.L[0] = 0
        self.L[1] = 1 

    def compute(self, N):
        if self.L[N] is not None: 
            return self.L[N] 
        else:
            result = self.compute(N-1) + self.compute(N-2)
            self.L[N] = result 
            return result 

    def solve(self): 
        t_start = time() 
        r = self.compute(self.N)
        t_end = time() 
        return (r, t_end-t_start)

def traditionalFibo(N): 
    if N == 0: 
        return 0
    elif N == 1: 
        return 1 
    else:
        return traditionalFibo(N-1) + traditionalFibo(N-2)

for i in range(1, 40): 
    print(f"Fibonacci({i}):")
    print('Traditional Method:')
    t_start = time() 
    result = traditionalFibo(i)
    t_end = time() 
    print(f'Result:{result}, Required time:{t_end-t_start}')
    print("Memoised Fibonacci:")
    F = MemoisedFibonacci(i)
    (result, delta) = F.solve() 
    print(f'Result:{result}, Required Time:{delta}, number of digits:{len(str(result))}')
    print('-' * 80)
    
