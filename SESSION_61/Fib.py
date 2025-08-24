def feb(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return feb(n-1)+feb(n-2)

print(feb(50))

'''
0 1 1 2 3 5 8 13 21 34 55
'''

class MemoisedFibonacci:
    def __init__(self, intN:int):
        assert intN >=0, "Fib of negative number cannot be applied"
        self.N = intN
        self.L = [None for i in range(self.N)]
        self.L[0] = 0
        self.L[1] = 1

    def compute(self, N):
        if self.L[N] is not None:
            return self.L[N]
        else:
            result = self.compute(N-1)+self.compute(N-2)
            self.L[N] = result
            return result
        
    def solve(self):
        return self.compute(self.N)