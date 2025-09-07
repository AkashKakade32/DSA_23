from time import time 

class ackerman: 
    def __init__(self, m, n): 
        assert m >= 0 and n >= 0, "m and n cannot be negative"
        self.m = m 
        self.n = n 
        # TODO 

    def compute(self, m, n): 
        # TODO 
        pass 

    def solve(self): 
        t_start = time() 
        result = self.compute(self.m, self.n)
        t_end = time() 
        T = (result, t_end-t_start)
        return T 
    

a = ackerman(3, 0)
result, delta = a.solve() 
print(f'ackerman({3}, {0}) = {result}, time required:{delta}')